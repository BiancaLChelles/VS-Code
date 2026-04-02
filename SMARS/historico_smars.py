
import customtkinter as ctk # Importa a biblioteca para o visual moderno e Modo Escuro
from datetime import datetime # Importa funções para ler a hora atual do seu computador
import varredura_fisica # Importa o seu módulo que traduz sensações do corpo
import dicionario # Importa o seu módulo com o banco de dados de sentimentos
import sqlite3
from datetime import datetime, timedelta
import motor_logico  # Importa o arquivo de manejo

import textos_smars
import teste_manejo


def centralizar_janela(janela, largura, altura):
    # Pega a largura e altura da tela do seu computador
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Calcula a posição X e Y para o centro
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)

    # Define a geometria: "Largura x Altura + PosX + PosY"
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")


    # --- CONFIGURAÇÃO VISUAL DO SISTEMA ---
ctk.set_appearance_mode("dark") # Define que o programa rodará sempre em Modo Escuro
ctk.set_default_color_theme("blue") # Define a cor azul como padrão para botões e detalhes

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

import os
print(f"📍 O Python está trabalhando na pasta: {os.getcwd()}")
print(f"📂 O arquivo do banco deveria estar em: {os.path.abspath('smars_logs.db')}")

# --- 1. FUNÇÃO QUE APENAS BUSCA NO BANCO E DESENHA OS CARDS ---
def carregar_logs(container_cards, janela=None, filtro_dias=None):
    # Limpeza visual do container
    for widget in container_cards.winfo_children():
        widget.destroy()

    try:
        
        import sqlite3
        from pathlib import Path

        BASE_DIR = Path(__file__).resolve().parent
        DB_PATH = BASE_DIR / "smars_logs.db"

        teste_manejo.configurar_banco
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row

        cursor = conn.cursor()
        cursor.execute("PRAGMA table_info(logs)")
        print(cursor.fetchall())
        
        if filtro_dias is not None:
         query = "SELECT id, data_hora, sentimento, intensidade, identifica, manejo, entrada_bruta FROM logs WHERE data_hora >= datetime('now', 'localtime', ?) ORDER BY id DESC"
         cursor.execute(query, (f"-{filtro_dias} days",))
        else:
            cursor.execute("SELECT id, data_hora, sentimento, intensidade, identifica, manejo, entrada_bruta FROM logs ORDER BY id DESC")
            
        rows = cursor.fetchall()
        
        if not rows:
            ctk.CTkLabel(container_cards, text=">>> NENHUM LOG REGISTRADO.", font=("Segoe UI", 14, "italic"), text_color="gray").pack(pady=50)
        else:
           for row in rows:
            # 1. CRIAR O CARD
            # O master deve ser o container_cards. 
            card = ctk.CTkFrame(container_cards, fg_color="#2b2b2b", corner_radius=10, border_width=1, border_color="#3d3d3d")
            
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
            if row ["identifica"] == 1:
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
                command=lambda r=row: mostrar_detalhes(r["data_hora"], r["sentimento"], r["intensidade"], r["manejo"], r["entrada_bruta"], master_window=janela)
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


def mostrar_detalhes(data_banco, sentimento, nivel, manejo_texto, entrada_usuario="Não registrado", master_window=None):
    # Janela principal
    detalhes = ctk.CTkToplevel(master_window)
    detalhes.title(f"HISTÓRICO SMARS - {sentimento.upper()}")
    centralizar_janela(detalhes, 500, 600) # Aumentei um pouco a altura para caber o seu texto
    detalhes.attributes("-topmost", True)
    detalhes.configure(fg_color="#121212") # Fundo grafite escuro (Padrão SMARS)
    detalhes.grab_set()

    # --- TÍTULO PRINCIPAL ---
    ctk.CTkLabel(detalhes, text=sentimento.upper(), 
                 font=("Segoe UI", 28, "bold"), text_color="#307acf").pack(pady=(25, 5))

    # --- STATUS (Nível e Data) ---
    nivel_limpo = str(nivel).split('/')[0]
    try:
        valor_nivel = int(nivel_limpo)
    except:
        valor_nivel = 5
    cor_nivel = "#2ecc71" if valor_nivel <= 3 else "#f1c40f" if valor_nivel <= 7 else "#e74c3c"
    
    # Formatação da data
    try:
        data_formatada = datetime.strptime(data_banco, "%Y-%m-%d %H:%M:%S").strftime("%d/%m/%Y %H:%M")
    except:
        data_formatada = data_banco

    ctk.CTkLabel(detalhes, text=f"Intensidade: {nivel_limpo}/10  •  {data_formatada}", 
                 font=("Segoe UI", 12, "bold"), text_color=cor_nivel).pack(pady=(0, 20))

    # --- SEÇÃO 1: O SEU RELATO (VARREDURA) ---
    # Criamos um frame com borda cinza para o seu texto
    frame_relato = ctk.CTkFrame(detalhes, fg_color="#1a1a1a", border_color="#333333", border_width=1, corner_radius=12)
    frame_relato.pack(fill="x", padx=30, pady=10)

    ctk.CTkLabel(frame_relato, text="VOCÊ ESCREVEU:", 
                 font=("Segoe UI", 10, "bold"), text_color="#1f538d").pack(anchor="w", padx=15, pady=(10, 0))

    ctk.CTkLabel(frame_relato, text=f'"{entrada_usuario}"', 
                 font=("Segoe UI", 13, "italic"), text_color="#bbbbbb", wraplength=400, justify="left").pack(anchor="w", padx=15, pady=(5, 15))

    # --- SEÇÃO 2: MANEJO DO SISTEMA ---
    # Tratamento do texto para exibição (Limpa os parênteses e aspas do banco e formata com bullets)
    conteudo_limpo = str(manejo_texto).strip("()").replace("'", "").replace('"', '')
    
    # Caixa de texto com borda colorida baseada no nível
    txt = ctk.CTkTextbox(detalhes, width=440, height=250, font=("Segoe UI", 15),
                         fg_color="#1a1a1a", border_color=cor_nivel, border_width=2, corner_radius=15, wrap="word")
    txt.pack(pady=15, padx=30)
    
    txt.insert("0.0", f"ANÁLISE E MANEJO:\n\n {conteudo_limpo}")
    txt.configure(state="disabled")

    # --- BOTÃO CONCLUIR ---
    ctk.CTkButton(
        detalhes, 
        text="VOLTAR", 
        font=("Segoe UI", 14, "bold"),
        fg_color="#1f538d", 
        hover_color="#14375e", 
        width=200, height=50,
        corner_radius=10,
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