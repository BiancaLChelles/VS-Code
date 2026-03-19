import tkinter as tk
from tkinter import simpledialog, messagebox
import json
import os
import unicodedata
import re

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
        "medo": ["medo", "assustado", "receio", "ameaca", "frio na barriga", "vigilante"],
        "hiperfoco": ["hiperfoco", "focado", "obcecado", "nao consigo parar", "eletrizado"],
        "looping": ["ruminacao", "looping", "mente presa", "repetitivo", "frase na cabeca", "ecolalia"],
        "shutdown": ["shutdown", "olhar morto", "olhar fixo", "travado", "desligado"],
        "tristeza": ["triste", "angustia", "no na garganta", "vontade de chorar", "choro preso"],
        "ansiedade": ["ansiedade", "peito apertado", "coracao acelerado", "falta de ar", "tremendo", "panico"],
        "sensorial": ["barulho", "luz", "agitacao sensorial", "muito som", "etiqueta incomodando", "meltdown", "sobrecarga"],
        "verbal": ["nao verbal", "mudo", "sem fala", "nao consigo falar"],
        "inercia": ["inercia", "nao consigo comecar", "preso no sofa", "muro invisivel"],
        "fome": ["fome", "estomago vazio", "estomago roncando", "fraco", "querendo comer"],
        "sede": ["sede", "agua", "boca seca", "garganta seca"],
        "cansaco": ["cansado", "exausto", "energia baixa", "bateria fraca", "sono", "exaustao"],
        "injustica": ["injustica", "errado", "mentira", "falta de logica", "revoltado", "angustia etica"],
        "rejeicao": ["rsd", "ele me odeia", "rejeitado", "excluido", "mico", "vergonha"],
        "empolgada": ["empolgado", "animado", "dopamina", "uhu", "venci", "empolgacao"],
        "paz": ["paz", "calma", "tranquilo", "zen", "sereno", "leve"],
        "conexao": ["conexao", "compreendido", "acolhido", "amado", "presenca"],
        "alivio": ["alivio", "tirei um peso", "ufa", "concluido"],
        "dissociacao": ["fora do corpo", "nevoeiro", "nuvem", "distante", "mundo de vidro", "dissociacao"],
        "burnout": ["esgotamento", "fim da linha", "acabou a bateria", "morto por dentro", "burnout"],
        "afeto": ["coracao quente", "borboletas no estomago", "carinho", "ternura", "afeto"],
        "raiva": ["odio", "mandibula presa", "punhos fechados", "querendo gritar", "raiva"],
        "confusao": ["nao entendi", "cerebro frito", "perdido", "muita coisa", "confusao"],
        "frustracao": ["nao da certo", "estagnado", "impotente", "desisto", "frustracao"],
        "solidao": ["sozinho", "isolado", "vazio", "invisivel", "solidao"],
        "orgulho": ["consegui", "fiz sozinho", "capaz", "orgulhoso", "orgulho"],
        "gratidao": ["obrigado", "grato", "ainda bem", "valorizar", "gratidao"],
        "culpa": ["nao devia", "peso na consciencia", "arrependido", "remorso", "culpa"],
        "tedio": ["chato", "sem nada", "inquieto de tédio", "tempo nao passa", "tedio"],
        "mal_estar": ["enjoo", "tontura", "dor no corpo", "indisposto", "mal estar"],
        "dor_cabeca": ["pressao nos olhos", "cabeca explodindo", "martelada", "dor de cabeca"],
        "nojo": ["ascom", "ecat", "gosmento", "textura ruim", "nojo"],
        "curiosidade": ["quero saber", "como funciona", "interessado", "descobrir", "curiosidade"]
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

def aprender_novo_termo(entrada_desconhecida):
    """Interface de aprendizado otimizada para ser chamada por outros scripts."""
    # Tenta usar uma janela já existente se houver, senão cria uma temporária
    try:
        temp_root = tk.Toplevel() # Cria uma janela sobreposta se o Tk principal existir
        temp_root.withdraw()
    except:
        temp_root = tk.Tk()
        temp_root.withdraw()

    temp_root.attributes("-topmost", True)

    banco = carregar_banco()
    lista_formatada = "\n".join([f"• {cat}" for cat in sorted(banco.keys())])
    
    instrucao = (f"Sinal '{entrada_desconhecida}' não identificado.\n\n"
                 f"Associe a uma categoria da lista ou digite uma NOVA:\n"
                 f"------------------------------------------\n"
                 f"{lista_formatada}")
    
    nova_cat = simpledialog.askstring("Aprendizado - Exoesqueleto", instrucao)

    if nova_cat:
        nova_cat = nova_cat.lower().strip()
        if nova_cat not in banco:
            banco[nova_cat] = []
        
        if entrada_desconhecida not in banco[nova_cat]:
            banco[nova_cat].append(entrada_desconhecida)
            salvar_banco(banco)
            
        messagebox.showinfo("Sucesso", f"Memória Atualizada: '{entrada_desconhecida}' -> '{nova_cat}'")
        temp_root.destroy()
        return nova_cat
    
    temp_root.destroy()
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
