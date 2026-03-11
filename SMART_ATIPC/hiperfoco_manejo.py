
import tkinter as tk         # Importa a biblioteca de janelas (a interface gráfica)
from tkinter import messagebox # Importa especificamente a caixa de mensagem
import time                  # Importa o controle de tempo do computador

def disparar_alerta():
    """Esta função cria a janela que 'trava' sua atenção."""
    root = tk.Tk()           # Cria a base da janela
    root.withdraw()          # Esconde a janela principal (queremos só o alerta)
    root.attributes("-topmost", True) # Força o alerta a ficar na frente de tudo
    
    # Texto que aparecerá para você
    mensagem = (
        " LEMBRETE DE MANEJO DE HIPERFOCO \n\n"
        "Status: 2 horas interruptas de atividade foram detectadas.\n"
        "Ação necessária: Execute a manutenção do (seu) hardware.\n\n"
        "• Beba água\n"
        "• Alongue o pescoço, as pernas e as costas\n"
        "• Se dê uma pausa de 5 minutos\n\n"
        "Clique em OK para confirmar que a manutenção foi concluída."
    )
    
    # Cria a caixa que exige o clique (showinfo)
    messagebox.showinfo("Lembrete de Autocuidado", mensagem)
    
    root.destroy() # Fecha tudo após o clique para liberar a memória

# --- LOOP DE MONITORAMENTO ---
print("Sistema de monitoramento de pausas iniciado...")

while True:
    # O tempo em Python é contado em segundos.
    # 2 horas = 2 * 60 minutos * 60 segundos = 7200 segundos.
   
    tempo_de_espera = 7200
    
    time.sleep(tempo_de_espera) # O programa "dorme" e não gasta processador aqui
    disparar_alerta()           # Quando acorda, executa a função do alerta
