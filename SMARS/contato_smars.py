


import customtkinter as ctk # Importa a biblioteca para o visual moderno e Modo Escuro
from datetime import datetime # Importa funções para ler a hora atual do seu computador
import varredura_fisica # Importa o módulo que traduz sensações do corpo
import dicionario # Importa o módulo com o banco de dados de sentimentos
import sqlite3
from datetime import datetime, timedelta
import motor_logico  # Importa o arquivo de manejo

import textos_smars
import teste_manejo
import historico_smars


def centralizar_janela(janela, largura, altura):
    # Pega a largura e altura da tela do computador
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Calcula a posição X e Y para o centro
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)

    # Define a geometria: "Largura x Altura + PosX + PosY"
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")


def abrir_contato():
    janela_contato = ctk.CTkToplevel()
    janela_contato.title("SMARS - SUPORTE E CONTATO")
    centralizar_janela(janela_contato, 500, 400) 
    janela_contato.attributes("-topmost", True)
    janela_contato.grab_set()
    janela_contato.configure(fg_color="#1a1a1a")

    # Título
    ctk.CTkLabel(janela_contato, text="CENTRAL DE SUPORTE", 
                 font=("Segoe UI", 22, "bold"), text_color="#1f538d").pack(pady=(30, 5))
    
    ctk.CTkLabel(janela_contato, text="EM CASO DE BUGS, SUGESTÕES, NOVOS CASOS OU DÚVIDAS.", 
                 font=("Segoe UI", 13), text_color="#82abda").pack(pady=(0, 20))

    # Frame Central
    info_frame = ctk.CTkFrame(janela_contato, fg_color="#242424", border_color="#1f538d", border_width=1)
    info_frame.pack(padx=40, pady=(0,0), fill="x")

    email_suporte = "SMARS.contato@outlook.com" # <--- e-mail aqui

    ctk.CTkLabel(info_frame, text="ENTRE EM CONTATO CONOSCO", 
                 font=("Segoe UI", 14, "bold"), text_color="#5c9ae0").pack(pady=(15, 5))

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
                 font=("Segoe UI", 15, "italic"), text_color="#82abda").pack(pady=(15,0))

    # Botão Sair
    ctk.CTkButton(janela_contato, text="VOLTAR", font=("Segoe UI", 13, "bold"),
                  fg_color="#1f538d", hover_color="#14375e", width=180, height=35,
                  command=janela_contato.destroy).pack(side="bottom", pady=(0,25))
