
import customtkinter as ctk # Importa a biblioteca para o visual moderno e Modo Escuro
from datetime import datetime # Importa funções para ler a hora atual do seu computador
import varredura_fisica # Importa o seu módulo que traduz sensações do corpo
import dicionario # Importa o seu módulo com o banco de dados de sentimentos
import sqlite3
from datetime import datetime, timedelta
from pathlib import Path

import textos_smars
import historico_smars
import contato_smars

hora_atual = datetime.now().strftime("%H:%M")

def centralizar_janela(janela, largura, altura):
    # Pega a largura e altura da tela do seu computador
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Calcula a posição X e Y para o centro
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)

    # Define a geometria: "Largura x Altura + PosX + PosY"
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")



# --- CONFIGURAÇÃO DE CAMINHOS (Onde os arquivos moram) ---
BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)
LOGS_DIR = BASE_DIR / "logs"
LOGS_DIR.mkdir(exist_ok=True)

# Caminho unificado e absoluto para evitar erros de "no such table"
DB_PATH = BASE_DIR / "smars_logs.db"

def configurar_banco():
    """
    Cria o banco de dados e a tabela logs com a nova coluna entrada_bruta.
    """
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT,
            sentimento TEXT,
            intensidade INTEGER,
            identifica INTEGER,
            manejo TEXT,
            entrada_bruta TEXT
        )
    """)
    conn.commit()
    conn.close()
    

# Executa a configuração imediatamente ao carregar o script
configurar_banco()

def salvar_log(sentimento, intensidade, identifica, manejo, texto_original):
    """
    Salva os dados processados e o texto original da varredura no banco SQL.
    """
    try:
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        cursor.execute("""
            INSERT INTO logs (data_hora, sentimento, intensidade, identifica, manejo, entrada_bruta) 
            VALUES (?, ?, ?, ?, ?, ?)
        """, (agora, sentimento, intensidade, identifica, manejo, texto_original))
        
        conn.commit()
        conn.close()
        
    except Exception as e:
        print(f"❌ Erro ao salvar no banco: {e}")

# --- CONFIGURAÇÃO VISUAL DO SISTEMA ---
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# --- SISTEMA DE LOGS EM TEXTO (.TXT) ---
ARQUIVO_DIARIO = LOGS_DIR / f"log_{datetime.now().strftime('%Y-%m-%d')}.txt"

def salvar_entrada_usuario(texto_puro):
    """
    Salva a entrada bruta do usuário em um arquivo .txt como backup.
    """
    agora = datetime.now().strftime("%H:%M:%S")
    try:
        with open(ARQUIVO_DIARIO, "a", encoding="utf-8") as arquivo:
            arquivo.write(f"[{agora}] ENTRADA: {texto_puro}\n")
            arquivo.write("-" * 30 + "\n")
       
    except Exception as e:
        print(f"❌ Erro ao salvar log de texto: {e}")



# --- FUNÇÕES DAS JANELAS PRINCIPAIS ---


def abrir_scanner():
    """Abre apenas a janela de decisão inicial"""
    janela_decisao = ctk.CTkToplevel()
    janela_decisao.title("SMARS - SCANNER")
    centralizar_janela(janela_decisao, 400,200)
    janela_decisao.attributes("-topmost", True)
    janela_decisao.grab_set()

    ctk.CTkLabel(janela_decisao, text="VOCÊ CONSEGUE IDENTIFICAR\nO QUE ESTÁ SENTINDO?", font=("Segoe UI", 14, "bold")).pack(pady=30)
    
    frame_btns = ctk.CTkFrame(janela_decisao, fg_color="transparent")
    frame_btns.pack(pady=10)

    # Ao clicar nos botões abaixo, eles sim chamam a função 'processar_final' com os dados
    def vai_para_sim():
        janela_decisao.destroy()
        
        # Criando a janela de input personalizada
        input_janela = ctk.CTkToplevel()
        input_janela.title("MANEJO")
        centralizar_janela(input_janela, 400, 200) # AGORA ESTÁ CENTRALIZADA
        input_janela.attributes("-topmost", True)
        input_janela.configure(fg_color="#1a1a1a")

        ctk.CTkLabel(input_janela, text="O que sente?", font=("Segoe UI", 14, "bold")).pack(pady=20)
        
        entrada = ctk.CTkEntry(input_janela, width=300, fg_color="#242424", border_color="#1f538d")
        entrada.pack(pady=10)
        entrada.focus_set() # Foca o cursor automaticamente

        identifica =True

        def enviar():
            res = entrada.get()
            if res:
                input_janela.destroy()
                processar_final(res, "direto")

        ctk.CTkButton(input_janela, text="PROCESSAR", command=enviar, fg_color="#1f538d").pack(pady=15)
        # Permite apertar ENTER para enviar
        input_janela.bind('<Return>', lambda event: enviar())

    def vai_para_nao():
        janela_decisao.destroy()
        
        # Criando a janela de varredura personalizada
        input_janela = ctk.CTkToplevel()
        input_janela.title("VARREDURA")
        centralizar_janela(input_janela, 400, 200) 
        input_janela.attributes("-topmost", True)
        input_janela.configure(fg_color="#1a1a1a")

        ctk.CTkLabel(input_janela, text="Sensações físicas:", font=("Segoe UI", 14, "bold")).pack(pady=20)
        
        entrada = ctk.CTkEntry(input_janela, width=300, fg_color="#242424", border_color="#c0392b")
        entrada.pack(pady=10)
        entrada.focus_set()

        def enviar():
            res = entrada.get() 
            if res:
                salvar_entrada_usuario(res) 
            
            input_janela.destroy()
            processar_final(res, "fisico")

        identifica = False
        identifica = 0

    

        ctk.CTkButton(input_janela, text="PROCESSAR", command=enviar, fg_color="#c0392b").pack(pady=15)
        # Permite apertar ENTER para enviar
        input_janela.bind('<Return>', lambda event: enviar())
        
    ctk.CTkButton(frame_btns, text="SIM", command=vai_para_sim, fg_color="#1f538d", width=120).pack(side="left", padx=10)
    ctk.CTkButton(frame_btns, text="NÃO", command=vai_para_nao, fg_color="#c0392b", width=120).pack(side="left", padx=10)    

def exibir_interface_manejo(diag, expl, instr, frase,cat_match):
    import customtkinter as ctk

    # 1. CRIAR A ESTRUTURA INICIAL
    janela_res = ctk.CTkToplevel()
    janela_res.title("SMARS | Central de Manejo")
    
    # Ajustei a geometria inicial para permitir o crescimento vertical (scroll)
    centralizar_janela(janela_res,600,500) 
    janela_res.configure(fg_color="#0B0D14")
    janela_res.attributes("-topmost", True)
    janela_res.grab_set()
    
    # Deixa a janela invisível por um instante para evitar o "flash"
    janela_res.attributes("-alpha", 0.0) 

    def desenhar_conteudo(diag,expl,instr,frase, cat_match):
        # Cores de Acento (Dinâmicas conforme o diagnóstico)
        cat= str(cat_match).lower().strip()
        cor_acento= "#C7CACF"
        # 1. SENTIMENTOS RUINS / URGENTES (VERMELHO)
        if cat in ["medo", "raiva", "looping", "ansiedade", "tristeza", "sensorial", "shutdown", "dissociacao", "burnout", "mal_estar", "dor_cabeca", "nojo", "culpa", "rejeicao", "frustracao", "confusao"]:
            cor_acento = "#E11D48" 

    # 2. SENTIMENTOS MÉDIOS / ALERTAS (AMARELO)
        elif cat in ["fome", "sede", "cansaco", "inercia", "verbal", "injustica", "tedio", "stimming"]:
            cor_acento = "#F59E0B"

    # 3. SENTIMENTOS BONS / ESTÁVEIS (VERDE)
        else:
            cor_acento= "#10B981"
     
        
        # Container Scrollable para garantir que o texto longo não suma
        scroll_main = ctk.CTkScrollableFrame(janela_res, fg_color="transparent", width=580, height=600)
        scroll_main.pack(fill="both", expand=True, padx=5, pady=5)

        # Cabeçalho de Telemetria
        ctk.CTkLabel(scroll_main, text="Sistema de Manejo de Alexitimia e Reeducação Sentimental", 
                     font=("Segoe UI", 12, "bold"), text_color= "#335BC9").pack(pady=(20,0), padx=30, anchor="w")
        
        # Título do Diagnóstico (Usa wraplength para não fugir da tela)
        lbl_diag = ctk.CTkLabel(scroll_main, text=diag, font=("Segoe UI Light", 28), 
                                text_color=cor_acento, wraplength=500, justify="left")
        lbl_diag.pack(padx=30, pady=(0, 10), anchor="w")

        # Card Principal de Informações
        card = ctk.CTkFrame(scroll_main, fg_color="#161B2A", corner_radius=20, border_color=cor_acento,border_width=2)
        card.pack(fill="both", expand=True, padx=20, pady=10)

        # SEÇÃO: ANÁLISE TÉCNICA
        ctk.CTkLabel(card, text="ANÁLISE TÉCNICA", font=("Segoe UI", 12, "bold"), 
                     text_color=cor_acento,wraplength=480, justify="left").pack(pady=(20,0), padx=25, anchor="w")
        
        lbl_expl = ctk.CTkLabel(card, text=expl, font=("Segoe UI", 13), text_color="#CBD5E1", 
                                wraplength=480, justify="left")
        lbl_expl.pack(pady=10, padx=25, anchor="w")

        # Divisor sutil
        ctk.CTkFrame(card, height=1, fg_color="#1E293B").pack(fill="x", padx=25, pady=10)

        # SEÇÃO: INSTRUÇÕES DE MANEJO
        ctk.CTkLabel(card, text="INSTRUÇÕES / PROTOCOLO", font=("Segoe UI", 12, "bold"), 
                     text_color=cor_acento ,wraplength=480, justify="left").pack(pady=(10,0), padx=25, anchor="w")
        
        lbl_instr = ctk.CTkLabel(card, text=instr, font=("Segoe UI Semibold", 15), text_color="#FFFFFF", 
                                 wraplength=480, justify="left")
        lbl_instr.pack(pady=10, padx=25, anchor="w")

         # Divisor sutil
        ctk.CTkFrame(card, height=1, fg_color="#1E293B").pack(fill="x", padx=25, pady=5)

        # SEÇÃO: FRASE / LOG
        if frase:
            ctk.CTkLabel(card, text=f"{frase}", font=("Consolas", 14, "italic"), 
                         text_color="#3474CE",wraplength=480, justify="left").pack(pady=(0, 20), padx=25, anchor="w")

        # Botão de Estabilização (Fixo no final do scroll)
        ctk.CTkButton(scroll_main, text="FINALIZAR", command=janela_res.destroy, 
                      font=("Segoe UI", 13, "bold"), fg_color="#335BC9", 
                      hover_color="#254499", height=50, corner_radius=12).pack(pady=30, padx=30, fill="x")

        # Finalização: Torna visível e foca
        janela_res.attributes("-alpha", 1.0)
        try:
            janela_res.grab_set()
        except:
            pass

    # Executa o desenho após o delay de segurança
    janela_res.after(10, lambda: desenhar_conteudo(diag, expl, instr, frase, cat_match))

def processar_final(entrada_usuario, tipo_fluxo):
    """O Cérebro do SMARS: Conecta inputs ao motor_logico, dicionário e varredura"""
    import motor_logico 
    import dicionario
    from datetime import datetime
    
    sentimento_final = "Não Identificado"
    intensidade = 5
    cat_match = "outro"
   

    try:
        # --- CAMINHO A: IDENTIFICAÇÃO DIRETA ---
        if tipo_fluxo == "direto":
            
            sentimento_final = entrada_usuario
            dialog = ctk.CTkInputDialog(text="Intensidade (1 a 10):", title="INTENSIDADE")
            dialog.geometry(f"+{int(dialog.winfo_screenwidth()/2 - 150)}+{int(dialog.winfo_screenheight()/2 - 100)}")
            int_input= dialog.get_input()
            

            intensidade = 5 # Valor padrão caso o input seja cancelado
            if int_input and int_input.isdigit():
                intensidade = int(int_input)
            
            identifica = True

            # Busca no arquivo dicionario.py
            cat_match = dicionario.buscar_sentimento(entrada_usuario)
            #se não achar, aprende.
            if not cat_match:
                dicionario.aprender_novo_termo(entrada_usuario)
                

        # --- CAMINHO B: TRADUÇÃO POR VARREDURA FÍSICA ---
        elif tipo_fluxo == "fisico":
        # 1. O SISTEMA ACESSA OS SENSORES HARDWARE
        # O detectado_bruto já vem limpo (ex: "fome" ou "sono_exaustao")
            detectado_bruto = varredura_fisica.tradutor_fisico(entrada_usuario)
        
        # REMOVA O .UPPER()! Queremos manter o texto limpo para a ponte.
        sentimento_final = str(detectado_bruto).strip() 

        intensidade = 7  
        identifica = False

        # 2. PONTE DE CATEGORIAS 

        ponte_categorias = {
          "ansiedade": "ansiedade",
        "sobrecarga": "sensorial",
        "inercia": "inercia",
        "burnout": "burnout",
        "rsd": "rsd",
        "tristeza": "tristeza",
        "afeto": "afeto",
        "hiperfoco": "hiperfoco",
        "raiva": "raiva",
        "confusao": "confusao",
        "medo": "medo",
        "shutdown": "shutdown",
        "dissociacao": "dissociacao",
        "paz": "paz",
        "vergonha": "vergonha",
        "tedio": "tedio",
        "vergonha_alheia": "vergonha_alheia",
        "fome": "fome",
        "sede": "sede",
        "sono": "sono",
        "meltdown": "Meltdown",
        "injustica": "injustica",
        "solidao": "solidao",
        "nao_verbal": "nao_verbal",
        "orgulho": "orgulho",
        "gratidao": "gratidao",
        "ecolalia": "ecolalia",
        "mal_estar": "mal_estar",
        "dor_de_cabeca": "dor_de_cabeca",
        "alivio": "alivio",
        "nojo": "nojo",
        "curiosidade": "curiosidade",
        "stimming": "stimming",
        "alegria" : "alegria",
        "luto": "luto"
        
        }
        
        # 3. BUSCA NA PONTE
        # Se o sentimento_final for "fome", ele acha "fome" na ponte.
        cat_match = ponte_categorias.get(sentimento_final, "outro")
        # --- 4. EXECUÇÃO DO RELATÓRIO REFINADO (FINALIZAÇÃO COMUM) ---
        try:
            hora_atual = datetime.now().strftime("%H:%M")
            
            # Busca as explicações sofisticadas no motor_logico.py
            diag, expl, instr, frase = motor_logico.obter_relatorio(cat_match, intensidade, hora_atual)
            
            # Exibe na interface SMARS (Estilo requinte)
            exibir_interface_manejo(diag, expl, instr, frase, cat_match)
            
            # Criamos uma string organizada para o banco não reclamar da "tupla"
            relatorio_texto = f"DIAGNÓSTICO: {diag}\n\nEXPLICAÇÃO: {expl}\n\nMANEJO: {instr}\n\n{frase}"
    
             # Agora passamos o TEXTO (relatorio_texto) e não a tupla
            salvar_log(sentimento_final, intensidade, identifica,manejo=relatorio_texto, texto_original=entrada_usuario)
            
        except Exception as e:
            print(f"Erro ao processar motor lógico ou interface: {e}")

    except Exception as e:
        print(f"ERRO CRÍTICO NO SISTEMA SMARS: {e}")





#-----------------------------------------------------------------------


# --- INTERFACE PRINCIPAL (DASHBOARD) ---

def criar_painel_principal():
    root = ctk.CTk() # Cria a janela principal do programa
    root.title("SMARS - Painel de Controle") # Nome da janela na barra superior
    centralizar_janela(root,500,500) # Define o tamanho da janela (Largura x Altura)
    root.grab_set()

    # Título principal do Dashboard no topo da tela
    ctk.CTkLabel(root, text="SISTEMA DE MANEJO DE ALEXITIMIA E REEDUCAÇÃO SENTIMENTAL", font=("Segoe UI", 14, "bold")).pack(pady=30)
    
    # Cria um 'Frame' (uma caixa invisível) para organizar o botão principal
    frame_menu = ctk.CTkFrame(root, fg_color="transparent")
    frame_menu.pack(pady=0, padx=10, fill="both", expand=True)

    # --- COMANDO DE CENTRALIZAÇÃO ---
    # Esta linha abaixo é o segredo: ela dá "peso" à coluna 0, forçando-a a ocupar o centro do frame
    frame_menu.grid_columnconfigure(0, weight=1) 
    # --------------------------------

   # BOTÃO 1: SCANNER
    btn_scanner = ctk.CTkButton(
        frame_menu, text="IDENTIFICAR SENTIMENTO", 
        width=280, height=55, # Aumentei um pouco a largura para ficar mais imponente
        font=("Segoe UI", 14, "bold"), 
        fg_color="#1f538d", # O azul oficial do SMARS
        hover_color="#14375e", # Azul mais escuro ao passar o mouse
        command=abrir_scanner
    )
    btn_scanner.grid(row=0, column=0, padx=15, pady=12) 

    # Cria um 'Frame' (uma caixa invisível) para organizar os botões secundarios
    frame_menu2 = ctk.CTkFrame(root, fg_color="transparent")
    frame_menu2.pack(pady=0, padx=10, fill="both", expand=True)


    # BOTÃO 2: HISTÓRICO
    btn_hist = ctk.CTkButton(
        frame_menu2, text="HISTÓRICO DE SENTIMENTOS", 
        width=200, height=40,
        font=("Segoe UI", 11, "bold"),
        fg_color="#1f538d",
        hover_color="#14375e",
        command= historico_smars.abrir_historico
    )
    btn_hist.grid(row=1, column=0, padx=15, pady=12) 

     # BOTÃO 3: EXPLICAÇÃO SENTIMENTOS
    btn_conceito = ctk.CTkButton(
        frame_menu2, text="O QUE SÃO SENTIMENTOS?", 
        width=200, height=40,
        font=("Segoe UI", 11, "bold"),
        fg_color="#1f538d",
        hover_color="#14375e",
        command= textos_smars.abrir_conceito
    )
    btn_conceito.grid(row=1, column=1, padx=15, pady=12) 

   
    # BOTÃO 4: EXPLICAÇÃO PROGRAMA (O QUE É O SMARS)
    btn_programa = ctk.CTkButton(
        frame_menu2, text="O QUE É O 'SMARS'?", 
        width=200, height=40,
        font=("Segoe UI", 11, "bold"),
        fg_color="#1f538d",
        hover_color="#14375e",
        command=textos_smars.abrir_sobre_projeto
    )
    btn_programa.grid(row=2, column=0, padx=15, pady=12) 

    # BOTÃO 5: COMO USAR? (COMO USAR O SMARS)
    btn_programa = ctk.CTkButton(
        frame_menu2, text="COMO USAR?", 
        width=200, height=40,
        font=("Segoe UI", 11, "bold"),
        fg_color="#1f538d",
        hover_color="#14375e",
        command=textos_smars.abrir_comousar
    )
    btn_programa.grid(row=2, column=1, padx=15, pady=12) 

 # BOTÃO 6: PRA QUE SERVE? (COMO USAR O SMARS)
    btn_programa = ctk.CTkButton(
        frame_menu2, text="PARA QUE SERVE O 'SMARS'?", 
        width=200, height=40,
        font=("Segoe UI", 11, "bold"),
        fg_color="#1f538d",
        hover_color="#14375e",
        command=textos_smars.abrir_intuito
    )
    btn_programa.grid(row=3, column=0, padx=15, pady=12) 

    # BOTÃO 7: EXPLICAÇÃO ALEXITIMIA (O QUE É ALEXITIMIA)
    btn_alexi = ctk.CTkButton(
        frame_menu2, text="O QUE É ALEXITIMIA?", 
        width=200, height=40,
        font=("Segoe UI", 11, "bold"),
        fg_color="#1f538d",
        hover_color="#14375e",
        command=textos_smars.abrir_explicacao_alexitimia
    )
    btn_alexi.grid(row=3, column=1, padx=15, pady=12)

    # Cria um 'Frame' (uma caixa invisível) para organizar o botão principal
    frame_rodape = ctk.CTkFrame(root, fg_color="transparent")
    frame_rodape.pack(pady=(0,0), padx=10, fill="both", expand=True)

    # --- COMANDO DE CENTRALIZAÇÃO ---
    # Esta linha abaixo é o segredo: ela dá "peso" à coluna 0, forçando-a a ocupar o centro do frame
    frame_rodape.grid_columnconfigure(0, weight=1) 
    # --------------------------------

   # BOTÃO 8: CONTATO
    btn_contato = ctk.CTkButton(
        frame_rodape, text="INFORMAÇÕES DE CONTATO", 
        width=160, height=25, # Aumentei um pouco a largura para ficar mais imponente
        font=("Segoe UI", 10, "bold"), 
        fg_color="#384452", # O azul oficial do SMARS
        hover_color="#14375e", # Azul mais escuro ao passar o mouse
        command=contato_smars.abrir_contato
        
    )
    btn_contato.grid(row=0, column=0, padx=20, pady=(40,0)) 

    ctk.CTkLabel(
        frame_rodape, 
        text="SMARS - 2026", 
        font=("Consolas", 11),
        text_color="gray" 
        ).grid(row=1, column=0, padx=20, pady=(2, 10))

    root.mainloop() # Mantém o programa rodando
# Ponto de entrada que inicia tudo
if __name__ == "__main__":

    criar_painel_principal()
    configurar_banco()
    