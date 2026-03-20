import customtkinter as ctk
import sqlite3
from tkinter import messagebox

# Configuração de estilo
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SistemaMemoria(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela Principal
        self.title("Dicionário de Memória")
        self.geometry("700x500")

        self.configurar_banco()

        # --- Título ---
        self.label_titulo = ctk.CTkLabel(self, text="Arquivo de Memória e Força Feminina", font=("Roboto", 24, "bold"))
        self.label_titulo.pack(pady=20)

        # --- Botão para Abrir Cadastro ---
        self.btn_abrir_cadastro = ctk.CTkButton(
            self, 
            text="+ Adicionar Nova Personalidade", 
            fg_color="#2E8B57", 
            hover_color="#1E5D3A",
            command=self.abrir_janela_cadastro
        )
        self.btn_abrir_cadastro.pack(pady=10)

        # --- Frame de Filtros ---
        self.frame_filtros = ctk.CTkFrame(self)
        self.frame_filtros.pack(pady=10, padx=20, fill="x")

        self.btn_todas = ctk.CTkButton(self.frame_filtros, text="Ver Todas", width=150, command=self.listar_todas)
        self.btn_todas.grid(row=0, column=0, padx=15, pady=10)

        self.btn_autistas = ctk.CTkButton(self.frame_filtros, text="Autistas", fg_color="#6A5ACD", width=150, command=self.listar_autistas)
        self.btn_autistas.grid(row=0, column=1, padx=15, pady=10)

        self.btn_50mais = ctk.CTkButton(self.frame_filtros, text="Feitos 50+", fg_color="#D2691E", width=150, command=self.listar_50mais)
        self.btn_50mais.grid(row=0, column=2, padx=15, pady=10)

        # --- Área de Exibição ---
        self.texto_resultado = ctk.CTkTextbox(self, width=650, height=250, font=("Consolas", 12))
        self.texto_resultado.pack(pady=20, padx=20)

    def abrir_janela_cadastro(self):
        # Cria uma nova janela (Toplevel)
        self.janela_cad = ctk.CTkToplevel(self)
        self.janela_cad.title("Cadastrar Personalidade")
        self.janela_cad.geometry("450x450")
        self.janela_cad.attributes("-topmost", True) # Mantém a janela na frente

        # Interface dentro da nova janela
        ctk.CTkLabel(self.janela_cad, text="Nova Personalidade", font=("Roboto", 18, "bold")).pack(pady=15)

        self.entry_nome = ctk.CTkEntry(self.janela_cad, placeholder_text="Nome da Mulher", width=350)
        self.entry_nome.pack(pady=5)

        self.entry_area = ctk.CTkEntry(self.janela_cad, placeholder_text="Área (Ciência, Artes...)", width=350)
        self.entry_area.pack(pady=5)

        self.entry_idade = ctk.CTkEntry(self.janela_cad, placeholder_text="Idade do Feito", width=350)
        self.entry_idade.pack(pady=5)

        self.check_autista = ctk.CTkCheckBox(self.janela_cad, text="É Autista?")
        self.check_autista.pack(pady=10)

        self.entry_desc = ctk.CTkTextbox(self.janela_cad, width=350, height=100)
        self.entry_desc.pack(pady=5)
        self.entry_desc.insert("1.0", "Descrição do feito...") # Placeholder manual para Textbox

        self.btn_salvar = ctk.CTkButton(self.janela_cad, text="Salvar no Banco", fg_color="#2E8B57", command=self.salvar_mulher)
        self.btn_salvar.pack(pady=20)

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
        # Pegando texto do CTkTextbox (da linha 1 caractere 0 até o fim)
        desc = self.entry_desc.get("1.0", "end-1c")

        if nome == "" or idade == "":
            messagebox.showwarning("Erro", "Nome e Idade são obrigatórios!")
            return

        try:
            cursor = self.conexao.cursor()
            cursor.execute('''
                INSERT INTO mulheres (nome, area, e_autista, idade_feito_relevante, descricao)
                VALUES (?, ?, ?, ?, ?)
            ''', (nome, area, autista, int(idade), desc))
            self.conexao.commit()
            
            messagebox.showinfo("Sucesso", f"{nome} foi adicionada!")
            self.janela_cad.destroy() # Fecha a janela após salvar
            self.listar_todas() # Atualiza a lista automaticamente
        except ValueError:
            messagebox.showerror("Erro", "A idade deve ser um número!")

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