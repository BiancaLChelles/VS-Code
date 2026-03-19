# Importamos a função de busca do seu motor
from motor_sentimentos import identificar_sinal, carregar_banco
import tkinter as tk
from tkinter import messagebox

def rodar_exemplo():
    # 1. Vamos simular um sinal que veio do seu corpo
    sinal_detectado = "peito apertado"
    
    # 2. Chamamos o seu motor para identificar o que é isso
    resultado = identificar_sinal(sinal_detectado)
    
    # 3. Agora o seu novo projeto toma uma decisão baseada no dicionário
    if resultado == "ansiedade":
        messagebox.showinfo("Exoesqueleto", f"Detectei {sinal_detectado}. Isso indica ANSIEDADE. \nProtocolo: Tente respirar fundo 3 vezes.")
    elif resultado == "fome":
        messagebox.showinfo("Exoesqueleto", "Você precisa comer algo agora.")
    else:
        messagebox.showwarning("Aviso", "Sinal detectado, mas não tem protocolo de manejo ainda.")

if __name__ == "__main__":
    rodar_exemplo()