import tkinter as tk # Importa a biblioteca base para interfaces gráficas
import customtkinter as ctk # Importa a biblioteca para o visual moderno e Modo Escuro
from datetime import datetime # Importa funções para ler a hora atual do seu computador
import varredura_fisica # Importa o seu módulo que traduz sensações do corpo
import dicionario # Importa o seu módulo com o banco de dados de sentimentos
import sqlite3
from datetime import datetime, timedelta
import motor_logico  # Importa o arquivo de manejo
import sqlite3
from datetime import datetime, timedelta


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

def configurar_banco():
    conn = sqlite3.connect("smars_logs.db")
    cursor = conn.cursor()
    # Cria a tabela se ela não existir
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT,
            sentimento TEXT,
            intensidade INTEGER,
            identifica INTEGER,
            manejo TEXT
        )
    """)
    conn.commit()
    conn.close()

# Chama a configuração ao iniciar o programa
configurar_banco()

def salvar_log(sentimento, intensidade, identifica, manejo):
    conn = sqlite3.connect("smars_logs.db")
    cursor = conn.cursor()
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    cursor.execute("INSERT INTO logs (data_hora, sentimento, intensidade, identifica, manejo) VALUES (?, ?, ?, ?, ?)", 
                   (agora, sentimento, intensidade,identifica, manejo))
    conn.commit()
    conn.close()

# --- CONFIGURAÇÃO VISUAL DO SISTEMA ---
ctk.set_appearance_mode("dark") # Define que o programa rodará sempre em Modo Escuro
ctk.set_default_color_theme("blue") # Define a cor azul como padrão para botões e detalhes

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
        centralizar_janela(input_janela, 400, 200) # AGORA ESTÁ CENTRALIZADA
        input_janela.attributes("-topmost", True)
        input_janela.configure(fg_color="#1a1a1a")

        ctk.CTkLabel(input_janela, text="Sensações físicas:", font=("Segoe UI", 14, "bold")).pack(pady=20)
        
        entrada = ctk.CTkEntry(input_janela, width=300, fg_color="#242424", border_color="#c0392b")
        entrada.pack(pady=10)
        entrada.focus_set()

        identifica = False

        def enviar():
            res = entrada.get()
            if res:
                input_janela.destroy()
                processar_final(res, "fisico")

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
            detectado_bruto = varredura_fisica.tradutor_fisico(entrada_usuario)
          
            sentimento_final = str(detectado_bruto).upper()
            dialog = ctk.CTkInputDialog(text="Intensidade (1 a 10):", title="INTENSIDADE")
            dialog.geometry(f"+{int(dialog.winfo_screenwidth()/2 - 150)}+{int(dialog.winfo_screenheight()/2 - 100)}")
            int_input= dialog.get_input()

            intensidade = 7  # Nível de alerta padrão para detecção via sensores (Telemetria Automática)
            if int_input and int_input.isdigit():
                intensidade = int(int_input)

            identifica = False

            # 2. PONTE DE CATEGORIAS (MAPEAMENTO PARA O MOTOR LÓGICO)
            ponte_categorias = {
                "FOME": "fome", "SEDE": "sede", "SONO / EXAUSTÃO": "cansaco",
                "MAL-ESTAR FÍSICO": "mal_estar", "DOR DE CABEÇA / ENXAQUECA": "dor_cabeca",
                "MELTDOWN (CRISE EXTERNA)": "sensorial", "SHUTDOWN (CRISE INTERNA)": "shutdown",
                "SOBRECARGA SENSORIAL": "sensorial", "BURNOUT (ESGOTAMENTO)": "burnout",
                "DISSOCIAÇÃO": "dissociacao", "INÉRCIA EXECUTIVA": "inercia", 
                "HIPERFOCO / EMPOLGAÇÃO": "hiperfoco", "CONFUSÃO / OVERLOAD COGNITIVO": "confusao", 
                "ECOLALIA (REPETIÇÃO)": "looping", "CURIOSIDADE": "curiosidade",
                "ANSIEDADE / PÂNICO": "ansiedade", "RSD (DISFORIA SENSÍVEL À REJEIÇÃO)": "rejeicao", 
                "TRISTEZA / ANGÚSTIA": "tristeza", "AFETO / AMOR": "afeto",
                "RAIVA": "raiva", "MEDO / INSEGURANÇA": "medo", "FRUSTRAÇÃO": "frustracao", 
                "SOLIDÃO": "solidao", "ORGULHO / SUCESSO": "orgulho", "GRATIDÃO": "gratidao", 
                "PAZ / HOMEOSTASE": "paz", "INJUSTIÇA": "injustica", "NOJO / AVERSÃO": "nojo",
                "STIMMING (AUTORREGULAÇÃO)": "stimming"
            }
            
            # 3. TRATAMENTO DE BUSCA NA PONTE
            cat_match = ponte_categorias.get(sentimento_final.strip(), "outro")

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
            salvar_log(sentimento_final, intensidade, identifica,manejo=relatorio_texto)
            
        except Exception as e:
            print(f"Erro ao processar motor lógico ou interface: {e}")

    except Exception as e:
        print(f"ERRO CRÍTICO NO SISTEMA SMARS: {e}")



# --- 2. FUNÇÃO QUE CRIA A INTERFACE ---
def abrir_historico():
    janela = ctk.CTkToplevel()
    janela.title("SMARS - HISTÓRICO DE SENTIMENTOS")
    centralizar_janela(janela,700, 650)
    janela.attributes("-topmost", False)
    janela.lift()
    janela.focus_force()
    janela.configure(fg_color="#1a1a1a")
    janela.grab_set()

    ctk.CTkLabel(janela, text="REGISTROS DE SENTIMENTOS", font=("Segoe UI", 24, "bold"), text_color="#1f538d").pack(pady=(20, 10))

    frame_filtros = ctk.CTkFrame(janela, fg_color="transparent")
    frame_filtros.pack(pady=10, padx=10, fill="x")

    container_cards = ctk.CTkScrollableFrame(janela, width=550, height=400, fg_color="#242424", scrollbar_button_color="#1f538d", corner_radius=15)
    container_cards.pack(pady=10, padx=20, fill="both", expand=True)

    estilo_btn = {"width": 100, "height": 35, "font": ("Segoe UI", 12, "bold")}

    # Os botões agora chamam a função de carga passando o container correto
    ctk.CTkButton(frame_filtros, text="24 HORAS", command=lambda: carregar_logs(container_cards,janela, 1), **estilo_btn).pack(side="left", padx=10, expand=True)
    ctk.CTkButton(frame_filtros, text="7 DIAS", command=lambda: carregar_logs(container_cards, janela,7), **estilo_btn).pack(side="left", padx=10, expand=True)
    ctk.CTkButton(frame_filtros, text="30 DIAS", command=lambda: carregar_logs(container_cards, janela,30), **estilo_btn).pack(side="left", padx=10, expand=True)
    ctk.CTkButton(frame_filtros, text="TODOS", command=lambda: carregar_logs(container_cards, janela), **estilo_btn).pack(side="left", padx=10, expand=True)
    ctk.CTkButton(frame_filtros, text="EXCLUIR HISTÓRICO", command=lambda: confirmar_limpeza_total(container_cards),fg_color="#962d22",hover_color="#e74c3c",**estilo_btn).pack(side="left", padx=10, expand=True)

    # Iniciar carregando os dados assim que abrir
    carregar_logs(container_cards,janela)

    ctk.CTkButton(janela, text="CONCLUIR", font=("Segoe UI", 14, "bold"), fg_color="#d35400", hover_color="#a04000", height=45, command=janela.destroy).pack(side="bottom", pady=25)



# --- 1. FUNÇÃO QUE APENAS BUSCA NO BANCO E DESENHA OS CARDS ---
def carregar_logs(container_cards, janela=None, filtro_dias=None):
    # Limpeza visual do container
    for widget in container_cards.winfo_children():
        widget.destroy()

    try:
        import sqlite3
        conn = sqlite3.connect("smars_logs.db")
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(logs)")
        print(cursor.fetchall())
        
        if filtro_dias is not None:
            query = "SELECT * FROM logs WHERE data_hora >= datetime('now', 'localtime', ?) ORDER BY id DESC"
            cursor.execute(query, (f"-{filtro_dias} days",))
        else:
            cursor.execute("SELECT * FROM logs ORDER BY id DESC")
            
        rows = cursor.fetchall()
        
        if not rows:
            ctk.CTkLabel(container_cards, text=">>> NENHUM LOG REGISTRADO.", font=("Segoe UI", 14, "italic"), text_color="gray").pack(pady=50)
        else:
           for row in rows:
            # 1. CRIAR O CARD
            # O master deve ser o container_cards. 
            card = ctk.CTkFrame(container_cards, fg_color="#2b2b2b", corner_radius=10, border_width=1, border_color="#3d3d3d")
            
            # O SEGREDO: pack deve estar dentro do loop e com side="top"
            # Removi o 'expand=True' que estava fazendo um card "comer" o espaço do outro
            card.pack(pady=8, padx=10, fill="x", side="top", expand=False)

           
            # 2. TRATAMENTO DA DATA
            data_banco = row["data_hora"] 
            try:
                data_formatada = datetime.strptime(data_banco, "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y %H:%M")
            except:
                data_formatada = data_banco

            # 3. EXIBIÇÃO DOS DADOS (Alinhados à esquerda 'w')
            ctk.CTkLabel(card, text=f"DATA/HORA: {data_formatada}", font=("Segoe UI", 11), text_color="#1f538d").pack(anchor="w", padx=15)
            
            ctk.CTkLabel(card, text=str(row["sentimento"]).upper(), font=("Segoe UI", 19, "bold"), text_color="#ffffff").pack(anchor="w", padx=15)

            ctk.CTkLabel(card, text=f"NÍVEL DE TELEMETRIA: {row['intensidade']}", font=("Segoe UI", 13), text_color="#aaaaaa").pack(anchor="w", padx=15, pady=(0, 5))
            
              # 4. LÓGICA DO STATUS (Identifica)
            if row["identifica"] == 1:
                txt_status = "● INPUT DIRETO"
                cor_status = "#38CCC0" 
            else:
                txt_status = "● VARREDURA FÍSICA"
                cor_status = "#F0FF1D"

            lbl_status = ctk.CTkLabel(card, text=txt_status, font=("Consolas", 11, "bold"), text_color=cor_status)
            lbl_status.pack(anchor="e", padx=15, pady=(5, 0))

            # 5. FRAME DE AÇÕES (Para os botões ficarem lado a lado sem bugar o card)
            frame_acoes = ctk.CTkFrame(card, fg_color="transparent")
            frame_acoes.pack(fill="x", padx=10, pady=(5, 10))

            # Captura o ID corretamente para o lambda não apagar o item errado
            id_atual = row["id"]

            btn_info = ctk.CTkButton(
                frame_acoes, text="INFO", width=60, height=30,
                command=lambda r=row: mostrar_detalhes(r["data_hora"], r["sentimento"], r["intensidade"], r["manejo"], master_window=janela)
            )
            btn_info.pack(side="left", padx=5)

            # Botão Excluir usando uma função limpa para não bugar o SQLite
            def acao_excluir(id_p=id_atual):
                conn = sqlite3.connect("smars_logs.db")
                cursor = conn.cursor()
                cursor.execute("DELETE FROM logs WHERE id = ?", (id_p,))
                conn.commit()
                conn.close()
                carregar_logs(container_cards, janela)

            btn_del = ctk.CTkButton(
                frame_acoes, text="EXCLUIR", width=60, height=30, fg_color="#444", hover_color="red",
                command=acao_excluir
            )
            btn_del.pack(side="right", padx=5)

        
        conn.close()
        container_cards.update_idletasks() # Força o cálculo de geometria
    except Exception as e:
        print(f"Erro no banco: {e}")


def mostrar_detalhes(data_banco, sentimento, nivel, manejo_texto,master_window=None ):
    # Cria a janela com o tema escuro do SMARS
    detalhes = ctk.CTkToplevel(master_window)
    detalhes.title(f"TELEMETRIA: {sentimento.upper()}")
    centralizar_janela(detalhes,500,600)
    detalhes.attributes("-topmost", True)
    detalhes.configure(fg_color="#1a1a1a")
    detalhes.grab_set()

    # Título estilizado
    ctk.CTkLabel(detalhes, text="RELATÓRIO DE TELEMETRIA", 
                 font=("Segoe UI", 22, "bold"), text_color="#1f538d").pack(pady=(25, 10))
    
    ctk.CTkLabel(detalhes, text=sentimento.upper(), 
                 font=("Segoe UI", 22, "bold"), text_color="#307acf").pack(pady=(10, 5))

    # Header com Nivel
    header_frame = ctk.CTkFrame(detalhes, fg_color="transparent")
    header_frame.pack(pady=2)

    # Tratamento da Intensidade para garantir que a cor funcione
    # Remove o "/10" se ele existir para poder converter para inteiro
    nivel_limpo = str(nivel).split('/')[0]
    
    try:
        valor_nivel = int(nivel_limpo)
    except:
        valor_nivel = 5 # Valor padrão caso ocorra erro na conversão

    # Cor dinâmica para o nível
    cor_nivel = "#2ecc71" if valor_nivel <= 3 else "#f1c40f" if valor_nivel <= 7 else "#e74c3c"
    
    ctk.CTkLabel(header_frame, text=f"NÍVEL {nivel_limpo}/10", 
                 font=("Segoe UI", 12, "bold"), text_color=cor_nivel).pack(side="left")

    # Pegamos a data do banco (2026-03-24 11:15) e invertemos para exibição
    
    try:
    # Tenta converter o que veio do banco para o formato BR
        data_formatada = datetime.strptime(data_banco, "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y %H:%M")
    except:
    # Se o dado antigo ainda estiver no formato BR, ele apenas usa o que já tem
        data_formatada = data_banco

     # Header com data e hora
    header_frame1 = ctk.CTkFrame(detalhes, fg_color="transparent")
    header_frame1.pack(pady=2)
    ctk.CTkLabel(header_frame1, text=f"{data_formatada}", font=("Segoe UI", 12), text_color="gray").pack(side="left")
    
    
    # --- TRATAMENTO DO CONTEÚDO ---
    # O .strip("()") remove parênteses das extremidades caso venha como string de tupla
    conteudo_limpo = str(manejo_texto).strip("()").replace("'", "").replace(", ", "\n\n")
    
    # Caixa de texto estilizada para o relatório
    txt = ctk.CTkTextbox(detalhes, width=420, height=300, font=("Segoe UI", 14),
                         fg_color="#242424", border_color="#5c9ae0", border_width=2, corner_radius=15, wrap="word")
    txt.pack(pady=20, padx=20)
    
    # Título interno da caixa
    txt.insert("0.0", f"ANÁLISE DO SISTEMA\n\n{conteudo_limpo}")
    txt.configure(state="disabled")

    # Botão de fechar padrão
    ctk.CTkButton(
    detalhes, 
    text="CONCLUIR", 
    font=("Segoe UI", 13, "bold"),
    fg_color="#1f538d", 
    hover_color="#14375e", 
    
    # --- CONTROLE DE TAMANHO AQUI ---
    width=200,    # Altere este valor para a largura que desejar (em pixels)
    height=55,    # Altere este valor para a altura que desejar
    # --------------------------------
    
    corner_radius=10, # Opcional: deixa o botão mais arredondado ou quadrado
    command=detalhes.destroy
).pack(pady=20)
    

def confirmar_limpeza_total(container_cards):
    def acao_deletar():
        try:
            import sqlite3
            conn = sqlite3.connect("smars_logs.db")
            cursor = conn.cursor()
            cursor.execute("DELETE FROM logs")
            conn.commit()
            conn.close()
            
            # Fecha a janela de confirmação
            janela_confirma.destroy()
            
            # ATUALIZAÇÃO VISUAL: Limpa a tela de histórico imediatamente
            carregar_logs(container_cards)
            
        except Exception as e:
            print(f"Erro ao deletar: {e}")

    # Configuração da Janela de Confirmação
    janela_confirma = ctk.CTkToplevel()
    janela_confirma.title("CONFIRMAÇÃO CRÍTICA")
    centralizar_janela(janela_confirma,450,350)
    janela_confirma.attributes("-topmost", True)
    janela_confirma.configure(fg_color="#1a1a1a")
    janela_confirma.grab_set()

    aviso = ("ESSA AÇÃO APAGARÁ TODO O HISTÓRICO DE SENTIMENTOS.\n\n"
             "ESSA AÇÃO NÃO PODERÁ SER DESFEITA.\n\n"
             "O HISTÓRICO DE SENTIMENTO NUNCA SERÁ RECUPERADO.")
    
    ctk.CTkLabel(janela_confirma, text=aviso, text_color="#e74c3c", 
                 font=("Segoe UI", 13, "bold"), wraplength=400).pack(pady=30)

    # Botão de exclusão (inicia desativado)
    btn_excluir = ctk.CTkButton(janela_confirma, text="APAGAR HISTÓRICO", 
                                 fg_color="#c0392b", hover_color="#962d22",
                                 state="disabled", command=acao_deletar,
                                 font=("Segoe UI", 12, "bold"), height=40)
    
    # Lógica da trava de segurança
    def liberar_botao():
        if check_var.get() == "on":
            btn_excluir.configure(state="normal")
        else:
            btn_excluir.configure(state="disabled")

    check_var = ctk.StringVar(value="off")
    check = ctk.CTkCheckBox(janela_confirma, text="Compreendo e desejo prosseguir", 
                            variable=check_var, onvalue="on", offvalue="off", 
                            command=liberar_botao, font=("Segoe UI", 12),
                            fg_color="#1f538d", border_color="#1f538d")
    
    check.pack(pady=10)
    btn_excluir.pack(pady=20)





def abrir_explicacao_alexitimia():
    janela_alex = ctk.CTkToplevel()
    janela_alex.title("SMARS - O QUE É ALEXITIMIA?")
    centralizar_janela(janela_alex,650,650)
    janela_alex.attributes("-topmost", True)
    janela_alex.grab_set()

    # 1. BOTÃO PRIMEIRO (side="bottom" reserva o espaço do rodapé antes de tudo)
    btn_voltar = ctk.CTkButton(
        janela_alex, 
        text="COMPREENDIDO", 
        font=("Segoe UI", 14, "bold"),
        fg_color="#1f538d", 
        hover_color="#14375e",
        height=45,
        command=janela_alex.destroy
    )
    btn_voltar.pack(side="bottom", pady=(10, 25))

    # 2. CAIXA DE TEXTO (Ocupa o espaço que sobrar em cima do botão)
    caixa_texto = ctk.CTkTextbox(
        janela_alex, 
        font=("Segoe UI", 16), 
        border_spacing=30,
        fg_color="transparent",
        wrap="word"
    )
    caixa_texto.pack(padx=20, pady=(20, 0), fill="both", expand=True)

    texto_direto = (
        "ALEXITIMIA: A CIÊNCIA E A MEDIAÇÃO POR TRÁS DO SMARS\n"
        "______________________________________________________________\n\n"
        "A Alexitimia — termo derivado do grego 'Alexisthymos' (a = ausência, lexis = palavra, thymos = emoção) — "
        "não é uma descoberta recente, mas um constructo clínico consolidado. \nO termo foi cunhado pelo psiquiatra "
        "Peter Sifneos, de Harvard, em 1973, no artigo 'The prevalence of alexithymic characteristics in psychosomatic patients', "
        "publicado na revista Psychotherapy and Psychosomatics. Sifneos observou que pacientes com doenças psicossomáticas "
        "não possuíam um 'vocabulário de sentimentos', apresentando uma pobreza extrema na fantasia e no pensamento simbólico. "
        "\nNo SMARS, interpretamos essa observação original como uma falha crítica no 'Driver de Tradução': o hardware biológico "
        "dispara o sinal de pulso e tensão perfeitamente, mas o sistema consciente não possui o arquivo de legenda necessário "
        "para converter a biologia em símbolo linguístico.\n\n"
        
        "Cientificamente, essa barreira ocorre por uma disfunção na Interocepção, o oitavo sentido responsável por monitorar "
        "o estado interno do corpo através da Ínsula Anterior. Em indivíduos alexitímicos, há um ruído crônico nessa comunicação. "
        "É o que chamamos no SMARS de 'Telemetria Bruta': o corpo gera dados de voltagem (taquicardia, sudorese, nó na garganta), "
        "mas como a Ínsula não categoriza esses dados, a mente recebe apenas um log de 'Erro Crítico'. Sem a mediação do software, "
        "o indivíduo permanece em um estado de confusão sensorial, incapaz de discernir se o que sente é uma resposta emocional "
        "específica ou apenas um desconforto físico vago, o que frequentemente leva ao esgotamento por falta de regulação.\n\n"
        
        "Aprofundando ainda mais, a neurobiologia aponta para uma redução na conectividade funcional entre o Sistema Límbico "
        "e o Córtex Cingulado Anterior. Na nossa lógica de projeto, é um problema de 'Cabo de Rede Desconectado': o motor emocional "
        "está acelerando no máximo, mas o velocímetro na interface do usuário não recebe a informação. A fiação entre as partes opera "
        "com tamanha latência que a experiênca sentida se perde antes de ser rotulada. \nNo contexto neurodivergente, a 'Teoria do Mundo "
        "Intenso' de Markram e Markram (2007) sugere que o cérebro autista é hiper-reativo; logo, a Alexitimia surge como um "
        "'Modo de Proteção contra Sobrecarga' (Firewall Biológico). O sistema desativa as notificações de sentimento para evitar que "
        "o processador central entre em colapso (Meltdown) diante da intensidade avassaladora do mundo.\n\n"
        
        "A alma do SMARS, entretanto, reside na Pedagogia de Lev Vygotsky. Vygotsky defendia que o desenvolvimento humano é mediado "
        "por instrumentos e signos. O SMARS atua exatamente como um 'Andaime' dentro da Zona de Desenvolvimento Proximal "
        "(ZDP) — a distância entre o que o indivíduo consegue fazer sozinho e o que consegue com ajuda. \nComo o alexitímico não possui "
        "espontaneidade para nomear estados internos, o software fornece a mediação tecnológica (o signo) necessária para a tradução. "
        "Segundo Vygotsky, funções psicológicas superiores aparecem primeiro no plano social (entre pessoas ou entre pessoa e máquina) "
        "para depois serem internalizadas. Assim, ao usar o SMARS, o usuário não está apenas usando um scanner, mas reeducando sua "
        "percepção neural para, no futuro, conquistar sua autonomia emocional e dignidade cognitiva.\n\n"
        
        "REFERÊNCIAS BIBLIOGRÁFICAS:\n"
        "• SIFNEOS, P. E. (1973). The prevalence of 'alexithymic' characteristics in psychosomatic patients. Psychotherapy and Psychosomatics.\n"
        "• VYGOTSKY, L. S. (1978). Mind in Society: The Development of Higher Psychological Processes. Harvard University Press.\n"
        "• BIRD, G.; COOK, R. (2013). Mixed emotions: the contribution of alexithymia to the emotional symptoms of autism.\n"
        "• MARKRAM, H.; MARKRAM, K. (2007). The Intense World Theory – a unifying hypothesis for autism. Frontiers in Human Neuroscience.\n"
        "• HERBERT, B. M.; POLLATOS, O. (2012). The Relevance of Interoception in Clinical Disorders. Frontiers in Psychology."    
    )

    caixa_texto.insert("0.0", texto_direto)
    caixa_texto.configure(state="disabled")

def abrir_conceito():
    janela = ctk.CTkToplevel()
    janela.title("SMARS - O QUE SÃO SENTIMENTOS?")
    centralizar_janela(janela,650,650) 
    janela.attributes("-topmost", True)
    janela.grab_set()

    # Botão no fundo primeiro
    btn_sair = ctk.CTkButton(
        janela, 
        text="COMPREENDIDO", 
        font=("Segoe UI", 14, "bold"),
        fg_color="#1f538d", 
        hover_color="#14375e",
        height=45,
        command=janela.destroy
    )
    btn_sair.pack(side="bottom", pady=(10, 25))

    caixa_texto = ctk.CTkTextbox(
        janela, 
        font=("Segoe UI", 16), 
        border_spacing=35,
        fg_color="transparent",
        wrap="word"
    )
    caixa_texto.pack(padx=20, pady=(20, 0), fill="both", expand=True)

    texto_direto = (
        "O QUE SÃO SENTIMENTOS? \nUMA PERSPECTIVA NEUROBIOLÓGICA E COGNITIVA\n"
        "______________________________________________________________\n\n"
        "Cientificamente, o sentimento não é um evento isolado, mas o estágio final de um processo "
        "biológico complexo que visa a manutenção da vida. \nTudo começa com a Homeostase, o esforço do "
        "organismo para manter o equilíbrio interno. Através da Interocepção, o sistema nervoso monitora "
        "constantemente o estado dos órgãos e tecidos. \nQuando um estímulo externo ou interno ocorre, "
        "o corpo dispara uma Emoção — que, segundo António Damásio, é um conjunto de respostas químicas "
        "e neurais automáticas e universais. Essas respostas ocorrem no Sistema Límbico, especificamente "
        "na Amígdala, gerando alterações físicas imediatas como aceleração cardíaca, sudorese e tensão "
        "muscular, antes mesmo de qualquer percepção consciente.\n\n"
        "No ecossistema do SMARS, interpretamos essa cadeia biológica através da lógica de sistemas. "
        "As sensações físicas são a nossa 'Telemetria Bruta de Hardware': dados puros vindos de sensores "
        "periféricos informando sobre a voltagem e o status do organismo. \nAs emoções, por sua vez, são "
        "vistas como 'Protocolos de Segurança' ou scripts de execução rápida, desenhados para proteger "
        "a integridade do sistema operacional humano em situações de risco ou recompensa. \nO Sentimento "
        "surge, portanto, como o 'Relatório Processado pela CPU Central' (a mente consciente). Ele é a "
        "tradução semântica da pergunta: 'Por que meu hardware está agindo assim agora?'. É o momento "
        "em que o Córtex Pré-Frontal associa a eletricidade da emoção a um contexto, transformando a "
        "reação química em experiênca subjetiva e nomeável.\n\n"
        "Aprofundando na neurociência da consciência, esse processo de tradução depende da integridade "
        "funcional de áreas como a Ínsula Anterior e o Córtex Cingulado Posterior. A Teoria da Avaliação "
        "Cognitiva (Appraisal Theory) postula que o sentimento depende de como o cérebro avalia o estímulo. "
        "\nNa Alexitimia, ocorre um Erro de Driver crítico: há uma desconexão ou latência entre a leitura do "
        "corpo e a área de processamento de símbolos e linguagem. O hardware está 'quente' e os protocolos "
        "de emergência estão rodando em segundo plano, mas o sistema falha em gerar o relatório final. "
        "O usuário experimenta o impacto físico, mas o status do sistema permanece como 'Erro Desconhecido', "
        "o que impede a regulação e frequentemente leva ao superaquecimento do processador central (Meltdown).\n\n"
        "O SMARS finaliza este ciclo atuando como um Driver Externo de Intermediação, fundamentado na "
        "Pedagogia de Vygotsky. Ele fornece o 'Andaime' necessário na Zona de Desenvolvimento Proximal, "
        "oferecendo as legendas e os signos que o processador interno não consegue gerar sozinho no momento. "
        "\nAo mapear a telemetria física e sugerir diagnósticos lógicos, o software auxilia a CPU central a "
        "completar a tradução afetiva. O objetivo final é a Reeducação Neural Ativa, garantindo que, através "
        "da mediação tecnológica, o indivíduo reconquiste sua soberania emocional e a capacidade de ler "
        "seu próprio código interno com clareza e dignidade.\n\n"
        "REFERÊNCIAS BIBLIOGRÁFICAS:\n"
        "• DAMÁSIO, A. (2018). A Estranha Ordem das Coisas: As origens biológicas dos sentimentos. Companhia das Letras.\n"
        "• LAZARUS, R. S. (1991). Emotion and Adaptation. Oxford University Press. (Appraisal Theory).\n"
        "• SIFNEOS, P. E. (1973). The prevalence of 'alexithymic' characteristics in psychosomatic patients.\n"
        "• VYGOTSKY, L. S. (1978). Mind in Society: Development of Higher Psychological Processes.\n"
        "• MARKRAM, H.; MARKRAM, K. (2007). The Intense World Theory – a unifying hypothesis for autism."
    )

    caixa_texto.insert("0.0", texto_direto)
    caixa_texto.configure(state="disabled") 


def abrir_comousar():
    janela = ctk.CTkToplevel()
    janela.title("SMARS - COMO USAR?")
    centralizar_janela(janela,650,650) 
    janela.attributes("-topmost", True)
    janela.grab_set()

    # Botão no fundo primeiro
    btn_sair = ctk.CTkButton(
        janela, 
        text="VAMOS TESTAR", 
        font=("Segoe UI", 14, "bold"),
        fg_color="#1f538d", 
        hover_color="#14375e",
        height=45,
        command=janela.destroy
    )
    btn_sair.pack(side="bottom", pady=(10, 25))

    caixa_texto = ctk.CTkTextbox(
        janela, 
        font=("Segoe UI", 16), 
        border_spacing=35,
        fg_color="transparent",
        wrap="word"
    )
    caixa_texto.pack(padx=20, pady=(20, 0), fill="both", expand=True)

    texto_direto = (
        "SMARS \nCOMO USAR?\n"
        "______________________________________________________________\n\n"
        """Para iniciar o processo de tradução de sinais e regulação emocional,siga as instruções de navegação da interface:

