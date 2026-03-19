import tkinter as tk # Importa a biblioteca base para interfaces gráficas
import customtkinter as ctk # Importa a biblioteca para o visual moderno e Modo Escuro
from datetime import datetime # Importa funções para ler a hora atual do seu computador
import varredura_fisica # Importa o seu módulo que traduz sensações do corpo
import dicionario # Importa o seu módulo com o banco de dados de sentimentos
import sqlite3
from datetime import datetime, timedelta
import motor_logico  # Importa o arquivo de manejo
hora_atual = datetime.now().strftime("%H:%M")

def configurar_banco():
    conn = sqlite3.connect("smars_logs.db")
    cursor = conn.cursor()
    # Cria a tabela se ela não existir
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data_hora TEXT,
            sentimento TEXT,
            intensidade TEXT
        )
    """)
    conn.commit()
    conn.close()

# Chama a configuração ao iniciar o programa
configurar_banco()

def salvar_log(sentimento, intensidade):
    conn = sqlite3.connect("smars_logs.db")
    cursor = conn.cursor()
    agora = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    cursor.execute("INSERT INTO logs (data_hora, sentimento, intensidade) VALUES (?, ?, ?)", 
                   (agora, sentimento, intensidade))
    conn.commit()
    conn.close()

# --- CONFIGURAÇÃO VISUAL DO SISTEMA ---
ctk.set_appearance_mode("dark") # Define que o programa rodará sempre em Modo Escuro
ctk.set_default_color_theme("blue") # Define a cor azul como padrão para botões e detalhes

# --- FUNÇÕES DAS JANELAS PRINCIPAIS ---

import customtkinter as ctk
from datetime import datetime
def abrir_scanner():
    """Abre apenas a janela de decisão inicial"""
    janela_decisao = ctk.CTkToplevel()
    janela_decisao.title("SMARS - SCANNER")
    janela_decisao.geometry("400x250")
    janela_decisao.attributes("-topmost", True)
    janela_decisao.grab_set()

    ctk.CTkLabel(janela_decisao, text="VOCÊ CONSEGUE IDENTIFICAR\nO QUE ESTÁ SENTINDO?", font=("Segoe UI", 14, "bold")).pack(pady=30)
    
    frame_btns = ctk.CTkFrame(janela_decisao, fg_color="transparent")
    frame_btns.pack(pady=10)

    # Ao clicar nos botões abaixo, eles sim chamam a função 'processar_final' com os dados
    def vai_para_sim():
        janela_decisao.destroy()
        res = ctk.CTkInputDialog(text="O que sente?", title="MANEJO").get_input()
        if res: processar_final(res, "direto")

    def vai_para_nao():
        janela_decisao.destroy()
        res = ctk.CTkInputDialog(text="Sensações físicas:", title="VARREDURA").get_input()
        if res: processar_final(res, "fisico")

    ctk.CTkButton(frame_btns, text="SIM", command=vai_para_sim, fg_color="#1f538d").pack(side="left", padx=10)
    ctk.CTkButton(frame_btns, text="NÃO", command=vai_para_nao, fg_color="#c0392b").pack(side="left", padx=10)

def exibir_interface_manejo(diag, expl, instr, frase):
    import customtkinter as ctk

    # 1. CRIAR APENAS A ESTRUTURA BÁSICA
    janela_res = ctk.CTkToplevel()
    janela_res.title("SMART ATIPIC | Central de Manejo")
    janela_res.geometry("650x750")
    janela_res.configure(fg_color="#0B0D14")
    janela_res.attributes("-topmost", True)
    
    # IMPORTANTE: Deixe a janela invisível por um instante para evitar o "flash" preto
    janela_res.attributes("-alpha", 0.0) 

    def desenhar_conteudo():
        # Cores de Acento
        cor_acento = "#4F46E5"
        if any(p in str(diag).upper() for p in ["CRÍTICO", "MELTDOWN", "SHUTDOWN"]):
            cor_acento = "#E11D48"
        
        # Cabeçalho
        ctk.CTkLabel(janela_res, text="SMART ATIPIC // TELEMETRIA", 
                     font=("Segoe UI", 10, "bold"), text_color=cor_acento).pack(pady=(40,0), padx=40, anchor="w")
        
        ctk.CTkLabel(janela_res, text=diag, font=("Segoe UI Light", 30), 
                     text_color="#FFFFFF").pack(padx=40, anchor="w")

        # Card Principal
        card = ctk.CTkFrame(janela_res, fg_color="#161B2A", corner_radius=20)
        card.pack(fill="both", expand=True, padx=30, pady=20)

        # Usar LABEL em vez de Textbox para TESTE (Labels são mais leves e não bugam)
        ctk.CTkLabel(card, text="ANÁLISE TÉCNICA", font=("Segoe UI", 10, "bold"), text_color="#64748B").pack(pady=(20,0), padx=20, anchor="w")
        
        lbl_expl = ctk.CTkLabel(card, text=expl, font=("Segoe UI", 13), text_color="#CBD5E1", 
                                wraplength=550, justify="left")
        lbl_expl.pack(pady=10, padx=20, anchor="w")

        ctk.CTkLabel(card, text="INSTRUÇÕES", font=("Segoe UI", 10, "bold"), text_color=cor_acento).pack(pady=(10,0), padx=20, anchor="w")
        
        lbl_instr = ctk.CTkLabel(card, text=instr, font=("Segoe UI Semibold", 15), text_color="#FFFFFF", 
                                 wraplength=550, justify="left")
        lbl_instr.pack(pady=10, padx=20, anchor="w")

        # Botão
        ctk.CTkButton(janela_res, text="ESTABILIZAR", command=janela_res.destroy, 
                      fg_color=cor_acento, height=45).pack(pady=20, padx=40, fill="x")

        # Torna a janela visível APÓS desenhar tudo
        janela_res.attributes("-alpha", 1.0)
        janela_res.grab_set()

    # O SEGREDO: Chama a função de desenhar após 200ms
    janela_res.after(200, desenhar_conteudo)

def processar_final(entrada_usuario, tipo_fluxo):
    """O Cérebro do SMARS: Conecta inputs ao motor_logico, dicionário e varredura"""
    import motor_logico 
    from datetime import datetime
    
    sentimento_final = "Não Identificado"
    intensidade = 5
    cat_match = "outro"

    try:
        # --- CAMINHO A: IDENTIFICAÇÃO DIRETA ---
        if tipo_fluxo == "direto":
            sentimento_final = entrada_usuario
            int_input = ctk.CTkInputDialog(text="Intensidade (1 a 10):", title="TELEMETRIA").get_input()
            
            if int_input and int_input.isdigit():
                intensidade = int(int_input)
            
            # Busca no seu arquivo dicionario.py
            cat_match = dicionario.buscar_sentimento(entrada_usuario)
            if not cat_match:
                cat_match = "outro" 

        # --- CAMINHO B: TRADUÇÃO POR VARREDURA FÍSICA ---
        elif tipo_fluxo == "fisico":
            # O sistema consulta o seu programa especializado em sensações físicas
            detectado_bruto = varredura_fisica.tradutor_fisico(entrada_usuario)
            sentimento_final = str(detectado_bruto).upper()
            intensidade = 7  # Intensidade padrão para detecção física (alerta)

            # Ponte de Categorias: Traduz o termo técnico para a chave do Motor Lógico
            ponte_categorias = {
                "FOME": "fome", "SEDE": "sede", "SONO / EXAUSTÃO": "cansaco",
                "MAL-ESTAR FÍSICO": "mal_estar", "DOR DE CABEÇA / ENXAQUECA": "dor_cabeca",
                "MELTDOWN (CRISE EXTERNA)": "sensorial", "SHUTDOWN (CRISE INTERNA)": "shutdown",
                "SOBRECARGA SENSORIAL": "sensorial", "BURNOUT (ESGOTAMENTO)": "burnout",
                "DISSOCIAÇÃO": "dissociacao", "INÉRCIA EXECUTIVA": "inercia", 
                "HIPERFOCO / EMPOLGAÇÃO": "hiperfoco", "CONFUSÃO / OVERLOAD COGNITIVO": "confusao", 
                "ECOLALIA (REPETIÇÃO)": "looping", "CURIOSIDADE": "curiosidade",
                "ANSIEDADE / PÂNICO": "ansiedade", "RSD (DISFORIA SENSÍVEL À REJEIÇÃO)": "rejeicao", 
                "TRISTEZA / ANGÚSTIA": "tristeza", "AFETO / AMOR": "afeto",
                "RAIVA": "raiva", "MEDO / INSEGURANÇA": "medo", "FRUSTRAÇÃO": "frustracao", 
                "SOLIDÃO": "solidao", "ORGULHO / SUCESSO": "orgulho", "GRATIDÃO": "gratidao", 
                "PAZ / HOMEOSTASE": "paz", "INJUSTIÇA": "injustica", "NOJO / AVERSÃO": "nojo",
                "STIMMING (AUTORREGULAÇÃO)": "stimming"
            }
            
            # Busca segura: strip remove espaços e upper garante a caixa alta
            cat_match = ponte_categorias.get(sentimento_final.strip(), "outro")

        # --- FINALIZAÇÃO E RELATÓRIO ---
        hora_atual = datetime.now().strftime("%H:%M")

        # Registro de Telemetria (Banco de dados ou Log)
        try:
            salvar_log(sentimento_final.upper(), f"{intensidade}/10")
        except:
            print("Aviso: Falha ao registrar log, mas o sistema continua.")

        # Obtém os textos refinados do motor_logico.py
        diag, expl, instr, frase = motor_logico.obter_relatorio(cat_match, intensidade, hora_atual)
        
        # Dispara a interface visual de requinte
        exibir_interface_manejo(diag, expl, instr, frase)

    except Exception as e:
        print(f"ERRO CRÍTICO NO PROCESSAMENTO SMARS: {e}")
        # Opcional: mostrar um aviso simples em caso de erro fatal

def abrir_historico():
    janela = ctk.CTkToplevel()
    janela.title("SMARS - HISTÓRICO DE SENTIMENTOS")
    janela.geometry("700x750")
    janela.attributes("-topmost", True)
    janela.configure(fg_color="#1a1a1a") # Fundo mais profundo

    # Título da Janela
    ctk.CTkLabel(
        janela, 
        text="REGISTROS DE SENTIMENTOS", 
        font=("Segoe UI", 24, "bold"),
        text_color="#1f538d"
    ).pack(pady=(20, 10))

    # Frame para os botões de filtro
    frame_filtros = ctk.CTkFrame(janela, fg_color="transparent")
    frame_filtros.pack(pady=10, padx=10, fill="x")

    # Container principal dos cards (Scrollable)
    # É aqui que a "mágica" acontece: cada log vira um objeto visual
    container_cards = ctk.CTkScrollableFrame(
        janela, 
        width=650, 
        height=500,
        fg_color="#242424",
        scrollbar_button_color="#1f538d"
    )
    container_cards.pack(pady=10, padx=20, fill="both", expand=True)

    def carregar_logs(filtro_dias=None):
        # Limpar cards antigos antes de carregar novos
        for widget in container_cards.winfo_children():
            widget.destroy()
        
        conn = sqlite3.connect("smars_logs.db")
        cursor = conn.cursor()
        
        if filtro_dias:
            # Filtro inteligente por data
            data_limite = (datetime.now() - timedelta(days=filtro_dias)).strftime("%d/%m/%Y")
            cursor.execute("SELECT * FROM logs WHERE data_hora >= ? ORDER BY id DESC", (data_limite,))
        else:
            cursor.execute("SELECT * FROM logs ORDER BY id DESC")
            
        rows = cursor.fetchall()
        
        if not rows:
            ctk.CTkLabel(
                container_cards, 
                text=">>> NENHUM LOG REGISTRADO NO PERÍODO.", 
                font=("Segoe UI", 14, "italic"),
                text_color="gray"
            ).pack(pady=50)
        else:
            for row in rows:
                # Criar um Card para cada log
                card = ctk.CTkFrame(container_cards, fg_color="#2b2b2b", corner_radius=10, border_width=1, border_color="#3d3d3d")
                card.pack(pady=8, padx=10, fill="x")

                # Label da Data/Hora (Estilo Log Científico)
                ctk.CTkLabel(
                    card, 
                    text=f"TIMESTAMP: {row[1]}", 
                    font=("Segoe UI", 11),
                    text_color="#1f538d"
                ).pack(anchor="w", padx=15, pady=(10, 0))

                # Label do Sentimento (Destaque Principal)
                ctk.CTkLabel(
                    card, 
                    text=row[2].upper(), 
                    font=("Segoe UI", 18, "bold"),
                    text_color="#ffffff"
                ).pack(anchor="w", padx=15)

                # Label da Intensidade
                ctk.CTkLabel(
                    card, 
                    text=f"NÍVEL DE INTENSIDADE: {row[3]}", 
                    font=("Segoe UI", 13),
                    text_color="#aaaaaa"
                ).pack(anchor="w", padx=15, pady=(0, 10))

        conn.close()

    # Botões de Filtro Estilizados
    estilo_btn = {"width": 100, "height": 35, "font": ("Segoe UI", 12, "bold")}
    
    ctk.CTkButton(frame_filtros, text="24 HORAS", command=lambda: carregar_logs(1), **estilo_btn).pack(side="left", padx=10, expand=True)
    ctk.CTkButton(frame_filtros, text="7 DIAS", command=lambda: carregar_logs(7), **estilo_btn).pack(side="left", padx=10, expand=True)
    ctk.CTkButton(frame_filtros, text="30 DIAS", command=lambda: carregar_logs(30), **estilo_btn).pack(side="left", padx=10, expand=True)
    ctk.CTkButton(frame_filtros, text="TODOS", command=lambda: carregar_logs(), **estilo_btn).pack(side="left", padx=10, expand=True)

    # Botão Sair (Invisível no fundo até o scroll chegar nele ou fixo)
    btn_sair = ctk.CTkButton(
        janela, 
        text="CONCLUIR", 
        font=("Segoe UI", 14, "bold"),
        fg_color="#d35400", 
        hover_color="#a04000",
        height=45,
        command=janela.destroy
    )
    btn_sair.pack(side="bottom", pady=25)

    # Iniciar carregando tudo
    carregar_logs()
import customtkinter as ctk

def abrir_explicacao_alexitimia():
    janela_alex = ctk.CTkToplevel()
    janela_alex.title("SMARS - O QUE É ALEXITIMIA?")
    janela_alex.geometry("850x850")
    janela_alex.attributes("-topmost", True)

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
        "______________________________________________________________________\n\n"
        "A Alexitimia — termo derivado do grego 'Alexisthymos' (a = ausência, lexis = palavra, thymos = emoção) — "
        "não é uma descoberta recente, mas um constructo clínico consolidado. O termo foi cunhado pelo psiquiatra "
        "Peter Sifneos, de Harvard, em 1973, no artigo 'The prevalence of alexithymic characteristics in psychosomatic patients', "
        "publicado na revista Psychotherapy and Psychosomatics. Sifneos observou que pacientes com doenças psicossomáticas "
        "não possuíam um 'vocabulário de sentimentos', apresentando uma pobreza extrema na fantasia e no pensamento simbólico. "
        "No SMARS, interpretamos essa observação original como uma falha crítica no 'Driver de Tradução': o hardware biológico "
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
        "com tamanha latência que a experiênca sentida se perde antes de ser rotulada. No contexto neurodivergente, a 'Teoria do Mundo "
        "Intenso' de Markram e Markram (2007) sugere que o cérebro autista é hiper-reativo; logo, a Alexitimia surge como um "
        "'Modo de Proteção contra Sobrecarga' (Firewall Biológico). O sistema desativa as notificações de sentimento para evitar que "
        "o processador central entre em colapso (Meltdown) diante da intensidade avassaladora do mundo.\n\n"
        
        "A alma do SMARS, entretanto, reside na Pedagogia de Lev Vygotsky. Vygotsky defendia que o desenvolvimento humano é mediado "
        "por instrumentos e signos. O SMARS atua exatamente como um 'Andaime' (Scaffolding) dentro da Zona de Desenvolvimento Proximal "
        "(ZDP) — a distância entre o que o indivíduo consegue fazer sozinho e o que consegue com ajuda. Como o alexitímico não possui "
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
    janela.geometry("950x900") 
    janela.attributes("-topmost", True)

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
        "O QUE SÃO SENTIMENTOS? UMA PERSPECTIVA NEUROBIOLÓGICA E COGNITIVA\n"
        "______________________________________________________________________\n\n"
        "Cientificamente, o sentimento não é um evento isolado, mas o estágio final de um processo "
        "biológico complexo que visa a manutenção da vida. Tudo começa com a Homeostase, o esforço do "
        "organismo para manter o equilíbrio interno. Através da Interocepção, o sistema nervoso monitora "
        "constantemente o estado dos órgãos e tecidos. Quando um estímulo externo ou interno ocorre, "
        "o corpo dispara uma Emoção — que, segundo António Damásio, é um conjunto de respostas químicas "
        "e neurais automáticas e universais. Essas respostas ocorrem no Sistema Límbico, especificamente "
        "na Amígdala, gerando alterações físicas imediatas como aceleração cardíaca, sudorese e tensão "
        "muscular, antes mesmo de qualquer percepção consciente.\n\n"
        "No ecossistema do SMARS, interpretamos essa cadeia biológica através da lógica de sistemas. "
        "As sensações físicas são a nossa 'Telemetria Bruta de Hardware': dados puros vindos de sensores "
        "periféricos informando sobre a voltagem e o status do organismo. As emoções, por sua vez, são "
        "vistas como 'Protocolos de Segurança' ou scripts de execução rápida, desenhados para proteger "
        "a integridade do sistema operacional humano em situações de risco ou recompensa. O Sentimento "
        "surge, portanto, como o 'Relatório Processado pela CPU Central' (a mente consciente). Ele é a "
        "tradução semântica da pergunta: 'Por que meu hardware está agindo assim agora?'. É o momento "
        "em que o Córtex Pré-Frontal associa a eletricidade da emoção a um contexto, transformando a "
        "reação química em experiênca subjetiva e nomeável.\n\n"
        "Aprofundando na neurociência da consciência, esse processo de tradução depende da integridade "
        "funcional de áreas como a Ínsula Anterior e o Córtex Cingulado Posterior. A Teoria da Avaliação "
        "Cognitiva (Appraisal Theory) postula que o sentimento depende de como o cérebro avalia o estímulo. "
        "Na Alexitimia, ocorre um Erro de Driver crítico: há uma desconexão ou latência entre a leitura do "
        "corpo e a área de processamento de símbolos e linguagem. O hardware está 'quente' e os protocolos "
        "de emergência estão rodando em segundo plano, mas o sistema falha em gerar o relatório final. "
        "O usuário experimenta o impacto físico, mas o status do sistema permanece como 'Erro Desconhecido', "
        "o que impede a regulação e frequentemente leva ao superaquecimento do processador central (Meltdown).\n\n"
        "O SMARS finaliza este ciclo atuando como um Driver Externo de Intermediação, fundamentado na "
        "Pedagogia de Vygotsky. Ele fornece o 'Andaime' necessário na Zona de Desenvolvimento Proximal, "
        "oferecendo as legendas e os signos que o processador interno não consegue gerar sozinho no momento. "
        "Ao mapear a telemetria física e sugerir diagnósticos lógicos, o software auxilia a CPU central a "
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

def abrir_sobre_projeto():
    janela_sobre = ctk.CTkToplevel()
    janela_sobre.title("SMARS - SISTEMA DE MANEJO DE ALEXITIMIA E REEDUCAÇÃO SENTIMENTAL")
    janela_sobre.geometry("950x900")
    janela_sobre.attributes("-topmost", True)

    # Botão no fundo primeiro
    btn_voltar = ctk.CTkButton(
        janela_sobre, 
        text="SISTEMA VALIDADO", 
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
        "SMARS: SISTEMA DE MANEJO DE ALEXITIMIA E REEDUCAÇÃO SENTIMENTAL\n"
        "_________________________________________________________________________________\n\n"
        "O SMARS não é meramente um utilitário de software; é uma infraestrutura de mediação projetada para a "
        "independência cognitiva. Ele nasce para preencher um hiato crítico no processamento de informações "
        "humanas: a incapacidade de converter o fluxo caótico de sinais interoceptivos em símbolos linguísticos "
        "operáveis pela consciência. O SMARS é a ponte tecnológica construída para atravessar o abismo da "
        "Alexitimia, transformando o impacto sensorial bruto em conhecimento estratégico e autogestão emocional.\n\n"
        "A necessidade deste sistema fundamenta-se na realidade de que, para o indivíduo neurodivergente, a "
        "existência ocorre frequentemente sob uma 'Tempestade de Dados'. Imagine pilotar uma aeronave complexa "
        "através de uma névoa densa onde todos os indicadores de telemetria — altitude, velocidade e combustível — "
        "estão em pane ou desconectados. O mundo atípico é percebido com uma intensidade avassaladora, mas sem os "
        "instrumentos de leitura adequados. O SMARS não pretende silenciar a tempestade ou suprimir as reações "
        "biológicas; seu propósito é ACENDER O PAINEL DE CONTROLE. Ele fornece a interface de visualização "
        "necessária para que a navegação pela vida deixe de ser uma reação desesperada ao caos e passe a ser "
        "uma ação consciente e calculada.\n\n"
        "A Filosofia do Exoesqueleto Mental postula que a neurodivergência não é um erro de código a ser corrigido "
        "ou uma patologia a ser curada, mas uma arquitetura de hardware alternativa que requer drivers de interface "
        "específicos. Assim como um exoesqueleto devolve a função motora ao corpo, o SMARS atua como uma prótese "
        "cognitiva que devolve a função de INTERPRETAÇÃO. Através da mediação tecnológica fundamentada na Pedagogia "
        "de Vygotsky, o sistema opera na Zona de Desenvolvimento Proximal do usuário, oferecendo os 'signos' e 'ferramentas' "
        "externas que permitem a internalização progressiva da capacidade de nomear e gerir o próprio estado interno.\n\n"
        "Os Pilares de Excelência Operacional do SMARS garantem essa soberania. No âmbito da Segurança e Prevenção, "
        "o sistema funciona como um sentinela térmico, identificando padrões de superaquecimento químico — como a "
        "elevação abrupta da voltagem cardíaca e tensão muscular — para antecipar estados de Meltdown e Shutdown "
        "antes do colapso do sistema. No campo da Dignidade Humana, o SMARS desmancha a dependência de intérpretes "
        "externos, garantindo que a autoridade sobre o que é sentido pertença exclusivamente ao indivíduo. Por fim, "
        "através da Reeducação Neural, cada interação com o algoritmo é um reforço sináptico que treina a mente "
        "para reconhecer sua própria biologia.\n\n"
        "O SMARS existe porque o autoconhecimento não deve ser um labirinto inacessível ou um diagnóstico imposto por "
        "terceiros, mas um direito humano fundamental. Esta é a interface definitiva desenvolvida para garantir "
        "que o indivíduo atípico deixe de ser um passageiro à mercê de suas reações químicas e se torne o mestre "
        "absoluto de seu próprio código interno."
    )

    caixa_texto.insert("0.0", texto_manifesto)
    caixa_texto.configure(state="disabled")

# --- INTERFACE PRINCIPAL (DASHBOARD) ---

def criar_painel_principal():
    root = ctk.CTk() # Cria a janela principal do programa
    root.title("SMARS - Painel de Controle") # Nome da janela na barra superior
    root.geometry("500x525") # Define o tamanho da janela (Largura x Altura)

    # Título principal do Dashboard no topo da tela
    ctk.CTkLabel(root, text="SISTEMA DE MANEJO DE ALEXITIMIA E REEDUCAÇÃO SENTIMENTAL", font=("Segoe UI", 14, "bold")).pack(pady=20)
    
    # Cria um 'Frame' (uma caixa invisível) para organizar os botões
    frame_menu = ctk.CTkFrame(root, fg_color="transparent")
    frame_menu.pack(pady=0, padx=10, fill="both", expand=True)

    # --- COMANDO DE CENTRALIZAÇÃO ---
    # Esta linha abaixo é o segredo: ela dá "peso" à coluna 0, forçando-a a ocupar o centro do frame
    frame_menu.grid_columnconfigure(0, weight=1) 
    # --------------------------------

   # BOTÃO 1: SCANNER
    btn_scanner = ctk.CTkButton(
        frame_menu, text="IDENTIFICAR SENTIMENTO", 
        width=280, height=55, # Aumentei um pouco a largura para ficar mais imponente
        font=("Segoe UI", 14, "bold"), 
        fg_color="#1f538d", # O azul oficial do SMARS
        hover_color="#14375e", # Azul mais escuro ao passar o mouse
        command=abrir_scanner
    )
    btn_scanner.grid(row=0, column=0, padx=15, pady=12) 

    # BOTÃO 2: HISTÓRICO
    btn_hist = ctk.CTkButton(
        frame_menu, text="HISTÓRICO DE SENTIMENTOS", 
        width=280, height=55,
        font=("Segoe UI", 14, "bold"),
        fg_color="#1f538d",
        hover_color="#14375e",
        command=abrir_historico
    )
    btn_hist.grid(row=1, column=0, padx=15, pady=12) 
   
    # BOTÃO 3: EXPLICAÇÃO PROGRAMA (O QUE É O SMARS)
    btn_programa = ctk.CTkButton(
        frame_menu, text="O QUE É O 'SMARS'?", 
        width=280, height=55,
        font=("Segoe UI", 14, "bold"),
        fg_color="#1f538d",
        hover_color="#14375e",
        command=abrir_sobre_projeto
    )
    btn_programa.grid(row=2, column=0, padx=15, pady=12) 

    # BOTÃO 4: EXPLICAÇÃO ALEXITIMIA (O QUE É ALEXITIMIA)
    btn_alexi = ctk.CTkButton(
        frame_menu, text="O QUE É ALEXITIMIA?", 
        width=280, height=55,
        font=("Segoe UI", 14, "bold"),
        fg_color="#1f538d",
        hover_color="#14375e",
        command=abrir_explicacao_alexitimia
    )
    btn_alexi.grid(row=3, column=0, padx=15, pady=12)

    # BOTÃO 5: EXPLICAÇÃO SENTIMENTOS
    btn_conceito = ctk.CTkButton(
        frame_menu, text="O QUE SÃO SENTIMENTOS?", 
        width=280, height=55,
        font=("Segoe UI", 14, "bold"),
        fg_color="#1f538d",
        hover_color="#14375e",
        command=abrir_conceito
    )
    btn_conceito.grid(row=4, column=0, padx=15, pady=12) 



    # Texto de crédito no rodapé da janela
    ctk.CTkLabel(root, text="2026 - Bianca L. Chelles", font=("Consolas", 10)).pack(side="bottom", pady=20)

    root.mainloop() # Mantém o programa rodando
# Ponto de entrada que inicia tudo
if __name__ == "__main__":
    criar_painel_principal()
