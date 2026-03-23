import customtkinter as ctk         
from tkinter import messagebox
import time                

import customtkinter as ctk
import time

# Configuração de aparência do sistema
ctk.set_appearance_mode("dark")  # Opções: "dark", "light", "system"
ctk.set_default_color_theme("blue") # Opções: "blue", "green", "dark-blue"

def disparar_alerta():
    """Cria uma janela modernizada que exige atenção para o manejo de hiperfoco."""
    
    # Criamos a janela principal do alerta
    alerta = ctk.CTk()
    alerta.title("Manutenção de Hardware Humano")
    
    # Define o tamanho e centraliza (aproximadamente)
    alerta.geometry("450x400")
    alerta.attributes("-topmost", True) # Mantém na frente de tudo
    
    # Texto do cabeçalho
    titulo = ctk.CTkLabel(
        alerta, 
        text=" LEMBRETE DE MANEJO DE HIPERFOCO", 
        font=ctk.CTkFont(size=16, weight="bold")
    )
    titulo.pack(pady=(20, 10))

   # Subtítulo de Status
    status_label = ctk.CTkLabel(alerta, text="Status: 2 horas de atividade ininterruptas foram detectadas.", text_color="orange")
    status_label.pack(pady=(0, 20))


    # Frame para organizar os Checkboxes (Checklist)
    frame_checklist = ctk.CTkFrame(alerta, fg_color="transparent")
    frame_checklist.pack(pady=10, padx=40, fill="x")

    # Variáveis para rastrear os checks (0 = desmarcado, 1 = marcado)
    check_agua_var = ctk.IntVar(value=0)
    check_alongar_var = ctk.IntVar(value=0)
    check_pausa_var = ctk.IntVar(value=0)

    def verificar_protocolo():
        #Habilita o botão apenas se todos os checks forem concluídos.
        
        if check_agua_var.get() == 1 and check_alongar_var.get() == 1 and check_pausa_var.get() == 1:
            btn_confirmar.configure(state="normal", fg_color="#2c82c9")
        else:
            btn_confirmar.configure(state="disabled", fg_color="#333333")

    # Itens do Checklist
    check_agua = ctk.CTkCheckBox(frame_checklist, text="Beber água.", 
                                 variable=check_agua_var, command=verificar_protocolo,
                                 width=200,          # Largura da área do componente
                                height=30,          # Altura da área do componente
                                checkbox_width=20,  # Tamanho do quadradinho do check
                                checkbox_height=20,  # Tamanho do quadradinho do check
                                )
    check_agua.pack(pady=6, anchor="w")

    check_alongar = ctk.CTkCheckBox(frame_checklist, text="Alongar pescoço, costas e pernas.", 
                                    variable=check_alongar_var, command=verificar_protocolo,
                                    width=200,          # Largura da área do componente
                                    height=30,          # Altura da área do componente
                                    checkbox_width=20,  # Tamanho do quadradinho do check
                                    checkbox_height=20  # Tamanho do quadradinho do check
                                    )
    check_alongar.pack(pady=6, anchor="w")

    check_pausa = ctk.CTkCheckBox(frame_checklist, text="Pausa de 5 minutos", 
                                  variable=check_pausa_var, command=verificar_protocolo,
                                  width=200,          # Largura da área do componente
                                  height=30,          # Altura da área do componente
                                  checkbox_width=20,  # Tamanho do quadradinho do check
                                  checkbox_height=20  # Tamanho do quadradinho do check
                                  )
    check_pausa.pack(pady=6, anchor="w")


    # Frase de fechamento com fonte menor/itálico
    frase_final = ctk.CTkLabel(
    alerta, 
    text="\"Preservar a integridade do hardware é garantir a eficiência do processamento.\"",
    font=ctk.CTkFont(size=11, slant="italic"),
    text_color="#2c82c9",
)
    frase_final.pack(pady=(0, 10))

    
    # Botão estilizado
    btn_confirmar = ctk.CTkButton (
        alerta, 
        text="Manutenção Concluída", 
        command= alerta.destroy,  
        state= "disabled",
        width=200,          # Largura do botão
        height=50,          # Altura do botão (deixa ele mais imponente)
        corner_radius=10,   # Arredondamento dos cantos
        fg_color="#2c82c9",
        hover_color="#1e5a8a" 
        )
    btn_confirmar.pack(pady=30)

    alerta.mainloop()

# --- LOOP DE MONITORAMENTO ---
print("Monitor de hiperfoco ativo e operando em segundo plano...")

while True:
    # 2 horas = 7200 segundos
    tempo_de_espera = 2
    
    time.sleep(tempo_de_espera)
    disparar_alerta()