1. INICIALIZAÇÃO DO SISTEMA:
No menu principal, selecione a opção [IDENTIFICAR SENTIMENTOS].
Este é o ponto de entrada para qualquer análise de sinais internos.

2. SELEÇÃO DE FLUXO (Status da CPU):
O sistema perguntará: "Sabe o que está sentindo?". Escolha o caminho baseado na clareza do seu processador central no momento:

A) SE VOCÊ JÁ NOMEOU O SENTIMENTO QUE ESTÁ SENTINDO:
 - Clique em SIM.
 - Insira o nome do sentimento que você identificou
 (Ex: Ansiedade, Sobrecarga).
- Aguarde o processamento do "MANEJO-RESPOSTA" com as instruções.

B) SE VOCÊ NÃO SABE O NOME DO QUE ESTÁ SENTINDO:
  - Clique em NÃO.
  - O sistema abrirá um campo para entrada da TELEMETRIA BRUTA.
  - Descreva as sensações físicas e mentais exatamente como você as sente.

EXEMPLOS DE ENTRADA:
  > "Sinto que minha mente vai explodir, tô acelerada, mãos frias."
  > "Sinto minha barriga agitada, mãos suando e mente inquieta."
  > "Meus olhos estão pesados, minha cabeça tá doendo."
  > "To com um aperto na barriga e minha cabeça tá meio zonza."

