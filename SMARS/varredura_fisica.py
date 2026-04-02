import tkinter as tk
from tkinter import simpledialog, messagebox
import unicodedata
import re

def normalizar(texto):
    """Limpeza técnica interna para garantir que a comparação funcione."""
    if not texto: return ""
    if re.fullmatch(r'\.+', texto.strip()):
        return "silencio_pontos"
    # Remove acentos e converte para minúsculas
    texto = "".join(c for c in unicodedata.normalize('NFD', str(texto).lower().strip()) if unicodedata.category(c) != 'Mn')
    # Remove pontuação
    texto = re.sub(r'[^\w\s]', '', texto)
    return " ".join(texto.split())

def tradutor_fisico(texto_usuario):
    # O sinal do usuário é limpo apenas para a lógica de busca
    sinal = normalizar(texto_usuario)
    
    # BANCO DE DADOS DE HARDWARE (OS 30 SENTIMENTOS)
    mapa_sentimentos = {
       "FOME": [
    "fome", "estomago", "estomago vazio", "roncando", "buraco na barriga", "fraqueza", "tontura de jejum", 
    "salivando", "dor de cabeça de fome", "barriga roncando", "baixa energia", "tremedeira de fome", 
    "estomago doendo", "falta de combustivel", "vontade de mastigar", "estomago contraindo", 
    "visao escurecendo", "irritacao por fome", "hangry", "estomago alto", "vazio no estomago", 
    "vazio abdominal", "fraqueza nas pernas", "necessidade de glicose", "boca aguando", 
    "salivacao excessiva", "pensando em comida", "estomago dando no", "sensacao de desmaio", 
    "corpo sem sustento", "vontade de morder algo", "estomago sugando", "dor na boca do estomago", 
    "falta de foco por fome", "abdomen retraido", "pontada de fome", "desejo calorico", "baixa de acucar", 
    "corpo oco de fome", "tronco vazio por fome", "necessidade de mastigacao", "gosto de fome", 
    "vontade de devorar", "energia em queda livre", "estomago acido", "fomi", "estomgo", "estumago", 
    "bariga roncando", "buraqu no estomago", "vontade de kume", "preciso comer", "falta de comida", 
    "querendo rango", "estomago gritando", "sem comer", "desmaio de fome", "fome de leao", 
    "querendo morder a parede", "fomee", "fomeee", "estômgo", "estomgo doendo", "vontade de comer tudo", 
    "estomgu", "buraquinho na bariga", "estomago vaziu", "precizo de comida", "fome de morre", "fomii", 
    "hipoglicemia", "necessidade nutricional", "inanição", "estomgo roncand", "vazio no estomgo", 
    "querendo cumida", "precizo cume", "fome extrema", "estomago doend", "fraqueza por falta de comida", 
    "querendo mastigar algo", "estomago nas costas", "vontade de almocar", "vontade de jantar", 
    "vntd d comer", "preciso d cmer", "fme", "estmgo", "estmg", "vntd d rango", "fomi d+", "fome dms", 
    "fome braba", "preciso d glicose", "fome do kct", "fomr", "fomw", "estomaho", "estomafgo", 
    "comer um boi", "estomago grudado nas costas", "morrendo de inanição", "estômago falando", 
    "vazio por dentro no abdômen", "fome de mendigo", "preciso de sustento", "boca foi feita pra comer", 
    "larica", "laricado", "vontade de lanchar", "rangar", "bater um prato", "vontade de doce", 
    "vontade de salgado", "mão tremendo de fome", "suor frio fome"
],
       
        "SEDE": [
    "sede", "boca seca", "garganta seca", "labios rachados", "lingua pegajosa", "vontade de beber", "secura", 
    "desidratado", "garganta arranhando", "sede de deserto", "saliva grossa", "dificuldade de engolir", 
    "boca de lixa", "vontade de algo gelado", "labio descascando", "urina escura", "sede que nao passa", 
    "lingua branca", "garganta em carne viva", "desejo de agua", "interior seco de sede", "pele ressecada", 
    "necessidade hidrica", "lingua pesada", "garganta fechando de sede", "falta de agua", 
    "vontade de molhar a boca", "secura nas mucosas", "lingua aspera", "gosto de poeira", "sedi", 
    "garganta secaa", "preciso de agua", "querendo beber", "boca de gesso", "lingua seca", "vontade de h2o", 
    "boca colando", "garganta pegando fogo", "desidratacao", "falta de liquido", "copo d'agua", 
    "corpo seco de sede", "garganta travada", "beber algo", "sedee", "sedeeeee", "boca de lixa", 
    "garganta de deserto", "precizo de agua", "sedii", "boca ressecada", "garganta secaaa", "vontade d agua", 
    "boca colada", "lingua de lixa", "desidratado", "xerostomia", "necessidade de hidratação", 
    "garganta de poeira", "querendo h2o", "beber agua", "preciso d agua", "sese", "sece", "boca de deserto", 
    "garganta em brasa", "lingua rachada", "sde", "vntd d beber", "preciso d h2o", "preciso d agua gld", 
    "boca saca", "gargants", "gargnata", "swde", "ssde", "sedd", "sedee dms", "sedi d+", "preciso d líquido", 
    "seco igual deserto", "garganta empoeirada", "virado em pó", "preciso de um gole", "boca pregando", 
    "beber até o mar", "morrendo de sede", "interior esturricado", "pele de deserto", "glub glub", 
    "preciso dágua", "vontade de suco", "tontura de sede", "dor de cabeça de sede"
],
        
      "SONO": [
    "sono", "bocejo", "olho ardendo", "olho pesado", "olhos pesados", "olhos pesando", "olhar pesado", 
    "pálpebra pesada", "pescoco caindo", "exaustao", "corpo moido", "fadiga", "sem energia", "bateria fraca", 
    "querendo deitar", "palpebras pesadas", "corpo pesado de sono", "moleza", "exausto", "morto de cansaco", 
    "sem forcas", "visao embacada de cansaco", "coordenacao motora lenta", "corpo pedindo cama", "desligando", 
    "sono pesado", "musculos moles", "olheira", "peso na nuca", "exaurido", "bocejando sem parar", 
    "corpo arriado", "mente lenta de sono", "falha de memoria por cansaco", "querendo fechar os olhos", 
    "sono incontrolavel", "cansaco cronico", "exaustao fisica", "bracos pesados", "pernas arrastando", 
    "vontade de apagar", "olhos fechando sozinhos", "pescoco sem forca", "moleza nos joelhos", 
    "esgotamento total", "falta de ar de cansaco", "corpo derretendo", "sonoo", "bocejando", "cansaco", 
    "cansado", "quero dormir", "morrendo de sono", "preciso de cama", "olho fechando", "exuastao", 
    "exastao", "cançaso", "cansaso", "acabado", "destruido", "sem pilha", "sonolencia", "preguica de existir", 
    "querendo cochilar", "sonuu", "exausto total", "corp moido", "morto de cansaço", "sono dms", 
    "exaustãoo", "exausta", "exaustaum", "sonolento", "podre de sono", "letargia", "astenia", 
    "exaustao severa", "corpo sem bateria", "sono absurdo", "precizo dormir", "morto de cansaço", 
    "olho ardend", "exaustão física", "fadiga muscular", "querendo apagar", "olho fechando sozinho", 
    "sono incontrolável", "sno", "snolento", "exausto dms", "acabado d+", "morto de cansaç", "sonooo", 
    "sonn", "somno", "sonp", "soni", "exuastão", "exasutao", "cansadao", "canasdo", "cansadi", 
    "preciso dmir", "quero dromir", "querendo dmit", "bat fraca", "sem bat", "pregar o olho", 
    "morrendo de cansaço", "olhos de vidro de sono", "pescoço de borracha", "sono de pedra", 
    "desligar os motores", "cair de sono", "pescar de sono", "estar no bagaço", "estar no pó", 
    "pedindo arrego", "preciso de um berço", "zero por cento", "só o pó", "dromir", "preciso dumi", 
    "sonooooo", "cabeça caindo de sono", "pescando", "nas últimas"
],
       
        "MELTDOWN": [
    "explodir", "quebrar", "gritar", "ferver", "faisca", "vontade de bater", "pressao na cabeca", "nao aguento mais", 
    "irradiando raiva", "vontade de fugir", "chutar", "estourar", "incendio interno", "vulcao", "transbordando", 
    "panela de pressao", "querendo morder", "rosto queimando", "perda de controle", "ficar cego de raiva", 
    "maos tremulas", "vontade de destruir", "corpo eletrico", "pulso acelerado", "gritar de raiva", 
    "estimulo excessivo", "curto-circuito motor", "querendo arrancar a pele", "agressividade fisica", 
    "nervos a flor da pele", "querendo socar a parede", "visao vermelha", "corpo tremendo de furia", 
    "perda de filtro", "vontade de arrancar o cabelo", "sobrecarga motora", "crise de choro e grito", 
    "descontrole total", "gritar de pulmao cheio", "maos querendo agarrar algo", "tensao explosiva", 
    "cabeca fervilhando", "frenesi fisico", "explodi", "vontade de quebra tudo", "querendo gritar", 
    "perdi as estribeiras", "surto", "surtando", "nao me toca", "raiva descontrolada", "vontade de sumir", 
    "nao aguento", "iaaaaaaa", "aaaaaaa", "arrgh", "gritando", "quebrando", "estourando", "colapso nervoso", 
    "raiva fisica", "explodindo", "vou estourar", "nao aguento maisss", "meltdownn", "vontade de socar tudo", 
    "gritaria", "quebradeira", "perder o controle", "surto psicotico", "desregulação emocional externa", 
    "crise explosiva", "vontade de destruir tudo", "raiva visceral", "meltdon", "metldown", "vou esplodir", 
    "vontade de chutar tudo", "rosto pegando fogo", "corpo em curto", "espiral de raiva", "surto de raiva", 
    "gritando muito", "explod", "vou quebrar td", "vntd d bater", "nao aguento +", "nao aguento mms", 
    "explodind", "surtand", "vou surtar", "vou surta", "explodirrr", "metdown", "meuudown", "surtoo", 
    "meltaown", "explodit", "exolodir", "quebrsr", "gritat", "sair do sério", "chutar o balde", 
    "perder as estribeiras", "virar o bicho", "virar o capeta", "soltar os cachorros", "pisar no calo", 
    "dar um chilique", "ficar possesso", "quebrar o pau", "sair de si", "sangue subindo", "perder a cabeça", 
    "subir nas paredes", "espumar de raiva", "estar por um fio", "vontade de me bater", "bater a cabeça", 
    "sobrecarga explosiva", "sistema em chamas", "fritando", "vontade de urrar"
],
       
       "SHUTDOWN": [
    "mudo", "sem fala", "nao consigo falar", "travado", "desligado", "congelado", "estatico", "paralisado", 
    "olhar morto", "olhar fixo", "anestesiado", "robotico", "marmorizado", "ausente", "embotado", 
    "membros pesados", "sem reacao", "curto-circuito interno", "pensamento lento", "querendo ficar no escuro", 
    "encolhido", "mente em branco", "dissipado", "vontade de sumir dentro de si", "desconexao total", 
    "estado catatonico", "fala arrastada", "ouvindo mas nao processando", "incapaz de mover um dedo", 
    "camera lenta", "atordoado", "corpo de pedra", "voz que nao sai", "sistema travado", "olhar perdido", 
    "sentido unico de vazio", "encapsulado", "muralha interna", "isolado do mundo", "corpo de cimento", 
    "mente offline", "travei", "desliguei", "nao sai som", "sem palavras", "bloqueado", "estatua", 
    "mente vazia", "nao processando", "off", "fora do ar", "sumido", "encolhido", "catatonia", "mudez", 
    "incapaz de falar", "shutdown", "chutdown", "lutdown", "travadao", "congelada", "shoudown", "desligada", 
    "nao consigo abri a boca", "travadissimo", "estatico total", "mudez seletiva", "mente apagada", 
    "fala zero", "retraimento social", "desregulação interna", "sistema offline", "paralizado", 
    "estatua viva", "nao consigo me mover", "mente bloqueada", "sem resposta", "olhar pro nada", 
    "ouvido desligado", "travada total", "chutidown", "shutidown", "shtdown", "off total", "desligad", 
    "nao consigo flr", "n consigo flr", "travad", "congld", "congldo", "sem fl", "mudo dms", "shutdon", 
    "shutdo", "shurdown", "shatdown", "travsdo", "congelaso", "desligaso", "mudo d+", "ficar na concha", 
    "se fechar em copas", "engolir a seco", "ficar mudo igual uma porta", "estar em outro mundo", 
    "perder o fio da meada", "ficar no seu quadrado", "entrar no casulo", "se trancar por dentro", 
    "ficar que nem uma estátua", "mente no modo avião", "parecer uma parede", "estar no escuro", 
    "cercado por muros", "vácuo interno", "vácuo mental", "delay", "sem sinal", "zumbido no vácuo", 
    "não entendo o que dizem", "travs", "offf", "corpo de chumbo", "pernas de pedra"
],
       
      "DISSOCIAÇÃO": [
    "fora do corpo", "nevoeiro", "nuvem", "distante", "sonhando acordado", "irreal", "mundo de vidro", 
    "nao me reconheco", "flutuando", "desconectado", "vendo de cima", "perdi o tato", "corpo de algodao", 
    "sensacao de sonho", "piloto automatico", "dormente", "mente longe", "maos estranhas", "tempo paralisado", 
    "desrealizacao", "vultos", "corpo oco", "vendo a vida de longe", "perda de profundidade", 
    "realidade distorcida", "parecendo um fantasma", "sem sentir dor fisica", "desconectado do ambiente", 
    "flutuando no espaco", "maos irreais", "corpo sem peso", "sensacao de estar em um aquario", "mundo sem cor", 
    "percepcao alterada", "fora de mim", "desreali", "sonho acordado", "corpo estranho", "nao sou eu", 
    "vendo de fora", "desconectada", "distancia da realidade", "parece filme", "nevoa", "nevoa mental", 
    "mente fora", "avoado", "disperso", "lugar nenhum", "despersonalizacao", "dissoçiacao", "fora da realidade", 
    "parece sonho", "tudo irreal", "nao sinto meu corpo", "corpo de mentira", "flutuando no nada", 
    "mente em outro lugar", "disociaçao", "despersonalização", "desrealização", "estado dissociativo", 
    "sensação de bolha", "mundo irreal", "fora do eixo", "desconexo", "corpo mecanico", "mente distante", 
    "dissoçiaçao", "nuvem na cabeca", "nao me sinto aqui", "dissoç", "dissoc", "fora d mim", "nao so eu", 
    "flutuand", "distnt", "irreal dms", "n me reconheço", "piloto auto", "disoç", "disoçiaçao", "dissisciaçao", 
    "dissoaciação", "fora do cirpo", "fora di corpo", "flutuandp", "mebte longe", "estar no mundo da lua", 
    "pisar em nuvens", "estar fora de órbita", "viver num aquário", "parecer um robô", "estar no automático", 
    "se sentir um fantasma", "corpo sem alma", "estar em transe", "ver a vida passar em câmera lenta", 
    "não estar nem aí nem aqui", "sentir que a ficha não caiu", "estar num nevoeiro", "lag", "quadro a quadro", 
    "visão de túnel", "som abafado", "corpo de plástico", "pessoa de papel", "sem sentir o chão", "fora daki"
],
       
      "ANSIEDADE": [
    "coracao", "taquicardia", "palpitacao", "falta de ar", "sufocando", "tremedeira", "mao suada", "formigamento", 
    "no no estomago", "pavor", "vou morrer", "desespero", "tensao", "pernas bambas", "suor frio", "maos frias", 
    "pes gelados", "falta de chao", "visao de tunel", "aperto no peito", "agonia", "maos tremulas", 
    "bolo na garganta", "hiperventilacao", "sentindo o sangue pulsar", "dor no peito aguda", "medo de enlouquecer", 
    "tontura de pânico", "calafrio na espinha", "frio no estomago", "respiracao curta", "musculos da face rigidos", 
    "medo de perder o controle", "desmaio de ansiedade", "visao borrada", "formigamento no rosto", "maos dormentes", 
    "querendo sair correndo", "pressao no torax", "ombros subindo", "aperto na garganta", "coracao batendo forte", 
    "ansiedade", "crise de panico", "tremendo", "sufocado", "angustia", "medo", "aperto", "coracao saindo pela boca", 
    "suando frio", "pânico", "panico", "anciedade", "ansiendade", "anxiedade", "corassaun", "peito apertado", 
    "palpitaçao", "taquicardia forte", "ansiedade a mil", "pânicoo", "medo de morre", "falta de ar horrível", 
    "tremendo muito", "angustya", "anciedadee", "coração aceleradíssimo", "crise de ansiedade", "ataque de pânico", 
    "hiperventilação", "apreensão", "estado de alerta", "anciedade extrema", "coracao acelerado", "coracao pulando", 
    "falta de ar constante", "corasao", "panico total", "medo de morrer agora", "ansid", "ancid", "coraca", 
    "tremend", "taquc", "pavor dms", "vou morre", "ansiedade d+", "anciedade dms", "ansiedadr", "ansiedsde", 
    "ansiedaxe", "coracão", "coraçaoo", "palpitacoa", "palpitacaoo", "pnic", "pnc", "estar com o coração na mão", 
    "ficar com os nervos à flor da pele", "sentir o chão sumir", "estar com o coração na boca", "ter um nó na garganta", 
    "sentir o estômago dar voltas", "ficar com a pulga atrás da orelha", "estar em brasa", 
    "ficar com as pernas de gelatina", "perder o fôlego", "sentir o mundo desabar", "estar por um fio", 
    "beira de um colapso", "pensamento a mil", "mente acelerada", "futurismo", "n consig respirar", 
    "peito explodindo", "motor ligado", "vibração interna"
],
       
       "SOBRECARGA": [
    "barulho", "luz", "cheiro forte", "etiqueta", "roupa pinicando", "muito som", "muita gente", "caos", "zumbido", 
    "televisao alta", "poluicao visual", "toque indesejado", "agressao sonora", "irritacao tatil", "ambiente hostil", 
    "ruido", "estatica", "tudo muito alto", "luz que doi", "cheiro enjoado", "pele sensivel demais", "muitos inputs", 
    "bombardeio sensorial", "atordoado", "cheiros misturados", "pele queimando de toque", "dor sensorial", 
    "sons cortantes", "luzes piscando na mente", "vontade de tapar os ouvidos", "mundo agressivo demais", 
    "pele pinicando", "zumbido no ouvido", "cheiro de enxofre", "muita informacao visual", "muito barulho", 
    "luz forte", "som alto", "cheiro ruim", "muito estimulo", "sensorial", "overload", "lugar barulhento", 
    "luz incomodando", "som irritante", "toque chato", "pele sensivel", "agoniado com som", "irritacao visual", 
    "muita luz", "barulhera", "zuada", "zumbido forte", "overload sensorial", "muita informaçao", "luzes fortes", 
    "sons irritantes", "cheiro insuportável", "ambiente barulhento", "poluiçao sonora", "estatíca", "barulho dms", 
    "hipersensibilidade sensorial", "bombardeio de estímulos", "irritação auditiva", "caos visual", 
    "barulho insuportavel", "muito input", "luz q doi", "som q corta", "cheiro q enjoa", "senssorial", 
    "muito barulhooo", "sensord", "ovrload", "mto barulho", "mta luz", "mto som", "overlod", "sensorial dms", 
    "overload d+", "barulh", "brulho", "batulho", "luz forte dms", "mto estimulo", "senssorial", "barulhom", 
    "barulhi", "mundo está gritando", "luz cortando os olhos", "estar numa centrífuga", "sentir a pele em carne viva", 
    "estar num ninho de vespas", "ruído branco insuportável", "luz que fura", "ser bombardeado por tudo", 
    "estar numa feira livre", "sentir o som no osso", "ambiente me esmagando", "agulhadas nos ouvidos", 
    "textura ruim", "barulho de mastigação", "luz de farmácia", "muita falação", "atrito da roupa", 
    "luz branca", "socorro som", "pqp q barulho"
],
       "INÉRCIA": [
    "nao consigo comecar", "preso no sofa", "muro invisivel", "procrastinando", "estancado", "nao consigo levantar", 
    "trava mental", "querendo fazer mas nao indo", "corpo colado", "paralisia de decisao", "motor travado", 
    "sem arranque", "preso no loop", "corpo pesado demais", "falta de iniciativa fisica", "bloqueio motor", 
    "caminho bloqueado na mente", "vontade sem acao", "incapacidade de trocar de tarefa", "mente quer corpo nao vai", 
    "parado no tempo", "corpo imobilizado", "nao consigo fazer", "travado", "preso", "sem acao", 
    "querendo mas nao conseguindo", "paralisado no sofa", "trava para fazer", "inercia", "inercia mental", 
    "nao saio do lugar", "travadao", "procrastinacao", "bloqueado para agir", "inercia executiva", 
    "nao consigo começar", "preso no lugar", "imobilizado mental", "trava pra agir", "corpo nao obedece", 
    "mente travada", "sem impulsão", "parado sem conseguir sair", "disfunção executiva", "paralisia de análise", 
    "incapacidade de ação", "travado no lugar", "sem conseguir começar", "bloqueio executivo", 
    "motor mental travado", "não consigo mover", "inerçia", "executiva travada", "sem arranque mental", 
    "inerc", "n consigo começar", "n consigo levntar", "preso no sf", "procrastinnd", "travad", "sem arrnque", 
    "inercia dms", "executiva off", "muro invisivel dms", "inervia", "inerxia", "peeso no sofa", "travadi", 
    "n consigofazer", "estar com as mãos atadas", "atolar na tarefa", "estar empacado", "nadar no seco", 
    "não sair do zero", "estar preso em areia movediça", "motor que não pega", "ficar em banho-maria", 
    "estar de braços cruzados contra a vontade", "empurrar com a barriga", "travado na largada", 
    "muro de concreto invisível", "vontade travada", "não consigo mudar de aba", "dificuldade de trocar o disco", 
    "looping", "preso no celular", "rolagem infinita", "hipnotizado pela tela", "quero ir mas n vo", 
    "socorro n consigo começar", "querendo mas o corpo não responde"
],
       
        "BURNOUT": [
    "fim da linha", "acabou a bateria", "morto por dentro", "peso de mil toneladas", "sem alma", 
    "exaustao cronica", "colapso", "nao tenho forca para o basico", "derretido", "esgotado", "pau no sistema", 
    "sem processamento", "anemia de alma", "apagao", "corpo falhando", "cinzas", "sem motivacao biologica", 
    "colapso funcional", "incapaz de processar um oi", "alma drenada", "bateria viciada", "corpo sem resposta", 
    "desanimo organico", "fim de ciclo", "acabado", "sem vida", "esgotamento", "queimado", "fundo do poco", 
    "sem rumo", "zero energia", "corpo desligando", "mente queimada", "burnout", "esgotado mentalmente", 
    "exaurido total", "sem pilhas", "pifado", "pifou", "bernout", "esgotamento total", "estafa", 
    "fim de energia", "corpo pifado", "mente morta", "totalmente esgotado", "exaustao extrema", 
    "sem alma nenhuma", "morto de cansaço", "esgotamento profissional", "colapso mental", 
    "bateria social no zero", "drenado", "mente exausta", "burnoutt", "esgotado de tudo", "fim da energia total", 
    "corpo e mente mortos", "sem processamento algum", "derretidissimo", "brnout", "bornout", "burnot", 
    "fim d linha", "esgotad", "esgotdo", "sem bat", "bat no zero", "esgotamento dms", "burnout d+", "pifad", 
    "morri p dentro", "burnour", "burnoutr", "burnoht", "esgotqdo", "exaustao total", "estar no limite", 
    "chegar ao fundo do poço", "estar seco por dentro", "ser uma casca vazia", "jogar a toalha", 
    "estar nas últimas", "estar no bico da chaleira", "ser um farrapo humano", "não ter onde cair morto", 
    "alma no lixo", "esgotar a fonte", "corpo em cinzas", "bateria não carrega", "acordar cansado", 
    "sono que não descansa", "intolerância a tarefas", "vazio de energia", "não consigo ler uma frase", 
    "cérebro cozido", "dificuldade de raciocínio básico", "to morto", "n aguento + nada", "acabou td", "burnou"
],
       
       "RSD": [
    "ele me odeia", "falei errado", "mico", "me acham estranho", "rejeitado", "excluido", "dor de critica", 
    "querendo sumir de vergonha", "humilhacao", "sentindo-se um peso", "ferida social", "alma exposta", 
    "peito aberto", "dor de julgamento", "dor fisica de vergonha", "queimacao no peito social", 
    "obsessao pelo erro cometido", "rejeicao fisica", "pontada no coracao social", "vontade de se esconder", 
    "dor de reprovacao", "rejeicao", "vergonha", "me acham chato", "falei bosta", "ninguem gosta de mim", 
    "sou um estorvo", "sou um peso", "me olharam torto", "falei merda", "querendo cavar um buraco", 
    "sentindo-se mal por falar", "erro social", "julgamento", "critica doeu", "sentimento de exclusao", 
    "rsd", "disforia de rejeição", "me sentindo rejeitado", "vergonha extrema", "me acham ridículo", 
    "todo world me odeia", "falei besteira", "rejeição social", "hipersensibilidade à crítica", 
    "disforia sensível", "dor de ser excluído", "ferida emocional social", "rejeisao", "vergonha social", 
    "me odeiam", "falei errado de novo", "critica me matou", "sentindo um lixo social", "rsd dms", 
    "rejeitad", "excluid", "vergonh", "m acham chato", "m odeiam", "falei bst", "rsd d+", "dor de julgamento dms", 
    "rsx", "rsc", "regeisao", "me acham estrrnho", "falei erado", "levar um balde de água fria", 
    "ficar com a cara no chão", "sentir uma facada no peito", "vontade de sumir do mapa", 
    "ficar com o filme queimado", "ser a ovelha negra", "sentir que pisaram em mim", "ficar pequeno de vergonha", 
    "ser o patinho feio", "sentir que sou um estorvo", "falar para as paredes", "estar sobrando", 
    "remoendo", "looping do que eu disse", "analisando a conversa", "por que eu falei aquilo?", 
    "agonia pós-conversa", "flashback de erro social", "calor subindo", "choque de vergonha", 
    "todo mundo rindo", "socorro q vergonha"
],
       
        "TRISTEZA": [
    "no na garganta", "vontade de chorar", "choro preso", "peito apertado", "triste", "melancolia", "solucando", 
    "desanimado", "baixo astral", "nuvem cinza", "coracao pesado", "vazio de tristeza", "luto", "tristeza funda", 
    "corpo sem osso", "vontade de ficar no quarto", "peso no coracao", "amargura", "falta de cor no dia", 
    "dor na alma", "peito oco de dor", "alma cinzenta", "peso emocional", "tristeza", "angustia", "chorando", 
    "infeliz", "pra baixo", "desolado", "sem alegria", "deprimido", "tristeza profunda", "tristi", 
    "vontade de chora", "coracao doendo", "alma triste", "tristesa", "angustya", "angusta", "tristee", 
    "angustia profunda", "muito triste", "vontade de choraar", "melancolico", "coraçao doendo", "alma vazia", 
    "tristezaa", "depressão", "desolação", "estado melancólico", "angustia no peito", "vazio profundo de tristeza", 
    "tristesza", "chorando muito", "coracao partido", "tristesa profunda", "angustiaa", "muita tristeza", 
    "sem chao de tristeza", "trist", "angstia", "vntd d chorar", "triste dms", "angustia d+", "chorand", 
    "tristez", "choro preso dms", "teisteza", "trisreza", "tristrza", "tristeza profunda dms", "angustu", 
    "estar na fossa", "coração partido", "estar com a alma lavada de choro", "viver um mar de rosas murchas", 
    "alma em frangalhos", "chorar as pitangas", "céu de chumbo", "estar com o coração apertado", "vida sem cor", 
    "sentir um vazio imenso", "ficar de luto pela vida", "estar na pior", "baixa astralidade", "olho marejado", 
    "soluço preso", "vontade de sumir debaixo do cobertor", "cansaço de chorar", "tristezzza", "queria chorar", 
    "choro vindo", "n aguento + essa dor", "dia cinza", "vontade de nada"
],
       
        "AFETO": [
    "coracao quente", "borboletas no estomago", "querer abracar", "carinho", "ternura", "admiracao", "saudade boa", 
    "conexao", "querido", "acolhido", "quentinho", "paz no peito", "derretendo de amor", "sorriso bobo", 
    "corpo relaxado", "vontade de cuidar", "peito expandindo", "vibracao suave", "calor interno", "pele relaxada", 
    "seguranca fisica", "conforto no abraco", "batimento calmo", "amor", "amado", "gostando", "apaixonado", 
    "querer bem", "coracao leve", "afeto", "amizade", "abraço", "abracinho", "sentindo-se amado", "coracao bobo", 
    "paz", "carinhoso", "quentinho no coracao", "amoo", "muito amor", "carinhoso dms", "coração quentinho", 
    "querer abraçar", "amizade pura", "afetivo", "amorzinho", "querido dms", "carinho fisico", "conexão emocional", 
    "sentimento de pertença", "adoracao", "afetividade", "amorzão", "muito carinho", "coraçao quente", 
    "amado demais", "quentinho na alma", "amr", "carinh", "vntd d abraçar", "coracao leve dms", "amado d+", 
    "afeto dms", "querid", "amoor", "amo", "amlr", "amoe", "amir", "carunho", "carinhosoa", "amadooo", "queridoo", 
    "estar nas nuvens", "ser o porto seguro", "encher o peito de alegria", "viver um conto de fadas", 
    "ter o coração mole", "ser unha e carne", "ficar caidinho", "amor à primeira vista", "estar no céu", 
    "chamego", "carinho na alma", "sentir-se em casa", "vontade de esmagar de amor", "pressão boa", 
    "conforto tátil", "brilho no olhar", "banho de sol interno", "músculos soltos", "iti malia", "fofura", 
    "aaaamo", "meu dengo", "coração pulsando em paz"
],
       
        "HIPERFOCO": [
    "obcecado", "eletrizado", "nao consigo parar", "viciado na tarefa", "eureka", "brilhante", "energy alta", 
    "uhu", "venci", "animado", "entusiasmado", "modo tunel", "vidrado", "focado", "pilhado", "acelerado", 
    "hiperestimulado", "corpo vibrando", "nao piscar", "flow", "mente a mil", "dopamina", "efervescencia", 
    "sem sono de empolgacao", "foco total", "perda da nocao de tempo", "ligado no 220v", "vibracao nas maos", 
    "visao focada", "pulso vibrante", "mente acelerada", "hiperfoco", "focado demais", "empolgado", "nao paro", 
    "fissurado", "vidrado na tarefa", "foco maximo", "muito animado", "eletrico", "ligado", "mente voando", 
    "fluxo total", "hiper foco", "iperfoco", "vidradao", "muito loko", "hiper-foco", "animadissimo", 
    "focado total", "mente a mil por hora", "dopamina pura", "flow total", "vibraçao forte", "vidradaum", 
    "obsessão produtiva", "estado de fluxo", "excitação extrema", "focado dms", "super animado", "hiper-focado", 
    "eletrizada", "focadaço", "mente a milhao", "empolgação total", "hperfoco", "focad", "animad", "pilhad", 
    "foco total dms", "eletric", "mente a mil d+", "hiper foco dms", "hiperfoco d+", "hiperfoc", "hiperfoxo", 
    "hipergicp", "focadp", "pilhadp", "anomado", "estar a mil por hora", "ficar com a mente fervilhando", 
    "mergulhar de cabeça", "ficar cego para o mundo", "estar no fluxo", "ser uma máquina", 
    "estar com sangue nos olhos", "ficar ligado na tomada", "fogo nas vendas", "ir com tudo", 
    "não tirar os olhos", "estar na zona", "mente em alta rotação", "que horas são?", "esqueci do mundo", 
    "não sinto o corpo", "só mais um minuto", "modo turbo", "euforia de criação", "focadissimo", "boraaaa"
],
       
       "RAIVA": [
    "odio", "mandibula presa", "punhos fechados", "calor subindo", "irritado", "bravo", "furioso", "querendo gritar", 
    "sangue quente", "indignacao", "fervendo", "querendo rosnar", "explosivo", "pelos em pe", "ombros tensos", 
    "dentes trincados", "respiracao pesada", "veia saltando", "vontade de socar", "irritabilidade", "corpo rigido", 
    "olhar fixo de raiva", "maos fechadas", "calor no pescoco", "respiracao ofegante", "impaciencia fisica", 
    "vontade de xingar", "ódio", "raiva", "irritada", "furiosidade", "brabeza", "querendo bater", "nervoso", 
    "nervoso demais", "odio mortal", "puto", "puto da vida", "com raiva", "mordendo os dentes", "trincado", 
    "braveza", "raivaa", "odioo", "irritadissimo", "querendo socar tudo", "fervendo de raiva", "bravo dms", 
    "putasso", "puto dms", "fúria", "colera", "ira", "irritabilidade extrema", "com ódio", "brava", "muito bravo", 
    "nervosíssimo", "raiva visceral", "braveza total", "puto da vvida", "odinho", "raiv", "odi", "irritad", 
    "put d vida", "raiva dms", "odio d+", "bravo d+", "raivaa", "raov", "raia", "rsiva", "pito", "putp", 
    "putoo", "irratado", "irritsdo", "furiozo", "soltar fogo pelas ventas", "estar com a faca nos dentes", 
    "ficar com sangue quente", "virar o bicho", "estar com a macaca", "subir o sangue", "ficar com a gota", 
    "estar possesso", "trincar os dentes", "fechar o tempo", "roer as unhas de raiva", "estar com o diabo no corpo", 
    "ficar de bico", "ficar com o cão", "irritabilidade tátil", "paciência zero", "corpo em alerta", "tensão de contenção", 
    "não me olha", "para de falar", "ouvindo o sangue pulsar", "querendo morder o ar", "vontade de chacoalhar", 
    "pescoço travado", "mãos em garra", "pulso firme demais", "rosto rígido", "pqp", "vsf", "merdaaa", "q raiva"
],
       
        "CONFUSÃO": [
    "nao entendi", "confuso", "perdido", "embaralhado", "muita coisa", "cerebro frito", "muitos dados", 
    "labirinto mental", "sem logica", "travado no erro", "cabeca pesada", "chiado mental", "emaranhado", 
    "inputs demais", "excesso de informacao", "curto circuito no cerebro", "pensamento atropelado", 
    "incapaz de decidir", "nevoa mental", "brain fog", "ruido mental", "nao saquei", "entendi nada", 
    "baguncado", "mente zoneada", "tudo misturado", "muita info", "confusao", "sobrecarga", "nao processa", 
    "falha mental", "mente cheia", "cabeca dando tilt", "tiltou", "tiltou o cerebro", "overload cognitivo", 
    "confusaum", "tudo bagunçado", "muito dado", "mente confusa", "nao entendi nada", "perdidaço", "tiltouu", 
    "desorientação", "caos mental", "desorientado", "embaralhado dms", "mente bagunçada", "confuzao", 
    "nao procesa", "muita coisa na cabeca", "cerebro frito dms", "confuso total", "perdidasso", "confus", 
    "entendi nd", "n entendi nd", "n saquei nd", "bagunçd", "muita info dms", "confusao d+", "sobrecarga dms", 
    "tiltad", "confsuo", "confuao", "comfuso", "confuzo", "embaralhaso", "perdidi", "perdido dms", 
    "estar com a cabeça nas nuvens", "não saber onde se enfiar", "ficar com a cabeça fervendo", 
    "dar um nó no juízo", "estar em um beco sem saída", "não falar lé com cré", "ficar boiando", 
    "estar no mato sem cachorro", "perder a bússola", "estar com o tico e teco brigando", 
    "confuso igual cego em tiroteio", "dar um nó no cérebro", "engasgo mental", "processamento lento", 
    "muita aba aberta", "informação picada", "qual eu escolho?", "não sei por onde começar", "muitas opções", 
    "paralisia de escolha", "zumbido de informação", "rádio fora de sintonia", "chiado no pensamento", 
    "pensamento cortado", "n entendi", "comfuzao", "perdi o fio", "socorro mta coisa"
],
       
       "MEDO": [
    "frio na barriga", "incerto", "vigilante", "receio", "assustado", "pe atras", "com medo", "vulneravel", 
    "ameacado", "arrepio na espinha", "sensacao de perigo", "corpo alerta", "instinto de fuga", 
    "querendo se esconder", "olhando para os lados", "apreensivo", "coracao na boca", "instinto de preservacao", 
    "vigilancia constante", "musculos prontos para correr", "medo", "assustada", "inseguro", "com medo de algo", 
    "preocupado", "vontade de fugir", "alerta", "perigo", "sentindo medo", "receioso", "cagaco", "medinho", 
    "assustadissimo", "medoo", "medo constante", "perigo iminente", "com mto medo", "assustadissima", 
    "medo de tudo", "receioso dms", "insegurançaa", "medo de falhar", "pavor", "temor", "insegurança profunda", 
    "apreensividade", "vulnerabilidade", "com muinto medo", "ameaçado", "instinto de defesa", 
    "medo de que algo aconteça", "perigo total", "medo extremo", "inseguroo", "med", "recei", "com md", 
    "assustd", "preocupad", "medo dms", "inseguro d+", "medr", "meso", "mexo", "mwd", "assuatado", 
    "assustadi", "peeeigo", "perigoo", "receuoso", "ficar com o coração na mão", "estar com o rabo entre as pernas", 
    "sentir o sangue gelar", "ficar de cabelo em pé", "estar com a pulga atrás da orelha", 
    "tremer feito vara verde", "estar pisando em ovos", "sentir o estômago na garganta", "morrer de medo", 
    "ficar branco de susto", "sentir o calafrio da morte", "estado de vigília", "corpo em prontidão", 
    "sensação de ser observado", "medo de falar bobagem", "receio de incomodar", "travado pela dúvida", 
    "pisando em ovos social", "audição aguçada", "qualquer barulho assusta", "tensão na nuca", "olhar inquieto", 
    "mdo", "assustad", "q medo", "socorro medo"
],
       
        "ECOLALIA": [
    "repetindo", "frase na cabeca", "musica chiclete", "eco", "palavra viciante", "looping mental", 
    "estimulacao sonora", "vicio de fala", "repeticao verbal", "ecolalia", "sons repetidos", 
    "necessidade de repetir", "frase viciosa", "palatabilidade de palavras", "eco mental", "ecoando", 
    "repetindo frase", "palavra na mente", "repeticao", "frase que nao sai", "musica repetindo", 
    "eco de palavras", "ecoando na cabeca", "ecolalya", "repetindo sons", "fala repetida", "looping de fala", 
    "viciado na palavra", "repetindo dms", "musica chicletee", "repetição vocal", "ecoando dms", 
    "fala em looping", "repetição constante", "repetindo frases", "eco vocal", "estereotipia verbal", 
    "ecolalia imediata", "frase em eco", "repetindo som", "palavra repetitiva", "ecolaliaa", "looping de palavra", 
    "repetindo infinitamente", "eco constante", "palavra viciada", "repetind", "ecoand", "repetiç", 
    "ecolalia dms", "frase repetindo d+", "musica repetind", "repetindooo", "repetinso", "repsitindo", 
    "ecolslya", "ecoandp", "parecer um disco furado", "ficar como uma vitrola velha", "ecoar como um sino", 
    "estar em looping", "repetir igual um papagaio", "frase colada no cérebro", "eco que não para", 
    "mente repetidora", "ser uma repetição sem fim", "textura da palavra", "estímulo vocal", 
    "brincando com o som", "frase de filme", "scripting", "falando igual ao personagem", 
    "repetindo o que ouvi", "alívio de repetir", "preciso falar isso de novo", "som que encaixa", 
    "massagem vocal", "repete repete", "loopinggg", "palavra palavra palavra", "n sai da cabeça"
],
       
        "MAL_ESTAR": [
    "enjoo", "nausea", "tontura", "dor no corpo", "latejando", "pontada", "mal estar", "indisposto", 
    "corpo estranho", "instabilidade", "vontade de vomitar", "pressao baixa", "corpo mole", 
    "pontadas nas costas", "musculos doendo", "vomito", "dor visceral", "sensacao de doenca", 
    "corpo pedindo pausa fisica", "desconforto gastrico", "mal-estar", "enjoado", "sentindo mal", 
    "corpo ruim", "doente", "vontade de deitar", "fisicamente mal", "indisposicao", "enjo", "nauseas", 
    "corpo moído", "mal estar fisico", "tonto", "tontura forte", "mau-estar", "enjoado dms", 
    "sentindo-se doente", "corpo fraco", "nauseas fortes", "sentindo mal fisico", "indisposto dms", 
    "enjou", "vomitoo", "disfunção física", "desconforto somático", "corpo instável", "mal estar geral", 
    "sentindo-se mal", "corpo doendo muito", "enjoo forte", "nausea extrema", "tontura constante", 
    "mal-estarzão", "corpo ruim dms", "corpo pedindo arrego", "nause", "tontur", "mal estr", "mal estar dms", 
    "enjoado d+", "tonto dms", "indispost", "enjoo dms", "enjoio", "enjjo", "tonturs", "tonturaa", 
    "mal-estat", "indisposyo", "vomitp", "estar no bagaço", "estar no pó da rabiola", 
    "sentir-se como se um trator tivesse passado por cima", "estar mal das pernas", "virado do avesso", 
    "estar com o corpo moído", "sentir-se um trapo", "estar para lá de Bagdá", "corpo fora do eixo", 
    "sentir a vida pesando no corpo", "estar em frangalhos físicos", "boca seca", "dor de cabeça latejante", 
    "visão escurecendo ao levantar", "vazio que dói", "estômago revirado", "peso nos olhos", "corpo de chumbo", 
    "gravidade mais forte", "membros pesados", "vontade de fechar os olhos", "mto mal", "enjoadaa", "tontu", 
    "n consig levntar"
],
       
       "DOR_DE_CABEÇA": [
    "pressao nos olhos", "cabeca explodindo", "pulsacao na tempora", "luz doi", "martelada", "agulhada na cabeca", 
    "cerebro pulsando", "peso na testa", "pontada no olho", "enxaqueca", "cabeca latejando", "nausea de dor", 
    "dor na nuca", "pontadas cranianas", "visao com aura", "dor de cabeça", "dor de cabeca", "do de cabca", 
    "dor di cabela", "dor de babeca", "cabeca doendo", "dor na cabeca", "enxaqueca forte", "cabeca pesada", 
    "dor nos olhos", "martelando na cabeca", "cabeca pulsando", "dor de cabesa", "dor di cabeça", "do d cabeca", 
    "dor de cabeçaa", "cabeca explodindo de dor", "enxaquecaa", "pressão na cabeça", "pulsando dms", "dor na testa", 
    "dores de cabeça", "cabeça doendo muito", "cefaléia", "migrânea", "dor craniana", "pressão intracraniana", 
    "pulsatilidade na cabeça", "cabeca martelando", "dor de cabeca dms", "enxaqueca braba", 
    "cabeca explodindo total", "dor de cabeca infernal", "do d cabesa", "dor de cabç", "dr de cabeca", 
    "cabeca doend", "enxaquec", "dor de cabeca d+", "enxaqueca dms", "dor d cab", "dor d cabc", "dor de cabaca", 
    "dor de cabexa", "cabeca doebdo", "dor na cabesa", "enxqueca", "parece que tem um carpinteiro na minha cabeça", 
    "cabeça vai rachar", "martelada constante", "pressão de mil atmosferas", "sentir o cérebro pulsar", 
    "dor que cega", "cabeça de chumbo", "estar com a cabeça em brasas", "cérebro sendo esmagado", 
    "luz que corta a cabeça", "martelada interna", "mancha na visão", "pontos brilhantes", "visão quadriculada", 
    "dor na base do crânio", "pescoço de pedra", "dor de tela", "muito tempo de monitor", "cheiro que dá dor", 
    "barulho que fura o cérebro", "náusea de luz", "dr d cabeca", "cabecaaa", "n aguento a luz", "socorro cabeca"
],
       "NOJO": [
    "nojo", "ascom", "ecat", "repugnante", "gosmento", "textura ruim", "cheiro de podre", "nausea sensorial", 
    "arrepio de nojo", "vontade de cuspir", "pele arrepiada de asco", "repulsa fisica", "garganta fechando de nojo", 
    "vontade de lavar a mao", "nojo total", "nojento", "eca", "credo", "textura estranha", "vontade de vomitar de nojo", 
    "aversao", "asco", "repulsa", "que nojo", "cheiro ruim de nojo", "nojo de toque", "ecat", "nojinhu", "gosma", 
    "nojoo", "ecati", "aversaum", "nojento dms", "repulsa total", "textura nojenta", "gosmento dms", "repugnancia", 
    "asco total", "repulsa sensorial", "aversão física", "ojiza", "repugnância", "nojo de texture", "que nojooo", 
    "nojento dmais", "aversao total", "vontade de vomitar nojo", "cheiro de podridão", "repulsa visceral", "noj", 
    "asc", "nojent", "repulsa dms", "nojo d+", "aversao dms", "nojentooo", "nojinho dms", "nojento d+", "mojo", 
    "molo", "nojentoa", "nojewnto", "nojebto", "ecaaa", "embrulhar o estômago", "ficar com os pelos arrepiados", 
    "sentir o estômago dar um nó", "dar ânsia de vômito", "ficar com o estômago embrulhado", "virar o nariz", 
    "sentir ojeriza", "querer distância", "sentir nojo até da alma", "ter asco", "cheiro de morte", "textura de lama", 
    "ânsia de toque", "repulsa por textura", "aversão a cheiro", "comida estranha", "textura de pano", "mão suja", 
    "coisa grudenta", "cheiro de gordura", "barulho de chiclete", "preciso lavar", "tira isso de perto", 
    "não encosta", "sensação de sujeira", "n aguento esse cheiro", "coisa nojenta", "eca dms"
],
       
       "CURIOSIDADE": [
    "quero saber", "como funciona", "interessado", "pesquisando", "instigado", "descobrir", "investigando", 
    "cacador de dados", "fome de saber", "explorando", "mente aberta", "busca de padrao", "curioso", 
    "querendo entender", "interessada", "buscando info", "como e", "porque", "querendo descobrir", 
    "curiosidade", "buscando saber", "fome de dados", "instigada", "pesquisador", "investigador", 
    "querendo saber dms", "muito curioso", "interessadissimo", "investigando tudo", "caçador de info", 
    "querendo entender tudo", "curiosidadee", "interesse analítico", "investigação", "desejo de aprender", 
    "instigação", "querendo saber o porque", "exploração mental", "curiosidade total", "interessado dms", 
    "buscando padroes", "investigador de dados", "fome de conhecimento", "curiosid", "quero sbr", 
    "como func", "interessad", "curioso dms", "curiosidade d+", "querendo sbr dms", "interessadissimo dms", 
    "pesquisand", "curiozo", "curiso", "interessaso", "investiganso", "meter o nariz", 
    "querer saber até onde a coruja dorme", "desvendar o mistério", "ir fundo na questão", "caçador de pistas", 
    "estar sedento por respostas", "não sossegar enquanto não descobrir", "mente de detetive", 
    "querer ver com que olhos", "descobrir o X da questão", "mente de cientista", "modo detetive", 
    "querendo as peças do quebra-cabeça", "catalogando", "conectando os pontos", "buscando a lógica", 
    "como isso se encaixa?", "vontade de testar", "e se...?", "abrindo o capô", "desmontando a ideia", 
    "mta aba aberta", "preciso entender isso", "achei uma coisa", "olha que foda"
],
       
        "STIMMING": [
    "balancando", "maos agitadas", "girando", "maos balancando", "flapping", "pulando", "batendo o pe", 
    "mexendo no cabelo", "mordendo a caneta", "preciso me mexer", "corpo pedindo ritmo", "balanco", 
    "sacudindo", "esfregando as maos", "vocalizando", "apertando as maos", "balancar de cabeca", 
    "necessidade de pressao", "estalando os dedos", "morder os labios", "balancar o tronco", 
    "pressao profunda", "apertar objetos", "stimming", "estimming", "mexendo as maos", "balançando", 
    "ritmo no corpo", "preciso de movimento", "flaping", "flapping de maos", "balanco de corpo", 
    "auto estimulacao", "mexendo muito", "stiming", "maos balançando", "preciso de estimulo", 
    "stimming dms", "balanço constante", "auto-estimulação", "movimento repetitivo", "flaping de mãos", 
    "autorregulação sensorial", "estereotipias motoras", "busca sensorial", "preciso de stim", 
    "movimento de autorregulação", "stimming constante", "mexendo o corpo", "preciso me balançar", 
    "ritmo corporal", "balancando muito", "auto-estimulacao", "stim", "stimm", "balancand", 
    "preciso d movmnt", "stimmung", "stiminh", "balancandp", "balancandoo", "flappingg", "balancando dms", 
    "estar em transe motor", "corpo em balanço", "mãos que voam", "necessidade de sentir o ritmo", 
    "corpo que dança sozinho", "ficar no seu balanço", "sentir o corpo no espaço", "mãos inquietas", 
    "ficar em paz no movimento", "ritmo de proteção", "sentir a pressão do mundo", "marcha de regulação", 
    "movimento rítmico", "dança dos dedos", "cheirar as mãos", "olhar as luzes", "textura do teclado", 
    "som repetitivo", "pressão nas juntas", "esmagamento bom", "peso nas pernas", "abraço de urso", 
    "casulo", "cobertor pesado", "stimmm", "balançandooo", "flappp", "preciso de pressão"
],
       
       "FRUSTRAÇÃO": [
    "nao funcionou", "erro 404", "deu errado", "vontade de desistir", "irritado com erro", "output invalido", 
    "travado no problema", "indignado", "insucesso", "impaciencia", "frustrado", "falha no codigo", 
    "expectativa quebrada", "nao sai do lugar", "vontade de largar tudo", "frustracao", "nao deu certo", 
    "merda de erro", "erro no sistema", "falhou", "nao vai", "vontade de jogar tudo pro alto", "deu ruim", 
    "falha", "insatisfeito", "erro fatal", "que odio de erro", "nao ta indo", "travado", "frustraçaoo", 
    "deu errado dms", "frustradissimo", "nao funciona nada", "erro chato", "falhou dms", "frustração extrema", 
    "insucesso total", "desapontamento", "frustraçao braba", "deu tudo errado", "nao funcionou nada", 
    "erro de processamento", "frustraçao total", "frustaçao", "frustasao", "frust", "n funcionou", 
    "n deu certo", "deu r", "frustrad", "erro d sistm", "frustracao dms", "frustrado d+", "frustado", 
    "frustadao", "frustraçaoo", "deu erraso", "nao funcionpu", "frustradp", "frustrasaoo", 
    "dar murro em ponta de faca", "ficar a ver navios", "quebrar a cara", "perder a paciência", "estar por aqui", 
    "sentir o mundo contra mim", "dar com a cara no muro", "nadar, nadar e morrer na praia", 
    "ficar de mãos abanando", "vontade de chutar o balde", "estar no limite da paciência", 
    "frustração de código", "bloqueio de progresso", "vontade de resetar", "impaciência com o processo", 
    "objetivo travado", "bug que não sai", "lógica quebrada", "syntax error na vida", "loop infinito de erro", 
    "VS Code me odeia", "vontade de fechar o notebook", "preciso de um reboot", "vou apagar tudo", 
    "nada faz sentido no código", "afff", "q raiva d erro", "n vaaaai", "erro dms", "desisto hj"
],
       
       "INJUSTIÇA": [
    "absurdo", "antietico", "injusto", "quebra de logica", "erro de conduta", "revoltado", "quebra de expectativa", 
    "falta de criterio", "injustica", "violacao de protocolo", "indignacao moral", "nao e justo", "erro de admin", 
    "falha de carater externa", "injusto demais", "revolta", "absurdo total", "falta de etica", "quebra de regra", 
    "nao pode ser", "errado", "muito errado", "injusitca", "injustissa", "quebra de confiança", "sem logica moral", 
    "indignado", "injustiçaa", "anti-ético", "quebra de lógicaa", "indignação moral profunda", "totalmente injusto", 
    "erro de ética", "violação de princípios", "injustiça ética", "moralmente errado", "falta de justiça", 
    "injusto dms", "absurdo completo", "revoltado total", "sem ética alguma", "erro de justiça", "injustisça", 
    "injustiçaa", "injust", "revoltad", "n e justo", "absurd", "injustiça dms", "injusto d+", "injustisa", 
    "injustisaa", "absuado", "revoltqdo", "injusto dms total", "injustissq", "isso é um absurdo", 
    "ser passado para trás", "fazer de bobo", "estar com a razão e ser ignorado", "pisar na bola comigo", 
    "falta de caráter", "jogar sujo", "estar sendo injustiçado", "ser o bode expiatório", "fazer papel de palhaço", 
    "isso não se faz", "quebra de valores", "injustiça moral", "furo no protocolo", "lógica moral quebrada", 
    "erro de critério", "desigualdade", "não é o combinado", "quebra de acordo", "mudança de regra sem aviso", 
    "falta de transparência", "cadê a lógica nisso?", "ninguém me ouve", "fatos ignorados", 
    "mentira na minha frente", "conivência com erro", "absurdooo", "n aceito isso", "errado dms", "q injustiça"
],
       
       "SOLIDAO": [
    "sozinho", "isolado", "sem conexao", "servidor unico", "falta de troca", "invisivel", "sem ninguem para falar", 
    "vazio social", "desconectado de humanos", "solitario", "falta de pacotes sociais", "isolamento forcado", 
    "sem par", "solidao", "sozinho no mundo", "sem amigos", "isolado de tudo", "solitaria", "sem contato", 
    "vazio de gente", "necessidade social", "sem conversa", "sozinho total", "solidaoo", "solidao profunda", 
    "sozinhoo", "isoladissimo", "sem ninguém", "vazio social dms", "solitário dms", "isolamento total", 
    "falta de companhia", "sozinho de tudo", "desconexão social", "vazio interpessoal", "sentimento de isolamento", 
    "solidão extrema", "sem ninguem mesmo", "isolado do mundo", "vazio social total", "sem par social", 
    "sozinho de verdade", "sozinh", "isolad", "solitari", "solidao dms", "sozinho d+", "isolado dms", 
    "sozinhoo", "sozimho", "solidaom", "solidsao", "solidaooo", "sozinnho", "sozinhoo dms", "estar ao léu", 
    "sentir-se um deserto", "sozinho como um dedo", "estar na solidão da noite", "sem um ombro amigo", 
    "falar com as paredes", "invisibilidade social", "solidão que dói", "ser o único no mundo", 
    "solidão absoluta", "isolado no seu universo", "servidor offline", "ping sem resposta", "timeout social", 
    "tentativa de conexão falha", "firewall entre pessoas", "sozinho na multidão", "falar e ninguém ouvir", 
    "idioma diferente", "sem tradutor emocional", "falha de conexão social", "desejo de troca", 
    "solidão de entendimento", "necessidade de ser visto", "mto sozinho", "n tenho ninguem", "queria alguem"
],
       
       "NAO_VERBAL": [
    "sem fala", "nao verbal", "silencio_pontos", "voz nao sai", "modulo de audio off", "dificuldade de falar", "palavra some", 
    "fala arrastada", "mudo temporario", "energia para falar zero", "nao quero falar", "comunicacao dificil", 
    "bloqueio de fala", "nao consigo falar", "sem voz", "mudez temporaria", "nao-verbal", "fala bloqueada", 
    "palavras fugiram", "incapaz de falar", "silencio total", "sem comunicacao", "voz sumiu", "nao quero papo", 
    "nao-fala", "modulo off", "sem energia pra falar", "fala travada", "mudo total", "energia vocal zero", 
    "afasia temporária", "bloqueio comunicativo", "vontade de não falar", "mudez de exaustão", 
    "sem palavras para falar", "fala desligada", "bloqueio de voz", "não-verbalidade", "fala off", "mudo agora", 
    "sem condicao de falar", "nao-verbal total", "n verbal", "sem fl", "voz n sai", "mudo dms", "n quero falar", 
    "n verbal total", "fala off dms", "nao-verbl", "nao-verball", "nao-verbak", "sem dalar", "n verbal dms", 
    "ficar com a língua travada", "as palavras sumiram", "ficar mudo igual um peixe", 
    "voz que não atravessa a garganta", "bloqueio total de comunicação", "não sai nada", 
    "estar em mudez seletiva por cansaço", "erro de driver de voz", "falha de saída de áudio", 
    "buffer de fala cheio", "desconexão cérebro-boca", "bateria social em 0%", "muito barulho para falar", 
    "palavras pesam", "falar dói", "quero só escrever", "use meus cards", "leia o que escrevi", 
    "não me peça para explicar agora", "voz off", "mudo", "......."
],
       
       "ORGULHO": [
    "consegui", "venci", "eu fiz", "missao cumprida", "upgrade", "competente", "satisfeito com o codigo", 
    "deploy funcional", "sensacao de dever cumprido", "eu sou bom nisso", "resultado positivo", "orgulho", 
    "deu certo", "conseguido", "vitoria", "sucesso", "funciona", "orgulhoso", "vencedor", "fiz certo", 
    "to bem nisso", "conseguim", "vencim", "funcionouuu", "conseguii", "conseguiii", "vitoriaa", "eu fiz isso", 
    "orgulhoso dms", "sucesso total", "conseguido dms", "missao cumpridaa", "venci dms", "conquista pessoal", 
    "auto-eficácia", "sucesso funcional", "triunfo", "fui bem", "resultado excelente", "consegui mesmo", 
    "orgulho do trabalho", "deploy com sucesso", "venci o desafio", "conseguim total", "eu fiz bem feito", 
    "conseg", "venc", "orgulhos", "sucesso dms", "orgulho d+", "consegui d+", "venci dms", "conseguu", 
    "consequi", "suceso", "orgulhoso dms total", "estar com a alma lavada", "lavar a égua", "ganhar o dia", 
    "estar no topo do mundo", "ser o cara", "mandar bem", "dar um show", "tirar de letra", "acertar na mosca", 
    "matar a cobra e mostrar o pau", "conquista de ouro", "orgulho de mestre", "dever cumprido com louvor", 
    "validação interna", "sistema estável", "competência comprovada", "alinhamento de lógica", 
    "eu entendi o porquê", "aprendizado consolidado", "domínio técnico", "resolvi sozinho", "sem atalhos", 
    "paz de espírito", "corpo relaxado de dever cumprido", "sorriso involuntário", "sensação de progresso", 
    "BOAAAA", "CHUPA MUNDO", "FUNCIONOUUUU", "AEEEE", "SOU FODA"
],
       
        "GRATIDAO": [
    "obrigado", "grato", "agradecido", "sorte", "backup positivo", "valorizar", "reconhecimento", "sentimento bom", 
    "aliviado e grato", "reconhecer o bem", "gratidao", "valeu", "agradecida", "obrigada", "muito grata", "obrigadom", 
    "obrigadao", "reconhecido", "grato por tudo", "obrigadu", "obrigadaaa", "valeu mesmo", "gratidaoo", 
    "agradecidissimo", "obrigadão", "valeu dms", "muito grato", "gratidãum", "gratidãoo", "agradecida dms", 
    "reconhecimento positive", "apreço", "grata total", "obrigadissimo", "valeu de verdade", "agradecido dmais", 
    "muito obrigada", "muito obrigado", "gratidao imensa", "agradecimento profundo", "valeu dms mesmo", 
    "obrigadao total", "gratidaum", "obg", "vlw", "grat", "obrigad", "valeu dms", "gratidao d+", "valeu d+", 
    "obrigadaa", "obg dms", "vlw dms", "valeuu", "obrigadom", "obrigadp", "obrigado dms", "agradescido", 
    "agradeçido", "valru", "agradecer de coração", "estar com a alma grata", "reconhecer o valor", 
    "ser grato até o fim", "dar graças", "gratidão que transborda", "reconhecer a mão amiga", "gratidão infinita", 
    "estar em dívida de carinho", "coração agradecido", "muito obrigado mesmo", "suporte validado", 
    "ajuda processada", "alívio por assistência", "reconhecimento de recurso", "obrigado por explicar", 
    "entendi graças a você", "alívio por sair do erro", "gratidão pelo insight", "ufa, obrigado", 
    "ainda bem que deu certo", "gratidão pelo reset", "obrigado pela paciência", "obgg", "vlwww", 
    "gratidãooo", "sério, vlw", "vlw msm"
],
       
        "PAZ": [
    "homeostase", "silencio", "calma", "equilibrio", "corpo leve", "mente limpa", "sem alertas", "estavel", 
    "baixa latencia", "tranquilidade", "sistema em ordem", "paz", "tranquilo", "zen", "equilibrio total", 
    "corpo em paz", "mente relaxada", "sem estresse", "homeostasi", "sistema ok", "calmaria", "silencio mental", 
    "estabilidade", "corpo calmo", "pazz", "tranquilidadee", "mente limpa dms", "equilíbrio", "homeostase total", 
    "corpo estável", "paz interior", "calmaria total", "equilíbrio fisiológico", "estado de calma", 
    "sistema em harmonia", "estabilidade interna", "paz absoluta", "calmo dms", "mente em paz", 
    "corpo relaxado total", "homeostase perfeita", "tranquilidade absoluta", "equilíbrio mental", "paz total", 
    "homeo", "paz dms", "tranquil", "estavl", "zen dms", "calm", "paz d+", "tudo ok", "tudo cert", 
    "paz total dms", "homeostase dms", "homeostasw", "homeostasee", "pazz", "tranquiloo", "calmo dms total", 
    "estar em águas calmas", "céu de brigadeiro", "corpo em harmonia", "silêncio de ouro", 
    "estar na paz do senhor", "equilíbrio de mestre", "alma lavada e tranquila", "estar zen", "mar de rosas", 
    "viver um dia de cada vez em paz", "estar com a mente em ordem", "paz de espírito", "ruído branco mental", 
    "fluxo contínuo", "frequência estável", "ausência de atrito", "sistema nominal", "CPU em 5%", 
    "sem loops de erro", "memória limpa", "redundância operacional", "respiração automática", 
    "batimento rítmico", "músculos soltos", "conforto térmico", "sensação de encaixe", "paaaaaaz", 
    "tô zen", "uufa"
],
    "VERGONHA": [
    "me sinto mal", "nao devia ter feito", "erro meu", "falha interna", "quebra de protocolo pessoal", 
    "me sinto um lixo", "peso na consciencia", "culpa", "vergonha", "me sinto mal comigo", "autocriticismo", 
    "falei o que nao devia", "fui injusta", "erro de conduta meu", "vergonha de mim", "me sinto pequena", 
    "queria sumir de vergonha", "culpa dms", "vergonha total", "me sinto culpada", "me sinto burra", 
    "como eu pude?", "falha de carater minha", "remorso", "arrependimento", "me sinto mal dms", "culpad", 
    "vergonhad", "culp", "vergonh", "me sinto pessima", "deveria ter sido melhor", "vacilei", "pisei na bola", 
    "vontade de se enterrar", "cara de tacho", "estar com a moral no chão", "sentir o peso do mundo nas costas", 
    "querer enfiar a cabeça num buraco", "estar com a consciência pesada", "erro de execução pessoal", 
    "violação do meu código", "autocrítica feroz", "sentir-se um impostor", "fraude"
],

    "TEDIO": [
    "tedio", "sem nada pra fazer", "ocioso", "mente vazia", "subestimulado", "procurando o que fazer", 
    "falta de desafio", "sem foco", "entediado", "tempo nao passa", "querendo estímulo", "cérebro devagar", 
    "falta de interesse", "nada me prende", "vazio de tarefa", "sem objetivo agora", "tedio dms", 
    "entediado d+", "sem o que processar", "procurando erro por tedio", "querendo dopamina", "vazio cognitivo", 
    "mente inquieta por nada", "falta de input", "subestimulacao", "tedio total", "tedioo", "entediad", 
    "n tem nada", "q preguiça", "sem rumo", "vontade de inventar algo", "dar murro em ponta de faca por tedio", 
    "contar os minutos", "estar a ver navios", "coçar o nariz", "tempo parado", "espera infinita", 
    "falta de lenha pro fogo", "sistema em espera", "idle mode", "procurando sarna pra se coçar"
],

    "VERGONHA_ALHEIA": [
    "que mico", "vergonha por ele", "vergonha por ela", "que absurdo o outro", "desconforto social", 
    "erro de conduta alheio", "nao acredito que fez isso", "situacao constrangedora", "vergonha alheia", 
    "quebra de protocolo social", "sem nocao", "falta de tato", "constrangido pelo outro", "pelo amor de deus", 
    "que mico total", "vergonha alheia dms", "situacao ridicula", "nao sei onde enfiar a cara", 
    "constrangimento", "incomodo social", "falta de etiqueta", "vergonha alheiaa", "mico", "mico dms", 
    "ridiculo", "sem postura", "que vacilo do outro", "vergonha alheria", "micoo", "vergonhaalheia", 
    "n acredito nisso", "q vergonha dele", "q vergonha dela", "ficar com a cara no chão pelo outro", 
    "sentir o sangue subir por causa do outro", "querer desaparecer pela pessoa", "que papelão", 
    "estar no meio de um climão", "sentir ojeriza social", "falta de simetria ética no outro", "erro de sistema alheio"
],
    }

    pontuacao = {}

    for categoria, termos in mapa_sentimentos.items():
        pontos = 0
        for termo in termos:
            # 1. Limpamos o termo do dicionário e o sinal do usuário da MESMA forma
            termo_limpo = normalizar(termo) 
            palavras_do_usuario = sinal.split()

            # --- REGRA 1: TERMO EXATO (3 PONTOS) ---
            # Se o que você digitou é EXATAMENTE o termo (ex: "fome" == "fome")
            if termo_limpo == sinal:
                pontos += 3
            
            # --- REGRA 2: PALAVRA SOLTA NA FRASE (2 PONTOS) ---
            # Se a palavra está "limpa" dentro da sua lista de palavras
            elif termo_limpo in palavras_do_usuario:
                pontos += 2
                
            # --- REGRA 3: PARTE DA PALAVRA (1 PONTO) ---
            # Se o termo está contido no sinal (ex: "fome" dentro de "fomezinha")
            elif termo_limpo in sinal:
                pontos += 1
        if pontos > 0:
            pontuacao[categoria] = pontos

    if not pontuacao:
        return "Sinal Desconhecido"

    # Retorna o sentimento que teve mais palavras correspondentes encontradas
    vencedor = max(pontuacao, key=pontuacao.get)

    # Limpa o nome
    # Remove acentos, tira maiúsculas e troca espaços/barras por underline
    categoria_limpa = normalizar(vencedor).replace(" ", "_")

    return categoria_limpa

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
