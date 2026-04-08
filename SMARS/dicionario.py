import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os
import unicodedata
import re
import customtkinter as ctk
from tkinter import messagebox

ARQUIVO_MEMORIA = "dicionario_sensacoes.json"

def normalizar(texto):
    if not texto: return ""
    texto = "".join(c for c in unicodedata.normalize('NFD', str(texto).lower().strip()) if unicodedata.category(c) != 'Mn')
    return re.sub(r'(.)\1{2,}', r'\1', texto)

def carregar_banco():
    if os.path.exists(ARQUIVO_MEMORIA):
        try:
            with open(ARQUIVO_MEMORIA, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            pass
    
    # Base inicial (Sincronizada)
    banco_inicial = {
        
    "ansiedade": ["ansiedade", "ansioso", "ansiosa", "ansiose", "aflicao", "agonia", "apreensivo", "apreensiva", "apreensive", "panico", "ansiedade", "anciedade", "ancioso", "anciosa", "afliçao", "aflição", "afliçao", "apreencivo", "apreenciva", "panico", "pânico"],

    "sobrecarga": ["sobrecarga", "overload", "saturado", "saturada", "saturade", "irritabilidade", "cheio", "cheia", "cheie", "sensorial", "sobrecargu", "sobercarga", "saturadu", "saturadx", "sensurial", "irritabelidade"],

    "inercia": ["inercia", "muro invisivel", "paralisado", "paralisada", "paralisade", "bloqueado", "bloqueada", "bloqueade", "inerçia", "inércia", "paralizado", "paralizada", "paralizado", "bloquado", "muro invizivel"],

    "burnout": ["burnout", "esgotamento", "estafado", "estafada", "estafade", "fim da linha", "exaustao mental", "burnalt", "burnot", "esgotamentu", "exaustão", "exaustao", "exaustao"],

    "rsd": ["rsd", "rejeitado", "rejeitada", "rejeitade", "excluido", "excluida", "excluide", "mico", "vergonha", "sensibilidade a rejeicao", "rejeicao", "rejaitado", "rejaitada", "excluidu", "rejeiçao", "rejeição"],

    "tristeza": ["triste", "tristeza", "angustia", "melancolico", "melancolica", "melancolice", "desanimado", "desanimada", "desanimade", "tristre", "tristesa", "angústia", "angustia", "desanimadu"],

    "afeto": ["afeto", "carinho", "ternura", "querido", "querida", "queride", "amoroso", "amorosa", "amorose", "amado", "amada", "amade", "afetu", "carinhu", "amorosu", "queridu"],

    "hiperfoco": ["hiperfoco", "hiperfocada", "hiperfocado", "hiperfocade", "focado", "focada", "focade", "obcecado", "obcecada", "obcecade", "eletrizado", "eletrizada", "eletrizade", "hiper fodo", "iperfoco", "focadu", "obsecado", "obsecada", "eletrizadu"],

    "raiva": ["raiva", "odio", "furioso", "furiosa", "furiose", "bravo", "brava", "brave", "puto", "puta", "pute", "irritado", "irritada", "irritade", "raiava", "ódio", "furiosu", "bravu", "putu", "irritadu"],

    "confusao": ["confuso", "confusa", "confuse", "desorientado", "desorientada", "desorientade", "perdido", "perdida", "perdide", "atordoado", "atordoada", "atordoade", "confusu", "confuzão", "confusao", "perdidu", "atorduado"],

    "medo": ["medo", "pavor", "temor", "assustado", "assustada", "assustade", "receio", "ameaca", "vigilante", "acuado", "acuada", "acuade", "medu", "asustado", "asustada", "ameaça", "ameaca", "acuadu"],

    "shutdown": ["shutdown", "desligado", "desligada", "desligade", "travado", "travada", "travade", "apagão", "indiferente", "shatdown", "shutdon", "desligadu", "travadu", "apago"],

    "dissociacao": ["dissociacao", "desconectado", "desconectada", "desconectade", "distante", "mundo de vidro", "fora do corpo", "dissociaçao", "dissociação", "dissoçiaçao", "desconectadu", "disociacao"],

    "paz": ["paz", "calma", "tranquilo", "tranquila", "tranquile", "sereno", "serena", "serene", "leve", "relaxado", "relaxada", "relaxade", "pas", "tranquilu", "trankilo", "relaxadu"],

    "vergonha": ["vergonha", "envergonhado", "envergonhada", "envergonhade", "timidez", "humilhacao", "exposto", "exposta", "exposte", "culpa", "vergonha", "vergonha", "umilhaçao", "umilhação", "culpado", "culpada"],

    "tedio": ["tedio", "entediado", "entediada", "entediade", "subestimulado", "subestimulada", "subestimulade", "desinteresse", "tédio", "entediadu", "subestimuladu"],

    "vergonha_alheia": ["vergonha alheia", "constrangimento", "desconforto social", "mico alheio", "vergonha aleia", "constrangimentu"],

    "fome": ["fome", "faminto", "faminta", "faminte", "esfomeado", "esfomeada", "esfomeade", "vazio no estomago", "fomi", "famintu", "esfomeadu", "vazio no estomagu"],

    "sede": ["sede", "sedento", "sedenta", "sedente", "desidratado", "desidratada", "desidratade", "boca seca", "sedi", "sedentu", "desidratadu"],

    "sono": ["sono", "sonolento", "sonolenta", "sonolente", "cansaco", "exausto", "exausta", "exhauste", "esgotado", "esgotada", "esgotade", "sonu", "cansaço", "cansaco", "exaustu", "esgotadu"],

    "meltdown": ["meltdown", "explosao", "descontrole", "crise sensorial", "sobrecarga extrema", "meltdon", "explosão", "explosao", "descontroli"],

    "injustica": ["injustica", "revoltado", "revoltada", "revoltade", "indignado", "indignada", "indignade", "angustia etica", "injustiça", "injustiça", "revoltadu", "indignadu"],

    "solidao": ["solidao", "sozinho", "sozinha", "sozinhe", "isolado", "isolada", "isolade", "invisivel", "solidão", "solidao", "sozinhu", "isoladu", "invizivel"],

    "nao_verbal": ["nao verbal", "mudo", "muda", "mude", "sem fala", "silencioso", "silenciosa", "silenciose", "dificuldade em falar", "não verbal", "nao verbal", "muditu", "silenciosu"],

    "orgulho": ["orgulho", "orgulhoso", "orgulhosa", "orgulhose", "capaz", "vitorioso", "vitoriosa", "vitoriose", "realizado", "realizada", "realizade", "orgulhu", "orgulhosu", "vitoriosu", "realizadu"],

    "gratidao": ["gratidao", "grato", "grata", "grate", "agradecido", "agradecida", "agradecide", "gratidão", "gratidao", "agradeçidu", "agradecido"],

    "ecolalia": ["ecolalia", "looping", "ruminacao", "repetitivo", "repetitiva", "repetitive", "frase na cabeca", "mente presa", "ecolalia", "ruminaçao", "ruminação", "repetitivu", "cabeça"],

    "mal_estar": ["mal estar", "indisposto", "indisposta", "indisposte", "enjoado", "enjoada", "enjoade", "nausea", "mal estar", "indispostu", "enjoadu", "náusea"],

    "dor_de_cabeca": ["dor de cabeca", "enxaqueca", "cefaleia", "pressao na cabeca", "dor de cabeça", "enxaqueca", "preçao na cabeça"],

    "alivio": ["alivio", "descarregado", "descarregada", "descarregade", "concluido", "concluida", "concluide", "descanso", "alívio", "alivio", "concluidu", "descarregadu"],

    "nojo": ["nojo", "aversao", "repulsa", "enojado", "enojada", "enojade", "asco", "noju", "averçao", "aversão", "enojadu"],

    "curiosidade": ["curiosidade", "interessado", "interessada", "interessade", "curioso", "curiosa", "curiose", "investigativo", "curiosidadi", "interessadu", "curiosu"],

    "stimming": ["stimming", "autorregulacao", "estimulacao", "balanco", "movimento repetitivo", "agito", "estimulaçao", "estimulação", "balanço", "balanço"],

    "alegria": ["alegria", "felicidade", "feliz", "feliza", "felize", "contente", "euforico", "euforica", "euforice", "radiante", "alegria", "feliçidade", "eufórico", "radianti"],

    "luto": ["luto", "perda", "tristeza profunda", "choro", "sofrimento", "processando a perda", "lutu", "perda", "tristesa"]
}
    
    
    salvar_banco(banco_inicial)
    return banco_inicial

def salvar_banco(dados):
    with open(ARQUIVO_MEMORIA, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def buscar_sentimento(entrada):
    banco = carregar_banco()
    entrada_norm = normalizar(entrada)
    for categoria, variantes in banco.items():
        if any(normalizar(v) == entrada_norm for v in variantes):
            return categoria
    return None

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def aprender_novo_termo(entrada_desconhecida):
    """Interface de aprendizado moderna usando CustomTkinter."""
    
    # Gerenciamento da janela
    try:
        temp_root = ctk.CTkToplevel() 
    except:
        temp_root = ctk.CTk()

    temp_root.title("Aprendizado - Exoesqueleto")
    temp_root.geometry("450x550")
    temp_root.attributes("-topmost", True)
    
    # Variável para capturar a resposta
    resultado = {"nova_cat": None}

    def confirmar():
        val = entry.get().lower().strip()
        if val:
            resultado["nova_cat"] = val
            temp_root.destroy()

    # Carregamento dos dados
    banco = carregar_banco()
    lista_formatada = "\n".join([f"• {cat}" for cat in sorted(banco.keys())])
    
    # --- Interface Visual ---
    
    label_titulo = ctk.CTkLabel(temp_root, text="SINAL NÃO IDENTIFICADO", 
                                font=ctk.CTkFont(size=14, weight="bold"), text_color="#ff5555")
    label_titulo.pack(pady=(20, 5))

    label_sinal = ctk.CTkLabel(temp_root, text=f"'{entrada_desconhecida}'", 
                               font=ctk.CTkFont(size=18, weight="bold"))
    label_sinal.pack(pady=5)

    label_instrucao = ctk.CTkLabel(temp_root, text="Associe a uma categoria existente ou crie uma nova:",
                                   font=ctk.CTkFont(size=12))
    label_instrucao.pack(pady=10)

    # Caixa de texto rolável para as categorias
    textbox = ctk.CTkTextbox(temp_root, width=400, height=200, font=("Consolas", 12))
    textbox.pack(padx=20, pady=10, fill="both", expand=True)
    textbox.insert("0.0", f"CATEGORIAS ATUAIS:\n{'-'*30}\n{lista_formatada}")
    textbox.configure(state="disabled")

    # Entrada de texto customizada
    entry = ctk.CTkEntry(temp_root, placeholder_text="Digite a categoria aqui...", 
                         width=400, height=40)
    entry.pack(pady=10, padx=20)
    entry.focus_set()
    entry.bind("<Return>", lambda e: confirmar())

    # Botão estilizado
    btn_confirmar = ctk.CTkButton(temp_root, text="ATUALIZAR DICIONÁRIO", 
                                  command=confirmar, fg_color="#1f538d", hover_color="#2b71be")
    btn_confirmar.pack(pady=(10, 20), padx=20)

    # Loop para aguardar a interação
    temp_root.wait_window()

    nova_cat = resultado["nova_cat"]

    if nova_cat:
        if nova_cat not in banco:
            banco[nova_cat] = []
        
        if entrada_desconhecida not in banco[nova_cat]:
            banco[nova_cat].append(entrada_desconhecida)
            salvar_banco(banco)
            
        messagebox.showinfo("Sucesso", f"Memória Atualizada: '{entrada_desconhecida}' -> '{nova_cat}'")
        return nova_cat
    
    return None

# ---  PARA TESTAR SOZINHO ---
if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()
    teste = simpledialog.askstring("Teste Dicionário", "Como você descreveria o que sente?")
    if teste:
        res = buscar_sentimento(teste)
        if res:
            messagebox.showinfo("Scanner", f"Categoria detectada: {res}")
        else:
            aprender_novo_termo(teste)
    root.destroy()