3. PROCESSAMENTO E SAÍDA:
Após o envio do SENTIMENTO ou SENSAÇÕES, o SMARS atuará como  seu Driver de Intermediação, cruzando os dados para sugerir o  diagnóstico lógico e acender o "painel" em meio a tempestade."""
    )

    caixa_texto.insert("0.0", texto_direto)
    caixa_texto.configure(state="disabled") 


def abrir_sobre_projeto():
    janela_sobre = ctk.CTkToplevel()
    janela_sobre.title("SMARS - SISTEMA DE MANEJO DE ALEXITIMIA E REEDUCAÇÃO SENTIMENTAL")
    centralizar_janela(janela_sobre,650,650)
    janela_sobre.attributes("-topmost", True)
    janela_sobre.grab_set()

    # Botão no fundo primeiro
    btn_voltar = ctk.CTkButton(
        janela_sobre, 
        text="COMPREENDIDO", 
        font=("Segoe UI", 14, "bold"),
        fg_color="#1f538d", 
        hover_color="#14375e",
        height=45,
        command=janela_sobre.destroy
    )
    btn_voltar.pack(side="bottom", pady=(10, 25))

    caixa_texto = ctk.CTkTextbox(
        janela_sobre, 
        font=("Segoe UI", 16), 
        border_spacing=35,
        fg_color="transparent",
        wrap="word"
    )
    caixa_texto.pack(padx=20, pady=(20, 0), fill="both", expand=True)

    texto_manifesto = (
        "SMARS \nSISTEMA DE MANEJO DE ALEXITIMIA E REEDUCAÇÃO SENTIMENTAL\n"
        "______________________________________________________________\n\n"
        "O SMARS não é meramente um utilitário de software, é uma infraestrutura de mediação projetada para a "
        "independência cognitiva. Ele nasce para preencher um hiato crítico no processamento de informações "
        "humanas: a incapacidade de converter o fluxo caótico de sinais interoceptivos em símbolos linguísticos "
        "operáveis pela consciência. \nO SMARS é a ponte tecnológica construída para atravessar o abismo da "
        "Alexitimia, transformando o impacto sensorial bruto em conhecimento estratégico e autogestão emocional.\n\n"
        "A necessidade deste sistema fundamenta-se na realidade de que, para o indivíduo neurodivergente, a "
        "existência ocorre frequentemente sob uma 'Tempestade de Dados'. \nImagine pilotar uma aeronave complexa "
        "através de uma névoa densa onde todos os indicadores de telemetria — altitude, velocidade e combustível — "
        "estão em pane ou desconectados. \nO mundo atípico é percebido com uma intensidade avassaladora, mas sem os "
        "instrumentos de leitura adequados. \nO SMARS não pretende silenciar a tempestade ou suprimir as reações "
        "biológicas; seu propósito é ACENDER O PAINEL DE CONTROLE. Ele fornece a interface de visualização "
        "necessária para que a navegação pela vida deixe de ser uma reação desesperada ao caos e passe a ser "
        "uma ação consciente e calculada.\n\n"
        "A Filosofia do Exoesqueleto Mental postula que a neurodivergência não é um erro de código a ser corrigido "
        "ou uma patologia a ser curada, mas uma arquitetura de hardware alternativa que requer drivers de interface "
        "específicos. \nAssim como um exoesqueleto que devolve a função motora ao corpo, o SMARS atua como uma prótese "
        "cognitiva que devolve a função de INTERPRETAÇÃO. \nAtravés da mediação tecnológica fundamentada na Pedagogia "
        "de Vygotsky, o sistema opera na Zona de Desenvolvimento Proximal do usuário, oferecendo os 'signos' e 'ferramentas' "
        "externas que permitem a internalização progressiva da capacidade de nomear e gerir o próprio estado interno.\n\n"
        "Os Pilares de Excelência Operacional do SMARS garantem essa soberania. No âmbito da Segurança e Prevenção, "
        "o sistema funciona como um sentinela térmico, identificando padrões de superaquecimento químico — como a "
        "elevação abrupta da voltagem cardíaca e tensão muscular — para antecipar estados de Meltdown e Shutdown "
        "antes do colapso do sistema. \nNo campo da Dignidade Humana, o SMARS desmancha a dependência de intérpretes "
        "externos, garantindo que a autoridade sobre o que é sentido pertença exclusivamente ao indivíduo. \nPor fim, "
        "através da Reeducação Neural, cada interação com o algoritmo é um reforço sináptico que treina a mente "
        "para reconhecer sua própria biologia.\n\n"
        "O SMARS existe porque o autoconhecimento não deve ser um labirinto inacessível ou um diagnóstico imposto por "
        "terceiros, mas um direito humano fundamental. Esta interface é desenvolvida para garantir "
        "que o indivíduo atípico deixe de ser um passageiro à mercê de suas reações químicas e se torne o mestre "
        "absoluto de seu próprio código interno."
    )

    caixa_texto.insert("0.0", texto_manifesto)
    caixa_texto.configure(state="disabled")


def abrir_intuito():
    janela = ctk.CTkToplevel()
    janela.title("SMARS - ARQUITETURA OPERACIONAL")
    centralizar_janela(janela,650,650) 
    janela.attributes("-topmost", True)
    janela.grab_set()

    # Botão no fundo primeiro
    btn_sair = ctk.CTkButton(
        janela, 
        text="COMPREENDIDO", 
        font=("Segoe UI", 14, "bold"),
        fg_color="#1f538d", 
        hover_color="#14375e",
        height=45,
        command=janela.destroy
    )
    btn_sair.pack(side="bottom", pady=(10, 25))

    caixa_texto = ctk.CTkTextbox(
        janela, 
        font=("Segoe UI", 16), 
        border_spacing=35,
        fg_color="transparent",
        wrap="word"
    )
    caixa_texto.pack(padx=20, pady=(20, 0), fill="both", expand=True)

    texto_direto = (
       
    """COMO FUNCIONA O SMARS?
