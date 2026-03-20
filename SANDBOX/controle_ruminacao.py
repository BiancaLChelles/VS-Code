import customtkinter as ctk
from datetime import datetime
import json
import os

# Configurações de Interface
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class ProtocoloSandbox(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Protocolo Sandbox")
        self.geometry("500x450")
        
        # Novo nome do ficheiro de base de dados
        self.history_file = "registo_ruminacoes.json"
        self.active_timer = None
        
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.menu_principal()

    def clear_screen(self):
        for widget in self.winfo_children():
            widget.destroy()

    def menu_principal(self):
        self.clear_screen()
        
        lbl_title = ctk.CTkLabel(self, text="PROTOCOLO SANDBOX", font=("Consolas", 22, "bold"))
        lbl_title.pack(pady=(40, 10))
        
        # wraplength define em quantos pixels o texto deve quebrar a linha
        lbl_subtitle = ctk.CTkLabel(self, 
                                    text="AMBIENTE DE TESTE PARA O DESENVOLVIMENTO DE CONTROLE SOBRE A RUMINAÇÃO.", 
                                    font=("Consolas", 12), 
                                    text_color="gray",
                                    wraplength=500) # Ajusta o texto à largura da janela
        lbl_subtitle.pack(pady=(0, 30))

        # Definindo uma largura padrão (width) para todos os botões ficarem iguais
        largura_padrao = 280

        # Botão: Novo Registo
        btn_new = ctk.CTkButton(self, text="Registar Nova Ruminação", 
                                 command=self.janela_ruminacao,
                                 fg_color="#1f538d", hover_color="#1e4f86", 
                                 height=40, width=largura_padrao)
        btn_new.pack(pady=10)

        # Botão: Histórico
        btn_history = ctk.CTkButton(self, text="Consultar Histórico de Registo", 
                                     command=self.mostrar_historico,
                                     fg_color="#1f538d", hover_color="#1e4f86", 
                                     height=40, width=largura_padrao)
        btn_history.pack(pady=10)

        # Botão: Timer de Pensamento (Sem escrita)
        btn_pure_timer = ctk.CTkButton(self, text="Ativar Timer de Ruminação Pura", 
                                        command=self.timer_apenas_pensar,
                                        fg_color="#2c3e50", hover_color="#183755", 
                                        height=40, width=largura_padrao)
        btn_pure_timer.pack(pady=10)

        lbl_footer = ctk.CTkLabel(self, text='"Fazer pouco aos poucos é também fazer muito."', 
                                   font=("Consolas", 13, "italic"), text_color="#555555")
        lbl_footer.pack(side="bottom", pady=20)

    # --- JANELA DE REGISTO COM TIMER DE 15 MINUTOS ---
    def janela_ruminacao(self):
        self.clear_screen()
        self.tempo_restante = 900  # 15 minutos
        
        ctk.CTkLabel(self, text="MODO DEBUG: ANÁLISE DE INTERAÇÃO", font=("Consolas", 16, "bold")).pack(pady=15)
        
        self.entry_titulo = ctk.CTkEntry(self, placeholder_text="Título da Interação (Ex: Reunião/Mensagem)", width=450)
        self.entry_titulo.pack(pady=5)

        self.lbl_timer = ctk.CTkLabel(self, text="15:00", font=("Consolas", 40, "bold"), text_color="#3b8ed0")
        self.lbl_timer.pack(pady=10)

        self.txt_input = ctk.CTkTextbox(self, width=500, height=200, font=("Consolas", 12))
        self.txt_input.pack(pady=10)
        self.txt_input.insert("0.0", "Descreva o bug, o pensamento ou a sensação sobre a interação aqui...")

        self.btn_gravar = ctk.CTkButton(self, text="Concluir e Gravar", command=self.gravar_dados)
        self.btn_gravar.pack(pady=15)

        self.executar_contagem()

    def executar_contagem(self):
        if self.tempo_restante > 0:
            self.tempo_restante -= 1
            mins, secs = divmod(self.tempo_restante, 60)
            self.lbl_timer.configure(text=f"{mins:02d}:{secs:02d}")
            self.active_timer = self.after(1000, self.executar_contagem)
        else:
            # Bloqueio de segurança pós-timeout
            self.txt_input.configure(state="disabled")
            self.lbl_timer.configure(text="TEMPO FINALIZADO", text_color="#e74c3c")
            msg_bloqueio = ctk.CTkLabel(self, text="SESSÃO DE DEBUG ENCERRADA: O tempo de (re)processamento esgotou.", text_color="#e67e22")
            msg_bloqueio.pack()

    def gravar_dados(self):
        novo_registo = {
            "timestamp": datetime.now().strftime("%d/%m/%Y %H:%M"),
            "titulo": self.entry_titulo.get(),
            "conteudo": self.txt_input.get("0.0", "end").strip()
        }
        
        dados = []
        if os.path.exists(self.history_file):
            with open(self.history_file, "r", encoding="utf-8") as f:
                try:
                    dados = json.load(f)
                except json.JSONDecodeError:
                    dados = []
        
        dados.append(novo_registo)
        with open(self.history_file, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
            
        if self.active_timer:
            self.after_cancel(self.active_timer)
        self.menu_principal()

    # --- TIMER APENAS PARA PENSAR (SEM CAIXA DE TEXTO) ---
    def timer_apenas_pensar(self):
        self.clear_screen()
        self.tempo_restante = 900
        
        ctk.CTkLabel(self, text="DEBUG COGNITIVO", font=("Consolas", 18, "bold")).pack(pady=50)
        self.lbl_timer = ctk.CTkLabel(self, text="15:00", font=("Consolas", 70, "bold"), text_color="#3b8ed0")
        self.lbl_timer.pack(pady=20)
        
        ctk.CTkLabel(self, text="Observe os pensamentos, analise e permita-se ficar sem registar no sistema.", font=("Consolas", 12), text_color="gray").pack()
        
        btn_voltar = ctk.CTkButton(self, text="Abortar e Voltar ao Menu", command=self.menu_principal)
        btn_voltar.pack(pady=50)
        
        self.executar_contagem_pura()

    def executar_contagem_pura(self):
        if self.tempo_restante > 0:
            self.tempo_restante -= 1
            mins, secs = divmod(self.tempo_restante, 60)
            self.lbl_timer.configure(text=f"{mins:02d}:{secs:02d}")
            self.active_timer = self.after(1000, self.executar_contagem_pura)
        else:
            self.lbl_timer.configure(text="FIM", text_color="#e74c3c")

    # --- HISTÓRICO DE REGISTOS ---
    def mostrar_historico(self):
        self.clear_screen()
        ctk.CTkLabel(self, text="HISTÓRICO DE RUMINAÇÕES", font=("Consolas", 18, "bold")).pack(pady=20)

        frame_scroll = ctk.CTkScrollableFrame(self, width=520, height=380)
        frame_scroll.pack(pady=10, padx=10)

        if os.path.exists(self.history_file):
            with open(self.history_file, "r", encoding="utf-8") as f:
                try:
                    registos = json.load(f)
                except:
                    registos = []
            
            for reg in reversed(registos):
                item = ctk.CTkFrame(frame_scroll)
                item.pack(fill="x", pady=5, padx=5)
                
                info = f"{reg['timestamp']} | {reg['titulo']}"
                lbl = ctk.CTkLabel(item, text=info, font=("Consolas", 11))
                lbl.pack(side="left", padx=10)
                
                btn_ler = ctk.CTkButton(item, text="Detalhes", width=80,
                                         command=lambda r=reg: self.ver_detalhes(r))
                btn_ler.pack(side="right", padx=5)
        else:
            ctk.CTkLabel(frame_scroll, text="Nenhum registo encontrado.").pack(pady=20)

        ctk.CTkButton(self, text="Voltar ao Menu", command=self.menu_principal).pack(pady=15)

    def ver_detalhes(self, reg):
        janela_detalhe = ctk.CTkToplevel(self)
        janela_detalhe.title(f"Visualização: {reg['titulo']}")
        janela_detalhe.geometry("450x450")
        janela_detalhe.attributes("-topmost", True)
        
        ctk.CTkLabel(janela_detalhe, text="EDITAR TÍTULO:", font=("Consolas", 10, "bold")).pack(pady=(15,0))
        entry_edit_titulo = ctk.CTkEntry(janela_detalhe, width=350)
        entry_edit_titulo.insert(0, reg['titulo'])
        entry_edit_titulo.pack(pady=5)
        
        ctk.CTkLabel(janela_detalhe, text="CONTEÚDO (BLOQUEADO):", font=("Consolas", 10, "bold")).pack(pady=(15,0))
        txt_view = ctk.CTkTextbox(janela_detalhe, width=400, height=220, font=("Consolas", 11))
        txt_view.insert("0.0", reg['conteudo'])
        txt_view.configure(state="disabled") # Bloqueado conforme o protocolo
        txt_view.pack(pady=10)
        
        lbl_nota = ctk.CTkLabel(janela_detalhe, text="O conteúdo não pode ser reanalisado após o encerramento do tempo de processamento.", 
                                 font=("Consolas", 9), text_color="orange")
        lbl_nota.pack()

if __name__ == "__main__":
    app = ProtocoloSandbox()
    app.mainloop()