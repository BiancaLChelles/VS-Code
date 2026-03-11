
import tkinter as tk
from tkinter import simpledialog, messagebox
import re

# Função para normalizar texto (remove acentos, repetições exageradas, etc.)
def normalizar(texto):
    texto = texto.lower().strip()
    # Remove repetições exageradas de letras (ex: "nooooo" -> "no")
    texto = re.sub(r'(.)\1{2,}', r'\1', texto)
    # Remove espaços extras
    texto = re.sub(r'\s+', ' ', texto)
    return texto

# Tradutor de sentimentos baseado nos seus cases
def tradutor_de_sentimentos(sinal_fisico, intensidade):
    s = normalizar(sinal_fisico)

    if s in ["nó na garganta", "vontade de chorar", "choro preso"]:
        if intensidade >= 7:
            return ("Tristeza Profunda ou Vontade de chorar",
                    "O sistema precisa de liberação de pressão. Procure um lugar seguro para chorar.")
        else:
            return ("Angústia leve ou peso por algo que foi ou não dito",
                    "Tente escrever o que aconteceu no dia de hoje, tente identificar algum possivel gatilho.")

    elif s in ["peito apertado", "aperto no peito", "coração apertado"]:
        if intensidade >= 7:
            return ("Desespero / Pãnico",
                    "O sistema tem que voltar ao funcionamento básico urgentemente. Procure um lugar seguro. Converse com alguém.")
        else:
            return ("Ansiedade ou Sobrecarga",
                    "Reduza os estímulos sensoriais. Busque silêncio e o escuro. \n Ative o modo de respiração profunda e retorne ao momento presente.")

    elif s in ["mãos agitadas", "flappin hands", "mãos tremendo"]:
        if intensidade >= 5:
            return ("Agitação Sensorial ou Estresse",
                    "Use um objeto de regulação (fidget toy) ou faça alguma atividade que estimule suas mãos.")
        else:
            return ("Empolgação / Alegria (Stimming)",
                    "O seu sistema está em um pico de energia positiva. Aproveite esse momento! ISSO É BOM!")

    elif s in ["olhar fixo", "olhar desligando", "olhar travado", "olhar morto", "olhar pesado", "olhar pesando"]:
        if intensidade >= 6:
            return ("Dissociação ou Shutdown iminente",
                    "CRITICO: O sistema está tentando desligar para se proteger. Reduza IMEDIATAMENTE as luzes e sons. Não tente processar informações agora.")
        else:
            return ("Devaneio ou Processamento em segundo plano",
                    "Seu cérebro está organizando uma alta quantidade de dados. Deixe esse processamento fluir. Se possivel reduza os estimulos, busque voltar para o momemto presente.")

    elif s in ["respiração rápida", "respiração acelerada", "respiração forte"]:
        if intensidade >= 7:
            return ("Sobrecarga Sensorial ou Crise de Ansiedade",
                    "O sistema está em modo 'Luta ou Fuga'. Foque apenas em respirar lentamente (soltar o ar (e os pensamentos) é mais importante que puxar agora).")
        else:
            return ("Inquietude, Nervosismo ou Impaciência",
                    "Seu processamento está acelerado. Tente levantar, se alongar ou caminhar para gastar um pouco dessa energia acumulada.")

    elif s in ["sensibilidade ao som", "sons muito altos", "sons incomodando"]:
        if intensidade >= 6:
            return ("Irritabilidade ou Pré-Meltdown",
                    "Sinal de que uma crise sensorial está proxima. Ative isolamento acústico (fones) ou mude para uma 'sala silenciosa' imediatamente.")
        else:
            return ("Foco em ruídos",
                    "Seu sistema de filtragem de ruidos está baixo. Tente colocar um som ambiente, uma musica de conforto ou um ruído branco para mascarar um pouco dos sons externos.")

    elif s in ["pernas agitadas", "pernas tremendo"]:
        if intensidade >= 5:
            return ("Necessidade de autorregulação (Stimming)",
                    "Energia acumulada detectada. Deixe os movimentos acontecerem, a liberação de energia ajuda a manter o sistema estável.")
        else:
            return ("Tédio ou Desatenção",
                    "O sistema precisa de novos estímulos. Troque de tarefa, busque um novo interesse, sua mente está precisando ser utilzada.")

    elif s in ["mãos geladas", "mãos frias"]:
        if intensidade >= 6:
            return ("Medo ou Ansiedade Social",
                    "O foco está no funcionamento vital agora. Aqueça as mãos com água morna, busque conforto, e diminua os estimulos. Vamos enviar um sinal de 'segurança' para o cérebro.")
        else:
            return ("Desconforto Ambiental",
                    "Verifique a temperatura do local. Às vezes o bug é físico, não emocional. Você deve estar com frio. Vista um casaco.")

    elif s in ["dificuldade em falar", "dificuldade em formular frases", "fala lenta", "fala travada", "dissociação"]:
        if intensidade >= 6:
            return ("Esgotamento Verbal (NÃO VERBAL)",
                    "O sistema de linguagem está offline para previvinir danos com a sobrecarga de energia. Use gestos, textos ou apenas descanse. Nem tudo tem que ser comunicado agora.")
        else:
            return ("Cansaço Mental",
                    "Processamento de saída lento. Não se force a falar frases complexas agora. Respostas curtas também são aceitáveis.")

    elif s in ["pensamento acelerado", "mente com vários cenários ao mesmo tempo", "mente acelerada", "pensamentos caóticos", "pensamentos acelerados", "mente um caos"]:
        if intensidade >= 8:
            return ("Crise Ansiosa ou Loop de TAG",
                    "O processador está superaquecendo com simulações do futuro. Volte ao momento presente.")
        else:
            return ("Ansiedade Antecipatória",
                    "Muitas abas estão abertas mentalmente. Tente minimizar o funcionamento para que o sistema possa se regular.")

    elif s in ["pensamento em looping", "ruminando o passado", "ruminação", "mente presa", "mente em looping"]:
        if intensidade >= 7:
            return ("Ruminação (Bug de Autocrítica)",
                    "O sistema travou em um erro do passado. Lembre-se: código executado, não pode ser editado. Reprograme, recomece.")
        else:
            return ("Análise de Padrões Sociais",
                    "Você está tentando entender uma interação. Dê um tempo limite para isso, analise, processe e depois faça uma tarefa manual para sair deste foco.")

    return ("uma Emoção não reconhecida",
            "Beba água, busque silêncio e faça um scan corporal da cabeça aos pés. \n VAMOS ENTENDER ISSO! CALMA!")

# Interface gráfica
def iniciar_app():
    root = tk.Tk()
    root.withdraw()

    sabe_emocao = messagebox.askyesno("Identificação de Emoção",
                                      "Você sabe o que está sentindo agora?")

    if sabe_emocao:
        emocao = simpledialog.askstring("Emoção", "Digite o nome da emoção:")
        messagebox.showinfo("Manejo", f"Você está sentindo: {emocao}\n\n"
                                      f"Lembre-se que esse sentimento também irá passar, assim como todos os outros.")
    else:
        sintoma = simpledialog.askstring("Sintomas", "Digite seus sintomas físicos:")
        intensidade = simpledialog.askinteger("Intensidade", "De 1 a 10, qual a intensidade?")
        emocao, instrucao = tradutor_de_sentimentos(sintoma, intensidade)
        messagebox.showinfo("Resultado",
                            f"=== ANALISANDO SINAIS CORPORAIS ===\n\n"
                            f"EMOÇÃO: Neste momento você está sentindo {emocao}\n"
                            f"Lembre-se que esse sentimento também irá passar, assim como todos os outros.\n\n"
                            f"O QUE FAZER?: {instrucao}")

    root.destroy()

if __name__ == "__main__":
    iniciar_app()