A ENGENHARIA DA REEDUCAÇÃO SENTIMENTAL E AUTONOMIA
________________________________________________________________________

O SMARS opera como um EXOESQUELETO MENTAL TEMPORÁRIO. Seu funcionamento não visa criar dependência tecnológica, mas sim realizar uma "atualização" no processador central do usuário (a mente), utilizando os princípios da Pedagogia de Vygotsky.

O sistema funciona através de três estágios de maturação:


1. O ESTÁGIO DO APOIO (Mediação Externa):
   No início, o usuário enfrenta a "névoa" da Alexitimia e não consegue "enxergar" os proprios sentimentos.
   O SMARS entra como o INSTRUMENTO DE MEDIAÇÃO. 

   - O QUE O SOFTWARE FAZ: Ele fornece as palavras, os nomes e os caminhos que você ainda não consegue visualizar sozinho. Ele vai segurar todo o peso da interpretação e do processamento enquanto seu sistema interno está sobrecarregado e te fornecerá intruções para aquele momento.

   - O OBJETIVO: Estabilizar o hardware e evitar o Meltdown imediato através de instruções externas de manejo e controle.

   
2. A ZONA DE DESENVOLVIMENTO PROXIMAL (Aprendizado Ativo)
   Com o uso contínuo, o funcionamento do SMARS cria um "Andaime". Cada vez que você descreve uma sensação fisica e o programa associa a um sentimento ou busca como lidar com um sentimento e o programa sugere um manejo, você está treinando seu cérebro a fazer essa associação.

   - O QUE O SOFTWARE FAZ: Ele cria o link lógico entre o SINAL FÍSICO (ex: mão suando) e o SIGNIFICADO (ex: ansiedade) e cria a associação entre SENTIMENTO e MANEJO.

   - O OBJETIVO: Diminuir a latência entre o sentir, o entender e o agir.

   
