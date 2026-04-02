

import customtkinter as ctk # Importa a biblioteca para o visual moderno e Modo Escuro
from datetime import datetime # Importa funções para ler a hora atual do seu computador
import varredura_fisica # Importa o seu módulo que traduz sensações do corpo
import dicionario # Importa o seu módulo com o banco de dados de sentimentos
import sqlite3
from datetime import datetime, timedelta
import motor_logico  # Importa o arquivo de manejo

import teste_manejo
import historico_smars


def centralizar_janela(janela, largura, altura):
    # Pega a largura e altura da tela do seu computador
    largura_tela = janela.winfo_screenwidth()
    altura_tela = janela.winfo_screenheight()

    # Calcula a posição X e Y para o centro
    pos_x = (largura_tela // 2) - (largura // 2)
    pos_y = (altura_tela // 2) - (altura // 2)

    # Define a geometria: "Largura x Altura + PosX + PosY"
    janela.geometry(f"{largura}x{altura}+{pos_x}+{pos_y}")



    # --- CONFIGURAÇÃO VISUAL DO SISTEMA ---
ctk.set_appearance_mode("dark") # Define que o programa rodará sempre em Modo Escuro
ctk.set_default_color_theme("blue") # Define a cor azul como padrão para botões e detalhes



def abrir_explicacao_alexitimia():
    janela_alex = ctk.CTkToplevel()
    janela_alex.title("SMARS - O QUE É ALEXITIMIA?")
    centralizar_janela(janela_alex,650,650)
    janela_alex.attributes("-topmost", True)
    janela_alex.grab_set()

    # 1. BOTÃO PRIMEIRO (side="bottom" reserva o espaço do rodapé antes de tudo)
    btn_voltar = ctk.CTkButton(
        janela_alex, 
        text="COMPREENDIDO", 
        font=("Segoe UI", 14, "bold"),
        fg_color="#1f538d", 
        hover_color="#14375e",
        height=45,
        command=janela_alex.destroy
    )
    btn_voltar.pack(side="bottom", pady=(10, 25))

    # 2. CAIXA DE TEXTO (Ocupa o espaço que sobrar em cima do botão)
    caixa_texto = ctk.CTkTextbox(
        janela_alex, 
        font=("Segoe UI", 16), 
        border_spacing=30,
        fg_color="transparent",
        wrap="word"
    )
    caixa_texto.pack(padx=20, pady=(20, 0), fill="both", expand=True)

    texto_direto = (
        "ALEXITIMIA: A CIÊNCIA E A MEDIAÇÃO POR TRÁS DO SMARS\n"
        "______________________________________________________________\n\n"
        "A Alexitimia — termo derivado do grego 'Alexisthymos' (a = ausência, lexis = palavra, thymos = emoção) — "
        "não é uma descoberta recente, mas um constructo clínico consolidado. \nO termo foi cunhado pelo psiquiatra "
        "Peter Sifneos, de Harvard, em 1973, no artigo 'The prevalence of alexithymic characteristics in psychosomatic patients', "
        "publicado na revista Psychotherapy and Psychosomatics. Sifneos observou que pacientes com doenças psicossomáticas "
        "não possuíam um 'vocabulário de sentimentos', apresentando uma pobreza extrema na fantasia e no pensamento simbólico. "
        "\nNo SMARS, interpretamos essa observação original como uma falha crítica no 'Driver de Tradução': o hardware biológico "
        "dispara o sinal de pulso e tensão perfeitamente, mas o sistema consciente não possui o arquivo de legenda necessário "
        "para converter a biologia em símbolo linguístico.\n\n"
        
        "Cientificamente, essa barreira ocorre por uma disfunção na Interocepção, o oitavo sentido responsável por monitorar "
        "o estado interno do corpo através da Ínsula Anterior. Em indivíduos alexitímicos, há um ruído crônico nessa comunicação. "
        "É o que chamamos no SMARS de 'Telemetria Bruta': o corpo gera dados de voltagem (taquicardia, sudorese, nó na garganta), "
        "mas como a Ínsula não categoriza esses dados, a mente recebe apenas um log de 'Erro Crítico'. Sem a mediação do software, "
        "o indivíduo permanece em um estado de confusão sensorial, incapaz de discernir se o que sente é uma resposta emocional "
        "específica ou apenas um desconforto físico vago, o que frequentemente leva ao esgotamento por falta de regulação.\n\n"
        
        "Aprofundando ainda mais, a neurobiologia aponta para uma redução na conectividade funcional entre o Sistema Límbico "
        "e o Córtex Cingulado Anterior. Na nossa lógica de projeto, é um problema de 'Cabo de Rede Desconectado': o motor emocional "
        "está acelerando no máximo, mas o velocímetro na interface do usuário não recebe a informação. A fiação entre as partes opera "
        "com tamanha latência que a experiênca sentida se perde antes de ser rotulada. \nNo contexto neurodivergente, a 'Teoria do Mundo "
        "Intenso' de Markram e Markram (2007) sugere que o cérebro autista é hiper-reativo; logo, a Alexitimia surge como um "
        "'Modo de Proteção contra Sobrecarga' (Firewall Biológico). O sistema desativa as notificações de sentimento para evitar que "
        "o processador central entre em colapso (Meltdown) diante da intensidade avassaladora do mundo.\n\n"
        
        "A alma do SMARS, entretanto, reside na Pedagogia de Lev Vygotsky. Vygotsky defendia que o desenvolvimento humano é mediado "
        "por instrumentos e signos. O SMARS atua exatamente como um 'Andaime' dentro da Zona de Desenvolvimento Proximal "
        "(ZDP) — a distância entre o que o indivíduo consegue fazer sozinho e o que consegue com ajuda. \nComo o alexitímico não possui "
        "espontaneidade para nomear estados internos, o software fornece a mediação tecnológica (o signo) necessária para a tradução. "
        "Segundo Vygotsky, funções psicológicas superiores aparecem primeiro no plano social (entre pessoas ou entre pessoa e máquina) "
        "para depois serem internalizadas. Assim, ao usar o SMARS, o usuário não está apenas usando um scanner, mas reeducando sua "
        "percepção neural para, no futuro, conquistar sua autonomia emocional e dignidade cognitiva.\n\n"
        
        "REFERÊNCIAS BIBLIOGRÁFICAS:\n"
        "• SIFNEOS, P. E. (1973). The prevalence of 'alexithymic' characteristics in psychosomatic patients. Psychotherapy and Psychosomatics.\n"
        "• VYGOTSKY, L. S. (1978). Mind in Society: The Development of Higher Psychological Processes. Harvard University Press.\n"
        "• BIRD, G.; COOK, R. (2013). Mixed emotions: the contribution of alexithymia to the emotional symptoms of autism.\n"
        "• MARKRAM, H.; MARKRAM, K. (2007). The Intense World Theory – a unifying hypothesis for autism. Frontiers in Human Neuroscience.\n"
        "• HERBERT, B. M.; POLLATOS, O. (2012). The Relevance of Interoception in Clinical Disorders. Frontiers in Psychology."    
    )

    caixa_texto.insert("0.0", texto_direto)
    caixa_texto.configure(state="disabled")

def abrir_conceito():
    janela = ctk.CTkToplevel()
    janela.title("SMARS - O QUE SÃO SENTIMENTOS?")
    centralizar_janela(janela,650,650) 
    janela.attributes("-topmost", True)
    janela.grab_set()

    # Botão no fundo primeiro
    btn_sair = ctk.CTkButton(
        janela, 
        text="COMPREENDIDO", 
        font=("Segoe UI", 14, "bold"),
        fg_color="#1f538d", 
        hover_color="#14375e",
        height=45,
        command=janela.destroy
    )
    btn_sair.pack(side="bottom", pady=(10, 25))

    caixa_texto = ctk.CTkTextbox(
        janela, 
        font=("Segoe UI", 16), 
        border_spacing=35,
        fg_color="transparent",
        wrap="word"
    )
    caixa_texto.pack(padx=20, pady=(20, 0), fill="both", expand=True)

    texto_direto = (
        "O QUE SÃO SENTIMENTOS? \nUMA PERSPECTIVA NEUROBIOLÓGICA E COGNITIVA\n"
        "______________________________________________________________\n\n"
        "Cientificamente, o sentimento não é um evento isolado, mas o estágio final de um processo "
        "biológico complexo que visa a manutenção da vida. \nTudo começa com a Homeostase, o esforço do "
        "organismo para manter o equilíbrio interno. Através da Interocepção, o sistema nervoso monitora "
        "constantemente o estado dos órgãos e tecidos. \nQuando um estímulo externo ou interno ocorre, "
        "o corpo dispara uma Emoção — que, segundo António Damásio, é um conjunto de respostas químicas "
        "e neurais automáticas e universais. Essas respostas ocorrem no Sistema Límbico, especificamente "
        "na Amígdala, gerando alterações físicas imediatas como aceleração cardíaca, sudorese e tensão "
        "muscular, antes mesmo de qualquer percepção consciente.\n\n"
        "No ecossistema do SMARS, interpretamos essa cadeia biológica através da lógica de sistemas. "
        "As sensações físicas são a nossa 'Telemetria Bruta de Hardware': dados puros vindos de sensores "
        "periféricos informando sobre a voltagem e o status do organismo. \nAs emoções, por sua vez, são "
        "vistas como 'Protocolos de Segurança' ou scripts de execução rápida, desenhados para proteger "
        "a integridade do sistema operacional humano em situações de risco ou recompensa. \nO Sentimento "
        "surge, portanto, como o 'Relatório Processado pela CPU Central' (a mente consciente). Ele é a "
        "tradução semântica da pergunta: 'Por que meu hardware está agindo assim agora?'. É o momento "
        "em que o Córtex Pré-Frontal associa a eletricidade da emoção a um contexto, transformando a "
        "reação química em experiênca subjetiva e nomeável.\n\n"
        "Aprofundando na neurociência da consciência, esse processo de tradução depende da integridade "
        "funcional de áreas como a Ínsula Anterior e o Córtex Cingulado Posterior. A Teoria da Avaliação "
        "Cognitiva (Appraisal Theory) postula que o sentimento depende de como o cérebro avalia o estímulo. "
        "\nNa Alexitimia, ocorre um Erro de Driver crítico: há uma desconexão ou latência entre a leitura do "
        "corpo e a área de processamento de símbolos e linguagem. O hardware está 'quente' e os protocolos "
        "de emergência estão rodando em segundo plano, mas o sistema falha em gerar o relatório final. "
        "O usuário experimenta o impacto físico, mas o status do sistema permanece como 'Erro Desconhecido', "
        "o que impede a regulação e frequentemente leva ao superaquecimento do processador central (Meltdown).\n\n"
        "O SMARS finaliza este ciclo atuando como um Driver Externo de Intermediação, fundamentado na "
        "Pedagogia de Vygotsky. Ele fornece o 'Andaime' necessário na Zona de Desenvolvimento Proximal, "
        "oferecendo as legendas e os signos que o processador interno não consegue gerar sozinho no momento. "
        "\nAo mapear a telemetria física e sugerir diagnósticos lógicos, o software auxilia a CPU central a "
        "completar a tradução afetiva. O objetivo final é a Reeducação Neural Ativa, garantindo que, através "
        "da mediação tecnológica, o indivíduo reconquiste sua soberania emocional e a capacidade de ler "
        "seu próprio código interno com clareza e dignidade.\n\n"
        "REFERÊNCIAS BIBLIOGRÁFICAS:\n"
        "• DAMÁSIO, A. (2018). A Estranha Ordem das Coisas: As origens biológicas dos sentimentos. Companhia das Letras.\n"
        "• LAZARUS, R. S. (1991). Emotion and Adaptation. Oxford University Press. (Appraisal Theory).\n"
        "• SIFNEOS, P. E. (1973). The prevalence of 'alexithymic' characteristics in psychosomatic patients.\n"
        "• VYGOTSKY, L. S. (1978). Mind in Society: Development of Higher Psychological Processes.\n"
        "• MARKRAM, H.; MARKRAM, K. (2007). The Intense World Theory – a unifying hypothesis for autism."
    )

    caixa_texto.insert("0.0", texto_direto)
    caixa_texto.configure(state="disabled") 


def abrir_comousar():
    janela = ctk.CTkToplevel()
    janela.title("SMARS - COMO USAR?")
    centralizar_janela(janela,650,650) 
    janela.attributes("-topmost", True)
    janela.grab_set()

    # Botão no fundo primeiro
    btn_sair = ctk.CTkButton(
        janela, 
        text="VAMOS TESTAR", 
        font=("Segoe UI", 14, "bold"),
        fg_color="#1f538d", 
        hover_color="#14375e",
        height=45,
        command=janela.destroy
    )
    btn_sair.pack(side="bottom", pady=(10, 25))

    caixa_texto = ctk.CTkTextbox(
        janela, 
        font=("Segoe UI", 16), 
        border_spacing=35,
        fg_color="transparent",
        wrap="word"
    )
    caixa_texto.pack(padx=20, pady=(20, 0), fill="both", expand=True)

    texto_direto = (
        "SMARS \nCOMO USAR?\n"
        "______________________________________________________________\n\n"
        """Para iniciar o processo de tradução de sinais e regulação emocional,siga as instruções de navegação da interface:

1. INICIALIZAÇÃO DO SISTEMA:
No menu principal, selecione a opção [IDENTIFICAR SENTIMENTOS].
Este é o ponto de entrada para qualquer análise de sinais internos.

2. SELEÇÃO DE FLUXO (Status da CPU):
O sistema perguntará: "Sabe o que está sentindo?". Escolha o caminho baseado na clareza do seu processador central no momento:

A) SE VOCÊ JÁ NOMEOU O SENTIMENTO QUE ESTÁ SENTINDO:
 - Clique em SIM.
 - Insira o nome do sentimento que você identificou
 (Ex: Ansiedade, Sobrecarga).
- Aguarde o processamento do "MANEJO-RESPOSTA" com as instruções.

B) SE VOCÊ NÃO SABE O NOME DO QUE ESTÁ SENTINDO:
  - Clique em NÃO.
  - O sistema abrirá um campo para entrada da TELEMETRIA BRUTA.
  - Descreva as sensações físicas e mentais exatamente como você as sente.

EXEMPLOS DE ENTRADA:
  > "Sinto que minha mente vai explodir, tô acelerada, mãos frias."
  > "Sinto minha barriga agitada, mãos suando e mente inquieta."
  > "Meus olhos estão pesados, minha cabeça tá doendo."
  > "To com um aperto na barriga e minha cabeça tá meio zonza."

3. PROCESSAMENTO E SAÍDA:
Após o envio do SENTIMENTO ou SENSAÇÕES, o SMARS atuará como  seu Driver de Intermediação, cruzando os dados para sugerir o  diagnóstico lógico e acender o "painel" em meio a tempestade."""
    )

    caixa_texto.insert("0.0", texto_direto)
    caixa_texto.configure(state="disabled") 


def abrir_sobre_projeto():
    janela_sobre = ctk.CTkToplevel()
    janela_sobre.title("SMARS - SISTEMA DE MANEJO DE ALEXITIMIA E REEDUCAÇÃO SENTIMENTAL")
    centralizar_janela(janela_sobre,650,650)
    janela_sobre.attributes("-topmost", True)
    janela_sobre.grab_set()

    # Botão no fundo primeiro
    btn_voltar = ctk.CTkButton(
        janela_sobre, 
        text="COMPREENDIDO", 
        font=("Segoe UI", 14, "bold"),
        fg_color="#1f538d", 
        hover_color="#14375e",
        height=45,
        command=janela_sobre.destroy
    )
    btn_voltar.pack(side="bottom", pady=(10, 25))

    caixa_texto = ctk.CTkTextbox(
        janela_sobre, 
        font=("Segoe UI", 16), 
        border_spacing=35,
        fg_color="transparent",
        wrap="word"
    )
    caixa_texto.pack(padx=20, pady=(20, 0), fill="both", expand=True)

    texto_manifesto = (
        "SMARS \nSISTEMA DE MANEJO DE ALEXITIMIA E REEDUCAÇÃO SENTIMENTAL\n"
        "______________________________________________________________\n\n"
        "O SMARS não é meramente um utilitário de software, é uma infraestrutura de mediação projetada para a "
        "independência cognitiva. Ele nasce para preencher um hiato crítico no processamento de informações "
        "humanas: a incapacidade de converter o fluxo caótico de sinais interoceptivos em símbolos linguísticos "
        "operáveis pela consciência. \nO SMARS é a ponte tecnológica construída para atravessar o abismo da "
        "Alexitimia, transformando o impacto sensorial bruto em conhecimento estratégico e autogestão emocional.\n\n"
        "A necessidade deste sistema fundamenta-se na realidade de que, para o indivíduo neurodivergente, a "
        "existência ocorre frequentemente sob uma 'Tempestade de Dados'. \nImagine pilotar uma aeronave complexa "
        "através de uma névoa densa onde todos os indicadores de telemetria — altitude, velocidade e combustível — "
        "estão em pane ou desconectados. \nO mundo atípico é percebido com uma intensidade avassaladora, mas sem os "
        "instrumentos de leitura adequados. \nO SMARS não pretende silenciar a tempestade ou suprimir as reações "
        "biológicas; seu propósito é ACENDER O PAINEL DE CONTROLE. Ele fornece a interface de visualização "
        "necessária para que a navegação pela vida deixe de ser uma reação desesperada ao caos e passe a ser "
        "uma ação consciente e calculada.\n\n"
        "A Filosofia do Exoesqueleto Mental postula que a neurodivergência não é um erro de código a ser corrigido "
        "ou uma patologia a ser curada, mas uma arquitetura de hardware alternativa que requer drivers de interface "
        "específicos. \nAssim como um exoesqueleto que devolve a função motora ao corpo, o SMARS atua como uma prótese "
        "cognitiva que devolve a função de INTERPRETAÇÃO. \nAtravés da mediação tecnológica fundamentada na Pedagogia "
        "de Vygotsky, o sistema opera na Zona de Desenvolvimento Proximal do usuário, oferecendo os 'signos' e 'ferramentas' "
        "externas que permitem a internalização progressiva da capacidade de nomear e gerir o próprio estado interno.\n\n"
        "Os Pilares de Excelência Operacional do SMARS garantem essa soberania. No âmbito da Segurança e Prevenção, "
        "o sistema funciona como um sentinela térmico, identificando padrões de superaquecimento químico — como a "
        "elevação abrupta da voltagem cardíaca e tensão muscular — para antecipar estados de Meltdown e Shutdown "
        "antes do colapso do sistema. \nNo campo da Dignidade Humana, o SMARS desmancha a dependência de intérpretes "
        "externos, garantindo que a autoridade sobre o que é sentido pertença exclusivamente ao indivíduo. \nPor fim, "
        "através da Reeducação Neural, cada interação com o algoritmo é um reforço sináptico que treina a mente "
        "para reconhecer sua própria biologia.\n\n"
        "O SMARS existe porque o autoconhecimento não deve ser um labirinto inacessível ou um diagnóstico imposto por "
        "terceiros, mas um direito humano fundamental. Esta interface é desenvolvida para garantir "
        "que o indivíduo atípico deixe de ser um passageiro à mercê de suas reações químicas e se torne o mestre "
        "absoluto de seu próprio código interno."
    )

    caixa_texto.insert("0.0", texto_manifesto)
    caixa_texto.configure(state="disabled")


def abrir_intuito():
    janela = ctk.CTkToplevel()
    janela.title("SMARS - ARQUITETURA OPERACIONAL")
    centralizar_janela(janela,650,650) 
    janela.attributes("-topmost", True)
    janela.grab_set()

    # Botão no fundo primeiro
    btn_sair = ctk.CTkButton(
        janela, 
        text="COMPREENDIDO", 
        font=("Segoe UI", 14, "bold"),
        fg_color="#1f538d", 
        hover_color="#14375e",
        height=45,
        command=janela.destroy
    )
    btn_sair.pack(side="bottom", pady=(10, 25))

    caixa_texto = ctk.CTkTextbox(
        janela, 
        font=("Segoe UI", 16), 
        border_spacing=35,
        fg_color="transparent",
        wrap="word"
    )
    caixa_texto.pack(padx=20, pady=(20, 0), fill="both", expand=True)

    texto_direto = (
       
    """COMO FUNCIONA O SMARS?
A ENGENHARIA DA REEDUCAÇÃO SENTIMENTAL E AUTONOMIA
________________________________________________________________________

O SMARS opera como um EXOESQUELETO MENTAL TEMPORÁRIO. Seu funcionamento não visa criar dependência tecnológica, mas sim realizar uma "atualização" no processador central do usuário (a mente), utilizando os princípios da Pedagogia de Vygotsky.

O sistema funciona através de três estágios de maturação:


1. O ESTÁGIO DO APOIO (Mediação Externa):
   No início, o usuário enfrenta a "névoa" da Alexitimia e não consegue "enxergar" os proprios sentimentos.
   O SMARS entra como o INSTRUMENTO DE MEDIAÇÃO. 

   - O QUE O SOFTWARE FAZ: Ele fornece as palavras, os nomes e os caminhos que você ainda não consegue visualizar sozinho. Ele vai segurar todo o peso da interpretação e do processamento enquanto seu sistema interno está sobrecarregado e te fornecerá intruções para aquele momento.

   - O OBJETIVO: Estabilizar o hardware e evitar o Meltdown imediato através de instruções externas de manejo e controle.

   
2. A ZONA DE DESENVOLVIMENTO PROXIMAL (Aprendizado Ativo)
   Com o uso contínuo, o funcionamento do SMARS cria um "Andaime". Cada vez que você descreve uma sensação fisica e o programa associa a um sentimento ou busca como lidar com um sentimento e o programa sugere um manejo, você está treinando seu cérebro a fazer essa associação.

   - O QUE O SOFTWARE FAZ: Ele cria o link lógico entre o SINAL FÍSICO (ex: mão suando) e o SIGNIFICADO (ex: ansiedade) e cria a associação entre SENTIMENTO e MANEJO.

   - O OBJETIVO: Diminuir a latência entre o sentir, o entender e o agir.

   
3. A INTERIORIZAÇÃO (Soberania e Autonomia)
   Este é o estágio final do uso do SMARS. De acordo com a teoria de Vygotsky, o que antes era feito com ajuda externa passa a ser feito internamente. 

   - O QUE ACONTECE: O raciocínio lógico do programa é absorvido pelas suas próprias sinapses. Você começa a identificar as sensações, linka-las aos sentimentos correspondentes e a aplicar os manejos SOZINHO E AUTOMATICAMENTE, antes mesmo de abrir o software.

   - O OBJETIVO FINAL: Que o SMARS se torne obsoleto. O intuito é que você "desinstale" a necessidade de usa-lo, porque agora você possui a SOBERANIA ABSOLUTA sobre o seu próprio código interno.

   
MISSÃO OPERACIONAL: 

O SMARS te apoia hoje para que você não precise de apoio amanhã. 
A tecnologia a serviço da autonomia do sentir."""
    )

    caixa_texto.insert("0.0", texto_direto)
    caixa_texto.configure(state="disabled")
