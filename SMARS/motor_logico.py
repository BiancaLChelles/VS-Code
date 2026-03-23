from datetime import datetime

def obter_relatorio(cat_match, intensidade, hora_atual_str):
    """
    Motor de Regras do SMART ATIPIC.
    Recebe a categoria, intensidade e a hora formatada.
    Retorna: (Diagnóstico, Explicação, Instrução, Frase de Efeito)
    """
    
    # Converte a string "HH:MM" para um número inteiro de hora para as regras funcionarem
    try:
        h = int(hora_atual_str.split(':')[0])
    except:
        h = datetime.now().hour
    hora_atual = h
    
      # --- SEUS TEXTOS E REGRAS ORIGINAIS (MANTIDOS 100% INTACTOS) ---
    madrugada = (0 <= hora_atual <= 5)
    tardeNoite = (18 <= hora_atual <= 23)
    hora_refeicao = (7 <= hora_atual <= 9) or (11 <= hora_atual <= 14) or (18 <= hora_atual <= 21)


    # --- BLOCO DE MANEJOS DO EXOSQUELETO MENTAL ---

    if cat_match == "medo":
        if intensidade >= 7: 
            return ("O sistema travou por excesso de ameaças detectadas.", 
                    "O hardware identificou um risco real ou não e cortou a energia dos movimentos para ampliar a proteção.", 
                    "Não force ação. Reduza luz, som e estímulos. Espere o sistema processar, equalizar e sinalizar segurança.", 
                    "Paralisar, às vezes é defesa, não falha. DESCANSE!")
        else: 
            return ("Alerta de Hesitação / Bug Social.", 
                    "Sensor de ameaças focado na interpretação de outros usuários ou ambiente.", 
                    "As informações podem estar sendo processadas de forma corrompida agora. Você está seguro.", 
                    "O ruído é apenas o medo. Mantenha o monitoramento.")

    elif cat_match == "raiva":
        return ("Superaquecimento Crítico.", 
                "Energia agressiva detectada buscando saída imediata após erro ou injustiça.", 
                "Descarregue o excesso fisicamente (aperte algo, pule). Resfrie o sistema antes que ele queime os cabos.", 
                "RESFRIE O SISTEMA! Não tome decisões com a CPU quente.")

    elif cat_match == "hiperfoco":
        if h >= 21 or madrugada: 
            return (f"Hiperfoco às {h}h (Risco de Insônia).", 
                    "Uso prolongado de CPU em horário de baixa energia química. Essa produção pode custar caro amanhã.", 
                    "Diminua a carga da atividade atual e inicie o planejamento mental de transição para o descanso.", 
                    "Gotham está segura! Você não é o Batman, vá descansar. VOCÊ NÃO É UM MORCEGO!")
        elif intensidade >= 7: 
            return (f"Processador em 100% (Modo Túnel) às {h}h.", 
                    "Atenção total em uma única tarefa, ignorando todos os alertas de manutenção do corpo.", 
                    "Check de sede, fome, cansaço e postura agora! Agende alarmes para pausas.", 
                    "Grandes poderes trazem grandes responsabilidades. SE ORGANIZE!")
        else: 
            return ("Produtividade Elevada.", 
                    "Sistema otimizado para a tarefa atual.", 
                    "Mantenha o scanner ligado para evitar exaustão precoce e salve o progresso.", 
                    "Bom trabalho. Evolua para a próxima fase.")

    elif cat_match == "looping":
        if madrugada or intensidade >= 7: 
            return (f"Loop Crítico de Madrugada ({h}h).", 
                    "A mente tenta reprocessar um erro antigo num horário de baixa energia química, gerando arquivos corrompidos.", 
                    "O sistema não resolve problemas após as 0h. Beba água, force um reset físico (banho) e saia da tela.", 
                    "Ficar rodando código com erro não conserta arquivo corrompido. VOLTE À REALIDADE!")
        else: 
            return ("Ruminação / Loop do Passado.", 
                    "Tentando editar logs de eventos que já foram fechados (apenas leitura).", 
                    "O passado é código apenas para leitura. Saia desse arquivo e mude para uma tarefa manual.", 
                    "Pare de rodar um script que só retorna erro! Mude a programação.")

    elif cat_match == "ansiedade":
        if intensidade >= 7: 
            return ("Pânico / Modo de Fuga Ativado.", 
                    "O sistema detectou uma ameaça crítica e ativou descarga química total (fuga ou luta).", 
                    "FOCO NO HARDWARE: Toque em algo gelado. Respire contando até 4. Volte para o presente.", 
                    "Isso é uma descarga química, não é um fato real. VOCÊ ESTÁ SEGURO!")
        else: 
            return ("Muitas Abas Abertas / Ansiedade.", 
                    "Excesso de processamento tentando prever múltiplas variáveis simultâneas.", 
                    "Feche as tarefas secundárias. Foque apenas no que é vital para o sistema agora.", 
                    "Reduza preocupações. Aumente o foco. O presente está aqui.")

    elif cat_match == "tristeza":
        if intensidade >= 7: 
            return ("Tristeza Profunda / Sobrecarga de Pressão.", 
                    "O reservatório emocional atingiu o limite crítico de carga.", 
                    "Permita o choro. Busque um ambiente seguro e reduza a pressão externa.", 
                    "Às vezes 'lavar' o sistema evita danos maiores. LIBERE A PRESSÃO!")
        else: 
            return ("Angústia Leve.", 
                    "Existe um dado não processado sobre uma interação social ou acontecimento.", 
                    "Tente escrever o que ficou pendente ou apenas observe os pensamentos sem julgamento.", 
                    "Pequenos tópicos também precisam de processamento.")

    elif cat_match == "sensorial":
        if intensidade >= 6: 
            return ("Agitação Sensorial Crítica.", 
                    "O ambiente está enviando dados demais e o sistema está superaquecendo.", 
                    "Use atividades corporais para liberar esta energia acumulada que esta querendo sair.\nOU\nMude para um lugar silencioso e escuro imediatamente, e aguarde seu sistema se estabilizar.", 
                    "Se o excesso de estimulos sobregarrega, descarregar (da forma que preferir) pode ser a melhor resposta.")
        else: 
            return ("Agitação Moderada / Falha no Filtro.", 
                    "O hardware está dando prioridade máxima para ruídos ou estímulos irrelevantes.", 
                    "Reduza a carga de inputs. Use música de conforto ou diminua as luzes.", 
                    "Filtro de ruídos em manutenção. Busque conforto.")

    elif cat_match == "shutdown":
        return ("Shutdown / Proteção de Hardware.", 
                "O sistema se desligou do mundo externo para evitar danos permanentes (pico de energia).", 
                "Não force o retorno. Fique em silêncio e escuro absoluto até o reset automático.", 
                "Protocolos de segurança ativos. Aguarde o reset.")

    elif cat_match == "dissociacao":
        return ("Sinal de Wi-Fi Perdido / Dissociação.", 
                "O hardware desconectou da base para se proteger de picos de energia ou traumas.", 
                "Toque em texturas físicas. Sinta o peso do seu corpo. Tente se ater ao 'tato'.", 
                "RECONECTANDO COM O CHÃO... Aguarde.")

    elif cat_match == "burnout":
        return ("CURTO-CIRCUITO TOTAL (Burnout).", 
                "Placa-mãe superaquecida por uso prolongado acima da capacidade de processamento.", 
                "DESLIGUE TUDO NA TOMADA. Isolamento e repouso total obrigatório por tempo indeterminado.", 
                "MODO DE SEGURANÇA OBRIGATÓRIO. Não tente reiniciar agora.")

    elif cat_match == "fome":
        if hora_refeicao: 
            return (f"Combustível Crítico ({h}h).", 
                    "O sistema consumiu as energias e atingiu o horário previsto de reabastecimento.", 
                    "Pausa obrigatória para nutrição. Priorize proteínas e carboidratos.", 
                    "Sem combustível o motor para. ABASTEÇA-SE!")
        else: 
            return (f"Fome fora de hora ({h}h).", 
                    "Gasto alto de CPU consumiu mais glicose que o esperado ou alimentação prévia insuficiente.", 
                    "Busque um snack saudável para estabilizar o sistema de energia. Nutra-se.", 
                    "Alimentação é sobre nutrição, não só mastigação. NUTRA-SE!")

    elif cat_match == "sede":
        return ("Hidratação Crítica.", 
                "Falha nos sensores de hidratação. O motor está superaquecendo e colapsando.", 
                "Pausa obrigatória para água. Hidrate os circuitos agora e nas próximas horas.", 
                "Sem água, o sistema trava. HIDRATE-SE!")

    elif cat_match == "cansaco":
        if (h >= 18 or madrugada) or intensidade >= 7: 
            return (f"Esgotamento de Fim de Dia ({h}h).", 
                    "Capacitores sobrecarregados pelo excesso de estímulos diários. Hora do reset total.", 
                    "Pare tudo, vá para o escuro. Inicie protocolo de sono profundo e silêncio.", 
                    "Descanso é cuidado, não punição. CUIDE-SE!")
        else: 
            return (f"Cansaço Diurno ({h}h).", 
                    "Superaquecimento precoce por excesso de estímulos ou sendo anterior de má qualidade.", 
                    "Soneca de 15 min ou 15 min de silêncio total para resfriar a CPU.", 
                    "Descanso também é progresso. Resfrie o sistema.")

    elif cat_match == "stimming":
        return ("Necessidade de Autorregulação.", 
                "O corpo precisa de movimentos repetitivos para organizar o sistema nervoso.", 
                "Não reprima. Use fidget toys ou movimentos naturais para equalizar a energia.", 
                "Stimming é manutenção do sistema, não bug!")

    elif cat_match == "inercia":
        return ("Falha na Inicialização / Inércia.", 
                "Dificuldade de converter comando mental em ação física. Muro invisível detectado.", 
                "Execute micro-tarefas de 30 segundos. Dê um 'tranco' manual no motor.", 
                "Dê um tranco no motor e saia da inércia.")

    elif cat_match == "verbal": 
        return ("Modo Não Verbal.", 
                "Módulo de fala offline. A bateria zerou e o sistema cortou o áudio para poupar energia.", 
                "Use escrita, gestos ou o silêncio. Não force a saída de áudio agora.", 
                "Módulo de áudio em auto-recarga. Aguarde.")

    elif cat_match == "injustica":
        return ("Bug de Justiça / Indignação Moral.", 
                "Quebra de protocolos éticos externos detectada. Violação de lógica social.", 
                "Você não é o admin do mundo. Foque no seu próprio código e ética agora.", 
                "Foque no seu código. O mundo tem bugs que você não pode consertar.")

    elif cat_match == "curiosidade":
        return ("Modo Exploração Ativo.", 
                "Desejo de novos dados. Seu processador está buscando atividade estimulante.", 
                "Siga o fluxo da informação, pesquise e documente o que aprender.", 
                "EXPANDINDO O BANCO DE DATOS. Sistema em evolução.")

    elif cat_match == "paz":
        return ("Homeostase / Sistema Estável.", 
                "Sensores em equilíbrio ideal. Baixa latência e silêncio interno.", 
                "Registre esse estado. Aproveite a estabilidade para tarefas de baixa pressão.", 
                "CONDIÇÕES IDEAIS. Sistema em ordem.")

    elif cat_match == "rejeicao":
        return ("Alerta de RSD (Sensibilidade à Rejeição).", 
                "O sistema interpretou um input social como exclusão catastrófica.", 
                "Verifique os fatos: existe prova real de rejeição ou é um erro de leitura do sensor? Saia do social por 10 min.", 
                "A opinião alheia não altera seu código-fonte. ESTABILIZE-SE.")

    elif cat_match == "empolgada":
        return ("Pico de Dopamina / Sistema em Festa.", 
                "Energia de recompensa em nível máximo. Grande chance de impulsividade.", 
                "Aproveite a onda para tarefas difíceis, mas evite compras ou compromissos de longo prazo agora.", 
                "SISTEMA EM ALTA. Use essa energia com inteligência!")

    elif cat_match == "conexao":
        return ("Sincronia de Sistema / Vínculo.", 
                "O hardware encontrou um terminal compatível e o intercâmbio de dados é seguro.", 
                "Permita o download de afeto. Valide a presença do outro e registre este log positivo.", 
                "CONEXÃO ESTABELECIDA. O sistema não está sozinho.")

    elif cat_match == "alivio":
        return ("Tarefa Concluída / Limpeza de Cache.", 
                "Uma carga pesada foi removida da fila de processamento. Tensão dissipada.", 
                "Respire fundo e sinta o espaço livre no HD mental antes de carregar a próxima tarefa.", 
                "LOG DE SUCESSO. Ufa!")

    elif cat_match == "afeto":
        return ("Aquecimento de Núcleo / Ternura.", 
                "Processamento de dados positivos sobre terceiros ou sobre si mesmo.", 
                "Deixe a temperatura subir. Aproveite a sensação física sem tentar explicá-la logicamente.", 
                "HARDWARE AQUECIDO COM SUCESSO. Sinta o carinho.")

    elif cat_match == "confusao":
        return ("Erro de Processamento / Dados Fragmentados.", 
                "Muitos inputs simultâneos ou instruções contraditórias recebidas.", 
                "Pare a entrada de dados. Peça para repetirem devagar ou divida o problema em partes menores.", 
                "CÉREBRO FRITO. Reinicie a explicação por partes.")

    elif cat_match == "frustracao":
        return ("Loop de Erro / Impedimento de Execução.", 
                "O comando foi enviado, mas o resultado esperado não foi atingido repetidas vezes.", 
                "Mude de tarefa por 5 minutos. O sistema precisa limpar o erro antes de tentar novamente.", 
                "NÃO FORCE O SCRIPT. Tente uma abordagem diferente depois.")

    elif cat_match == "solidao":
        return ("Sinal de Rede Fraco / Isolamento.", 
                "O sistema detectou falta de intercâmbio de dados sociais necessários para manutenção.", 
                "Busque conexão com algo: um animal, uma música, ou envie uma mensagem curta para um terminal confiável.", 
                "BUSCANDO REDE... Tente uma conexão segura.")

    elif cat_match == "orgulho":
        return ("Validação de Build / Conquista Própria.", 
                "Reconhecimento interno de que o código rodou perfeitamente após esforço.", 
                "Salve esse estado. Você superou bugs e entregou o resultado. Comemore.", 
                "VERSÃO ESTÁVEL ALCANÇADA. Você é capaz!")

    elif cat_match == "gratidao":
        return ("Otimização de Logs Positivos.", 
                "O sistema está focando nos recursos disponíveis em vez das falhas.", 
                "Anote o motivo dessa gratidão para consultas em momentos de 'burnout' ou 'tristeza'.", 
                "SISTEMA VALORIZADO. Continue assim.")

    elif cat_match == "culpa":
        return ("Alerta de Erro Crítico Interno.", 
                "O sistema está punindo o hardware por um log de evento passado.", 
                "Analise: houve dano real? Se sim, tente o reparo. Se não, encerre esse processo repetitivo.", 
                "REPARAÇÃO, NÃO PUNIÇÃO. Corrija o código e siga.")

    elif cat_match == "tedio":
        return ("Modo Ocioso / Falta de Estímulo.", 
                "Baixa atividade na CPU gerando inquietação e busca por ruído.", 
                "Inicie uma tarefa de 'curiosidade' ou uma manutenção física leve (limpeza) para gerar sinal.", 
                "SISTEMA EM STANDBY. Busque um novo input.")

    elif cat_match == "mal_estar":
        return ("Alerta Geral de Sensores Físicos.", 
                "O hardware reporta instabilidade não específica (náusea ou tontura).", 
                "Sente-se ou deite-se. Verifique temperatura e respiração. O sistema precisa de repouso físico imediato.", 
                "MODO DE PRESERVAÇÃO FÍSICA. Vá com calma.")

    elif cat_match == "dor_cabeca":
        return ("Pressão Interna no Processador.", 
                "Carga excessiva de luz, som ou processamento mental gerando dor física.", 
                "Escuro, silêncio e hidratação. Desligue as telas imediatamente.", 
                "LIMITE DE PROCESSAMENTO ATINGIDO. Desligue os monitores.")

    elif cat_match == "nojo":
        return ("Rejeição de Input Sensorial.", 
                "O sensor detectou uma textura, cheiro ou ideia incompatível com o sistema.", 
                "Afaste-se do estímulo. Lave o que for necessário. Respeite o limite do seu hardware.", 
                "TEXTURA INVÁLIDA. Remova o objeto do ambiente.")

    return ("Sinal não identificado.", 
            f"Um novo estado foi detectado às {h}h, mas ainda não possui um manual específico.", 
            "Observe os sintomas físicos e anote para criarmos um novo 'case' no futuro.", 
            "Continue aprendendo sobre seu sistema. VAMOS IDENTIFICAR ESSE BUG!")