3. A INTERIORIZAÇÃO (Soberania e Autonomia)
   Este é o estágio final do uso do SMARS. De acordo com a teoria de Vygotsky, o que antes era feito com ajuda externa passa a ser feito internamente. 

   - O QUE ACONTECE: O raciocínio lógico do programa é absorvido pelas suas próprias sinapses. Você começa a identificar as sensações, linka-las aos sentimentos correspondentes e a aplicar os manejos SOZINHO E AUTOMATICAMENTE, antes mesmo de abrir o software.

   - O OBJETIVO FINAL: Que o SMARS se torne obsoleto. O intuito é que você "desinstale" a necessidade de usa-lo, porque agora você possui a SOBERANIA ABSOLUTA sobre o seu próprio código interno.

   
MISSÃO OPERACIONAL: 

O SMARS te apoia hoje para que você não precise de apoio amanhã. 
A tecnologia a serviço da autonomia do sentir."""
    )

    caixa_texto.insert("0.0", texto_direto)
    caixa_texto.configure(state="disabled")


def abrir_contato():
    janela_contato = ctk.CTkToplevel()
    janela_contato.title("SMARS - SUPORTE E CONTATO")
    centralizar_janela(janela_contato, 500, 400) 
    janela_contato.attributes("-topmost", True)
    janela_contato.grab_set()
    janela_contato.configure(fg_color="#1a1a1a")

    # Título
    ctk.CTkLabel(janela_contato, text="CENTRAL DE SUPORTE", 
                 font=("Segoe UI", 20, "bold"), text_color="#1f538d").pack(pady=(30, 5))
    
    ctk.CTkLabel(janela_contato, text="BUGS, SUGESTÕES OU DÚVIDAS OPERACIONAIS", 
                 font=("Segoe UI", 12), text_color="gray").pack(pady=(0, 20))

    # Frame Central
    info_frame = ctk.CTkFrame(janela_contato, fg_color="#242424", border_color="#1f538d", border_width=1)
    info_frame.pack(padx=40, pady=(0,0), fill="x")

    email_suporte = "SMARS.contato@outlook.com" # <--- e-mail aqui

    ctk.CTkLabel(info_frame, text="E-MAIL OFICIAL:", 
                 font=("Segoe UI", 11, "bold"), text_color="#5c9ae0").pack(pady=(15, 5))

    # Campo de exibição do e-mail
    display_email = ctk.CTkEntry(info_frame, width=300, height=35, justify="center",
                                 fg_color="#1a1a1a", border_color="#333")
    display_email.insert(0, email_suporte)
    display_email.configure(state="readonly")
    display_email.pack(pady=5)

    # FUNÇÃO PARA COPIAR
    def copiar_email():
        janela_contato.clipboard_clear()
        janela_contato.clipboard_append(email_suporte)
        janela_contato.update() # Garante que o Windows registre a cópia
        
        # Feedback visual temporário no botão
        btn_copiar.configure(text="E-MAIL COPIADO!", fg_color="#27ae60")
        janela_contato.after(2000, lambda: btn_copiar.configure(text="COPIAR ENDEREÇO", fg_color="#333"))

    # Botão de Copiar
    btn_copiar = ctk.CTkButton(info_frame, text="COPIAR ENDEREÇO", font=("Segoe UI", 11, "bold"),
                               fg_color="#333", hover_color="#444", width=150, height=30,
                               command=copiar_email)
    btn_copiar.pack(pady=(10, 20))

    # Rodapé informativo
    ctk.CTkLabel(janela_contato, text="Tempo de resposta de até 3 dias úteis.", 
                 font=("Segoe UI", 15, "italic"), text_color="#555").pack(pady=(15,0))

    # Botão Sair
    ctk.CTkButton(janela_contato, text="VOLTAR", font=("Segoe UI", 13, "bold"),
                  fg_color="#1f538d", hover_color="#14375e", width=180, height=35,
                  command=janela_contato.destroy).pack(side="bottom", pady=(0,25))


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
        command=abrir_historico
    )
    btn_hist.grid(row=1, column=0, padx=15, pady=12) 

     # BOTÃO 3: EXPLICAÇÃO SENTIMENTOS
    btn_conceito = ctk.CTkButton(
        frame_menu2, text="O QUE SÃO SENTIMENTOS?", 
        width=200, height=40,
        font=("Segoe UI", 11, "bold"),
        fg_color="#1f538d",
        hover_color="#14375e",
        command=abrir_conceito
    )
    btn_conceito.grid(row=1, column=1, padx=15, pady=12) 

   
    # BOTÃO 4: EXPLICAÇÃO PROGRAMA (O QUE É O SMARS)
    btn_programa = ctk.CTkButton(
        frame_menu2, text="O QUE É O 'SMARS'?", 
        width=200, height=40,
        font=("Segoe UI", 11, "bold"),
        fg_color="#1f538d",
        hover_color="#14375e",
        command=abrir_sobre_projeto
    )
    btn_programa.grid(row=2, column=0, padx=15, pady=12) 

    # BOTÃO 5: COMO USAR? (COMO USAR O SMARS)
    btn_programa = ctk.CTkButton(
        frame_menu2, text="COMO USAR?", 
        width=200, height=40,
        font=("Segoe UI", 11, "bold"),
        fg_color="#1f538d",
        hover_color="#14375e",
        command=abrir_comousar
    )
    btn_programa.grid(row=2, column=1, padx=15, pady=12) 

 # BOTÃO 6: PRA QUE SERVE? (COMO USAR O SMARS)
    btn_programa = ctk.CTkButton(
        frame_menu2, text="PARA QUE SERVE O 'SMARS'?", 
        width=200, height=40,
        font=("Segoe UI", 11, "bold"),
        fg_color="#1f538d",
        hover_color="#14375e",
        command=abrir_intuito
    )
    btn_programa.grid(row=3, column=0, padx=15, pady=12) 

    # BOTÃO 7: EXPLICAÇÃO ALEXITIMIA (O QUE É ALEXITIMIA)
    btn_alexi = ctk.CTkButton(
        frame_menu2, text="O QUE É ALEXITIMIA?", 
        width=200, height=40,
        font=("Segoe UI", 11, "bold"),
        fg_color="#1f538d",
        hover_color="#14375e",
        command=abrir_explicacao_alexitimia
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
        command=abrir_contato
        
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
