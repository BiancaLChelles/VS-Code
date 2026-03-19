import tkinter as tk
from tkinter import simpledialog, messagebox
import unicodedata
import re

def normalizar(texto):
    """Limpeza técnica interna para garantir que a comparação funcione."""
    if not texto: return ""
    # Remove acentos e converte para minúsculas
    texto = "".join(c for c in unicodedata.normalize('NFD', str(texto).lower().strip()) if unicodedata.category(c) != 'Mn')
    # Remove pontuação
    return re.sub(r'[^\w\s]', '', texto)

def tradutor_fisico(texto_usuario):
    # O sinal do usuário é limpo apenas para a lógica de busca
    sinal = normalizar(texto_usuario)
    
    # BANCO DE DADOS DE HARDWARE (OS 30 SENTIMENTOS)
    mapa_sentimentos = {
        "FOME": 
        ["fome", "estomago", "vazio", "roncando", "buraco na barriga", "fraqueza", "tontura de jejum", "salivando", "dor de cabeça de fome", "barriga roncando", "baixa energia", "tremedeira de fome", "estomago doendo", "falta de combustivel", "vontade de mastigar", "estomago contraindo", "visao escurecendo", "irritacao por fome", "hangry", "estomago alto", "vazio no tronco", "fraqueza nas pernas", "necessidade de glicose", "boca aguando", "salivacao excessiva", "pensando em comida", "estomago dando no", "sensacao de desmaio", "corpo sem sustento", "vontade de morder algo", "estomago sugando", "dor na boca do estomago", "falta de foco por fome", "abdomen retraido", "pontada de fome", "desejo calorico", "baixa de acucar", "corpo oco", "tronco vazio", "necessidade de mastigacao", "gosto de fome", "vontade de devorar", "energia em queda livre", "estomago acido"],
       
        "SEDE": 
        ["sede", "boca seca", "garganta seca", "labios rachados", "lingua pegajosa", "vontade de beber", "secura", "desidratado", "garganta arranhando", "sede de deserto", "saliva grossa", "dificuldade de engolir", "boca de lixa", "vontade de algo gelado", "labio descascando", "urina escura", "sede que nao passa", "lingua branca", "garganta em carne viva", "desejo de agua", "interior seco", "pele ressecada", "necessidade hidrica", "lingua pesada", "garganta fechando de sede", "falta de agua", "vontade de molhar a boca", "secura nas mucosas", "lingua aspera", "gosto de poeira"],
        
        "SONO / EXAUSTÃO":
        ["sono", "bocejo", "olho ardendo", "olho pesado", "pescoco caindo", "exaustao", "corpo moido", "fadiga", "sem energia", "bateria fraca", "querendo deitar", "palpebras pesadas", "corpo de chumbo", "moleza", "exausto", "morto de cansaco", "sem forcas", "visao embacada de cansaco", "coordenacao motora lenta", "corpo pedindo cama", "desligando", "sono pesado", "musculos moles", "olheira", "peso na nuca", "exaurido", "bocejando sem parar", "corpo arriado", "mente lenta", "falha de memoria por cansaco", "querendo fechar os olhos", "sono incontrolavel", "cansaco cronico", "exaustao fisica", "bracos pesados", "pernas arrastando", "vontade de apagar", "olhos fechando sozinhos", "pescoco sem forca", "moleza nos joelhos", "esgotamento total", "falta de ar de cansaco", "corpo derretendo"],
       
        "MELTDOWN (CRISE EXTERNA)": 
        ["explodir", "quebrar", "gritar", "ferver", "faisca", "vontade de bater", "pressao na cabeca", "nao aguento mais", "irradiando raiva", "vontade de fugir", "chutar", "estourar", "incendio interno", "vulcao", "transbordando", "panela de pressao", "querendo morder", "rosto queimando", "perda de controle", "ficar cego de raiva", "maos tremulas", "vontade de destruir", "corpo eletrico", "pulso acelerado", "gritar de raiva", "estimulo excessivo", "curto-circuito motor", "querendo arrancar a pele", "agressividade fisica", "nervos a flor da pele", "querendo socar a parede", "visao vermelha", "corpo tremendo de furia", "perda de filtro", "vontade de arrancar o cabelo", "sobrecarga motora", "crise de choro e grito", "descontrole total", "gritar de pulmao cheio", "maos querendo agarrar algo", "tensao explosiva", "cabeca fervilhando", "frenesi fisico"],
       
        "SHUTDOWN (CRISE INTERNA)": 
        ["mudo", "sem fala", "nao consigo falar", "travado", "desligado", "congelado", "estatico", "paralisado", "olhar morto", "olhar fixo", "vazio por dentro", "anestesiado", "robotico", "marmorizado", "ausente", "embotado", "membros pesados", "sem reacao", "curto-circuito interno", "pensamento lento", "querendo ficar no escuro", "encolhido", "mente em branco", "dissipado", "vontade de sumir dentro de si", "desconexao total", "estado catatonico", "fala arrastada", "ouvindo mas nao processando", "incapaz de mover um dedo", "camera lenta", "atordoado", "corpo de pedra", "voz que nao sai", "sistema travado", "olhar perdido", "sentido unico de vazio", "encapsulado", "muralha interna", "isolado do mundo", "corpo de cimento", "mente offline"],
       
        "DISSOCIAÇÃO": 
        ["fora do corpo", "nevoeiro", "nuvem", "distante", "sonhando acordado", "irreal", "mundo de vidro", "nao me reconheco", "flutuando", "desconectado", "vendo de cima", "perdi o tato", "corpo de algodao", "sensacao de sonho", "piloto automatico", "dormente", "mente longe", "maos estranhas", "tempo paralisado", "desrealizacao", "vultos", "anestesia emocional", "corpo oco", "vendo a vida de longe", "perda de profundidade", "realidade distorcida", "parecendo um fantasma", "sem sentir dor fisica", "desconectado do ambiente", "flutuando no espaco", "maos irreais", "corpo sem peso", "sensacao de estar em um aquario", "mundo sem cor", "percepcao alterada"],
       
        "ANSIEDADE / PÂNICO": 
        ["coracao", "taquicardia", "palpitacao", "falta de ar", "sufocando", "tremedeira", "mao suada", "formigamento", "no no estomago", "pavor", "vou morrer", "desespero", "tensao", "pernas bambas", "suor frio", "maos frias", "pes gelados", "falta de chao", "visao de tunel", "aperto no peito", "agonia", "maos tremulas", "bolo na garganta", "hiperventilacao", "sentindo o sangue pulsar", "dor no peito aguda", "medo de enlouquecer", "tontura subita", "calafrio na espinha", "frio no estomago", "respiracao curta", "musculos da face rigidos", "medo de perder o controle", "sensacao de desmaio iminente", "visao borrada", "formigamento no rosto", "maos dormentes", "querendo sair correndo", "pressao no torax", "ombros subindo", "aperto na garganta"],
       
        "SOBRECARGA SENSORIAL": 
        ["barulho", "luz", "cheiro forte", "etiqueta", "roupa pinicando", "muito som", "muita gente", "caos", "zumbido", "televisao alta", "poluicao visual", "toque indesejado", "agressao sonora", "irritacao tatil", "ambiente hostil", "ruido", "estatica", "tudo muito alto", "luz que doi", "cheiro enjoado", "pele sensivel demais", "muitos inputs", "bombardeio sensorial", "atordoado", "cheiros misturados", "pele queimando de toque", "dor sensorial", "sons cortantes", "luzes piscando na mente", "vontade de tapar os ouvidos", "mundo agressivo demais", "pele pinicando", "nervos expostos", "zumbido no ouvido", "cheiro de enxofre", "muita informacao visual"],
       
        "INÉRCIA EXECUTIVA": 
        ["nao consigo comecar", "preso no sofa", "muro invisivel", "procrastinando", "estancado", "nao consigo levantar", "trava mental", "querendo fazer mas nao indo", "corpo colado", "paralisia de decisao", "motor travado", "sem arranque", "preso no loop", "corpo pesado demais", "falta de iniciativa fisica", "bloqueio motor", "caminho bloqueado na mente", "vontade sem acao", "incapacidade de trocar de tarefa", "mente quer corpo nao vai", "parado no tempo", "corpo imobilizado"],
       
        "BURNOUT (ESGOTAMENTO)": 
        ["fim da linha", "acabou a bateria", "morto por dentro", "peso de mil toneladas", "sem alma", "nada faz sentido", "exaustao cronica", "colapso", "nao tenho forca para o basico", "derretido", "esgotado", "pau no sistema", "sem processamento", "anemia de alma", "apagao", "corpo falhando", "cinzas", "sem motivacao biologica", "colapso funcional", "incapaz de processar um oi", "alma drenada", "bateria viciada", "corpo sem resposta", "desanimo organico", "fim de ciclo"],
       
        "RSD (DISFORIA SENSÍVEL À REJEIÇÃO)": 
        ["ele me odeia", "falei errado", "mico", "me acham estranho", "rejeitado", "excluido", "dor de critica", "querendo sumir de vergonha", "humilhacao", "sentindo-se um peso", "ferida social", "alma exposta", "peito aberto", "dor de julgamento", "sentimento de lixo", "dor fisica de vergonha", "queimacao no peito social", "obsessao pelo erro cometido", "rejeicao fisica", "pontada no coracao social", "vontade de se esconder", "dor de reprovacao"],
       
        "TRISTEZA / ANGÚSTIA": 
        ["no na garganta", "vontade de chorar", "choro preso", "peito apertado", "triste", "melancolia", "solucando", "desanimado", "baixo astral", "nuvem cinza", "coracao pesado", "vazio no peito", "luto", "tristeza funda", "corpo sem osso", "vontade de ficar no quarto", "peso no coracao", "amargura", "falta de cor no dia", "dor na alma", "peito oco de dor", "alma cinzenta", "corpo pesado"],
       
        "AFETO / AMOR": 
        ["coracao quente", "borboletas no estomago", "querer abracar", "carinho", "ternura", "admiracao", "saudade boa", "conexao", "querido", "acolhido", "quentinho", "paz no peito", "derretendo de amor", "sorriso bobo", "corpo relaxado", "vontade de cuidar", "peito expandindo", "vibracao suave", "calor interno", "pele relaxada", "seguranca fisica", "conforto no abraco", "batimento calmo"],
       
        "HIPERFOCO / EMPOLGAÇÃO": 
        ["obcecado", "eletrizado", "nao consigo parar", "viciado na tarefa", "eureka", "brilhante", "energy alta", "uhu", "venci", "animado", "entusiasmado", "modo tunel", "vidrado", "focado", "pilhado", "acelerado", "hiperestimulado", "corpo vibrando", "nao piscar", "flow", "mente a mil", "dopamina", "efervescencia", "inquieto de alegria", "coracao saltitante", "sem sono de empolgacao", "foco total", "perda da nocao de tempo", "ligado no 220v", "vibracao nas maos", "visao focada", "pulso vibrante", "mente acelerada"],
       
        "RAIVA": 
        ["odio", "mandibula presa", "punhos fechados", "calor subindo", "irritado", "bravo", "furioso", "querendo gritar", "sangue quente", "indignacao", "fervendo", "querendo rosnar", "explosivo", "pelos em pe", "ombros tensos", "dentes trincados", "respiracao pesada", "veia saltando", "vontade de socar", "irritabilidade", "corpo rigido", "olhar fixo de raiva", "maos fechadas", "calor no pescoco", "respiracao ofegante", "impaciencia fisica", "vontade de xingar"],
       
        "CONFUSÃO / OVERLOAD COGNITIVO": 
        ["nao entendi", "confuso", "perdido", "embaralhado", "muita coisa", "cerebro frito", "muitos dados", "labirinto mental", "sem logica", "travado no erro", "cabeca pesada", "chiado mental", "emaranhado", "inputs demais", "excesso de informacao", "curto circuito no cerebro", "pensamento atropelado", "incapaz de decidir", "nevoa mental", "brain fog", "ruido mental"],
       
        "MEDO / INSEGURANÇA": 
        ["frio na barriga", "incerto", "vigilante", "receio", "assustado", "pe atras", "com medo", "vulneravel", "ameacado", "arrepio na espinha", "sensacao de perigo", "corpo alerta", "instinto de fuga", "querendo se esconder", "olhando para os lados", "apreensivo", "coracao na boca", "instinto de preservacao", "vigilancia constante", "musculos prontos para correr"],
       
        "ECOLALIA (REPETIÇÃO)": 
        ["repetindo", "frase na cabeca", "musica chiclete", "eco", "palavra viciante", "looping mental", "estimulacao sonora", "vicio de fala", "repeticao verbal", "ecolalia", "sons repetidos", "necessidade de repetir", "frase viciosa", "palatabilidade de palavras", "eco mental"],
       
        "MAL-ESTAR FÍSICO": 
        ["enjoo", "nausea", "tontura", "dor no corpo", "latejando", "pontada", "mal estar", "indisposto", "corpo estranho", "instabilidade", "vontade de vomitar", "calafrio", "pressao baixa", "suor estranho", "corpo mole", "pontadas nas costas", "musculos doendo", "vomito", "dor visceral", "sensacao de doenca", "corpo pedindo pausa fisica", "desconforto gastrico"],
       
        "DOR DE CABEÇA / ENXAQUECA": 
        ["pressao nos olhos", "cabeca explodindo", "pulsacao na tempora", "luz doi", "martelada", "agulhada na cabeca", "cerebro pulsando", "peso na testa", "pontada no olho", "enxaqueca", "cabeca latejando", "nausea de dor", "dor na nuca", "pontadas cranianas", "visao com aura"],
       
        "NOJO / AVERSÃO": 
        ["nojo", "ascom", "ecat", "repugnante", "gosmento", "textura ruim", "cheiro de podre", "nausea sensorial", "arrepio de nojo", "vontade de cuspir", "pele arrepiada de asco", "repulsa fisica", "garganta fechando de nojo", "vontade de lavar a mao"],
       
        "CURIOSIDADE": 
        ["quero saber", "como funciona", "interessado", "pesquisando", "instigado", "descobrir", "investigando", "cacador de dados", "fome de saber", "explorando", "mente aberta", "busca de padrao"],
       
        "STIMMING (AUTORREGULAÇÃO)": 
        ["balancando", "girando", "maos balancando", "flapping", "pulando", "batendo o pe", "mexendo no cabelo", "mordendo a caneta", "preciso me mexer", "corpo pedindo ritmo", "balanco", "sacudindo", "esfregando as maos", "vocalizando", "apertando as maos", "balancar de cabeca", "necessidade de pressao", "andando sem parar", "estalando os dedos", "morder os labios", "balancar o tronco", "pressao profunda", "apertar objetos"],
       
        "FRUSTRAÇÃO": 
        ["nao funcionou", "erro 404", "deu errado", "vontade de desistir", "irritado com erro", "output invalido", "travado no problema", "indignado", "insucesso", "impaciencia", "frustrado", "falha no codigo", "expectativa quebrada", "nao sai do lugar", "vontade de largar tudo"],
       
        "INJUSTIÇA":
        ["absurdo", "antietico", "injusto", "quebra de logica", "erro de conduta", "revoltado", "quebra de expectativa", "falta de criterio", "injustica", "violacao de protocolo", "indignacao moral", "nao e justo", "erro de admin", "falha de carater externa"],
       
        "SOLIDÃO": 
        ["sozinho", "isolado", "sem conexao", "servidor unico", "falta de troca", "invisivel", "sem ninguem para falar", "vazio social", "desconectado de humanos", "solitario", "falta de pacotes sociais", "isolamento forcado", "sem par"],
       
        "NÃO-VERBAL": 
        ["sem fala", "nao verbal", "voz nao sai", "modulo de audio off", "dificuldade de falar", "palavra some", "fala arrastada", "mudo temporario", "energia para falar zero", "nao quero falar", "comunicacao dificil", "bloqueio de fala"],
       
        "ORGULHO / SUCESSO": 
        ["consegui", "venci", "eu fiz", "missao cumprida", "upgrade", "competente", "satisfeito com o codigo", "deploy funcional", "sensacao de dever cumprido", "eu sou bom nisso", "resultado positivo"],
       
        "GRATIDÃO": 
        ["obrigado", "grato", "agradecido", "sorte", "backup positivo", "valorizar", "reconhecimento", "sentimento bom", "aliviado e grato", "reconhecer o bem"],
       
        "PAZ / HOMEOSTASE": 
        ["homeostase", "silencio", "calma", "equilibrio", "corpo leve", "mente limpa", "sem alertas", "estavel", "baixa latencia", "tranquilidade", "sistema em ordem"]
    }

    pontuacao = {}

    for categoria, termos in mapa_sentimentos.items():
        pontos = 0
        for termo in termos:
            termo_limpo = normalizar(termo)
            # A correção fundamental: verifica se a palavra-chave está dentro do que o usuário escreveu
            if termo_limpo in sinal:
                pontos += 1
        
        if pontos > 0:
            pontuacao[categoria] = pontos

    if not pontuacao:
        return "Sinal Desconhecido"

    # Retorna o sentimento que teve mais palavras correspondentes encontradas
    return max(pontuacao, key=pontuacao.get)

def executar():
    root = tk.Tk()
    root.withdraw()
    
    prompt = (
        "SISTEMA DE VARREDURA FÍSICA\n"
        "---------------------------\n"
        "Descreva detalhadamente o que você está sentindo no corpo agora:"
    )
    
    entrada = simpledialog.askstring("Input de Hardware", prompt)
    
    if entrada:
        # O resultado é apenas a string do sentimento (ex: "FOME")
        resultado = tradutor_fisico(entrada)
        
        # Exibe o diagnóstico limpo
        messagebox.showinfo("Diagnóstico de Varredura", f"Resultado da análise de sensores:\n\n>>> {resultado}")
    
    root.destroy()

if __name__ == "__main__":
    executar()
