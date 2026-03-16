import customtkinter as ctk
import sqlite3
from tkinter import messagebox

# Configuração de estilo
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SistemaMemoria(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela
        self.title("Dicionário de Memória: Mulheres Históricas")
        self.geometry("700x750")

        # Inicializa o Banco de Dados internamente
        self.configurar_banco()

        # --- Título ---
        self.label_titulo = ctk.CTkLabel(self, text="Arquivo de Memória e Força Feminina", font=("Roboto", 24, "bold"))
        self.label_titulo.pack(pady=15)

        # --- Frame de Cadastro (Entradas de Dados) ---
        self.frame_cadastro = ctk.CTkFrame(self)
        self.frame_cadastro.pack(pady=10, padx=20, fill="x")

        self.label_cad = ctk.CTkLabel(self.frame_cadastro, text="Adicionar Nova Personalidade", font=("Roboto", 16, "bold"))
        self.label_cad.grid(row=0, column=0, columnspan=2, pady=10)

        self.entry_nome = ctk.CTkEntry(self.frame_cadastro, placeholder_text="Nome da Mulher", width=300)
        self.entry_nome.grid(row=1, column=0, padx=10, pady=5)

        self.entry_area = ctk.CTkEntry(self.frame_cadastro, placeholder_text="Área (Ciência, Artes...)", width=300)
        self.entry_area.grid(row=1, column=1, padx=10, pady=5)

        self.check_autista = ctk.CTkCheckBox(self.frame_cadastro, text="É Autista?")
        self.check_autista.grid(row=2, column=0, pady=5)

        self.entry_idade = ctk.CTkEntry(self.frame_cadastro, placeholder_text="Idade do Feito", width=140)
        self.entry_idade.grid(row=2, column=1, sticky="w", padx=10, pady=5)

        self.entry_desc = ctk.CTkEntry(self.frame_cadastro, placeholder_text="Breve descrição do feito", width=620)
        self.entry_desc.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

        self.btn_salvar = ctk.CTkButton(self.frame_cadastro, text="Salvar no Banco", fg_color="#2E8B57", command=self.salvar_mulher)
        self.btn_salvar.grid(row=4, column=0, columnspan=2, pady=10)

        # --- Frame de Filtros (Botões de Busca) ---
        self.frame_filtros = ctk.CTkFrame(self)
        self.frame_filtros.pack(pady=10, padx=20, fill="x")

        self.btn_todas = ctk.CTkButton(self.frame_filtros, text="Ver Todas", width=150, command=self.listar_todas)
        self.btn_todas.grid(row=0, column=0, padx=10, pady=10)

        self.btn_autistas = ctk.CTkButton(self.frame_filtros, text="Autistas", fg_color="#6A5ACD", width=150, command=self.listar_autistas)
        self.btn_autistas.grid(row=0, column=1, padx=10, pady=10)

        self.btn_50mais = ctk.CTkButton(self.frame_filtros, text="Feitos 50+", fg_color="#D2691E", width=150, command=self.listar_50mais)
        self.btn_50mais.grid(row=0, column=2, padx=10, pady=10)

        # --- Área de Exibição ---
        self.texto_resultado = ctk.CTkTextbox(self, width=650, height=250, font=("Consolas", 12))
        self.texto_resultado.pack(pady=10, padx=20)

    def configurar_banco(self):
        self.conexao = sqlite3.connect("memoria_mulheres.db")
        cursor = self.conexao.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS mulheres (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                area TEXT,
                e_autista BOOLEAN,
                idade_feito_relevante INTEGER,
                descricao TEXT
            )
        ''')
        self.conexao.commit()

    def salvar_mulher(self):
        nome = self.entry_nome.get()
        area = self.entry_area.get()
        autista = 1 if self.check_autista.get() else 0
        idade = self.entry_idade.get()
        desc = self.entry_desc.get()

        if nome == "" or idade == "":
            messagebox.showwarning("Erro", "Nome e Idade são obrigatórios!")
            return

        cursor = self.conexao.cursor()
        cursor.execute('''
            INSERT INTO mulheres (nome, area, e_autista, idade_feito_relevante, descricao)
            VALUES (?, ?, ?, ?, ?)
        ''', (nome, area, autista, int(idade), desc))
        self.conexao.commit()
        
        messagebox.showinfo("Sucesso", f"{nome} foi adicionada com sucesso!")
        self.limpar_campos()

    def limpar_campos(self):
        self.entry_nome.delete(0, 'end')
        self.entry_area.delete(0, 'end')
        self.entry_idade.delete(0, 'end')
        self.entry_desc.delete(0, 'end')
        self.check_autista.deselect()

    def exibir_na_tela(self, mulheres):
        self.texto_resultado.delete("1.0", "end")
        if not mulheres:
            self.texto_resultado.insert("end", "Nenhum registro encontrado.")
            return

        for m in mulheres:
            aut = "Sim" if m[3] else "Não"
            info = f"NOME: {m[1].upper()}\nÁREA: {m[2]} | AUTISTA: {aut} | IDADE: {m[4]}\nFEITO: {m[5]}\n"
            info += "="*60 + "\n"
            self.texto_resultado.insert("end", info)

    def listar_todas(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM mulheres")
        self.exibir_na_tela(cursor.fetchall())

    def listar_autistas(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM mulheres WHERE e_autista = 1")
        self.exibir_na_tela(cursor.fetchall())

    def listar_50mais(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM mulheres WHERE idade_feito_relevante >= 50")
        self.exibir_na_tela(cursor.fetchall())

if __name__ == "__main__":
    app = SistemaMemoria()
    app.mainloop()