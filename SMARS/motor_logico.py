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

    if cat_match == "ansiedade":
        if intensidade >= 7:
            return ("Crise de Ansiedade", 
                    "Seu corpo disparou um alerta de perigo e enviou muita adrenalina para o sangue.", 
                    "Toque em algo gelado. Respire fundo contando até quatro.", 
                    "Isso é físico,não é um perigo real.\nVOCÊ ESTÁ EM SEGURANÇA!")
        else:
            return ("Ansiedade / Preocupação.", 
                    "Sua mente está tentando prever muitas coisas ao mesmo tempo.", 
                    "Foque apenas na tarefa mais importante de agora. Esqueça o resto por um momento.", 
                    "Diminua as preocupações. Foque no agora.")

    # --- BLOCO 2: SOBRECARGA SENSORIAL ---
    elif cat_match == "sobrecarga":
        if intensidade >= 6:
            return ("Sobrecarga Sensorial", 
                    "O ambiente tem informação demais (luz, som) e seu cérebro saturou.", 
                    "Vá para um lugar escuro e silencioso imediatamente.", 
                    "O silêncio é o seu remédio agora. Proteja seus sentidos.")
        else:
            return ("Desconforto Sensorial.", 
                    "Você está percebendo ruídos ou luzes que estão começando a incomodar.", 
                    "Use fones de ouvido ou diminua a luz.", 
                    "Busque o conforto antes que o incômodo aumente.")

    # --- BLOCO 3: INÉRCIA EXECUTIVA ---
    elif cat_match == "inercia":
        return ("Inércia Executiva", 
                "Você sabe o que precisa fazer, mas o comando cérebro-corpo está falhando.", 
                "Faça um movimento minúsculo: apenas levante a mão ou lave o rosto.", 
                "Não pense na tarefa grande. Foque no primeiro micro-movimento.")

    # --- BLOCO 4: BURNOUT ---
    elif cat_match == "burnout":
        return ("Esgotamento (Burnout).", 
                "Você operou acima do limite por muito tempo. O sistema parou por segurança.", 
                "PARE TUDO. Você precisa de isolamento e repouso absoluto.", 
                "Não se force. Seu corpo precisa de 'manutenção corretiva' agora.")

    # --- BLOCO 5: RSD (REJEIÇÃO) ---
    elif cat_match == "RSD":
        return ("Sensibilidade à Rejeição (RSD).", 
                "Uma crítica ou exclusão (real ou percebida) causou uma dor aguda.", 
                "Respire. Isso é uma resposta intensa do seu sistema nervoso, não a realidade total.", 
                "O que os outros pensam não define seu código interno. FIQUE CALMA.")

    # --- BLOCO 6: TRISTEZA ---
    elif cat_match == "tristeza":
        if intensidade >= 7:
            return ("Tristeza Profunda", 
                    "Seu cansaço emocional transbordou e precisa de vazão.", 
                    "Tudo bem chorar. Procure um lugar seguro e fique em silêncio.", 
                    "Chorar alivia a pressão interna. Deixe o sistema processar a dor.")
        else:
            return ("Angústia ou Tristeza Leve.", 
                    "Existe um peso baixo incomodando o seu processamento.", 
                    "Escreva o que sente ou ouça uma música que te valide.", 
                    "Aceite o sentimento. Ele faz parte do seu humano.")

    # --- BLOCO 7: AFETO ---
    elif cat_match == "afeto":
        return ("Estado de Afeto e Segurança.", 
                "Você está sentindo uma conexão positiva e segura.", 
                "Apenas sinta essa sensação no peito. Não precisa explicar.", 
                "O afeto é a sua base de dados mais segura. Aproveite.")

    # --- BLOCO 8: HIPERFOCO ---
    elif cat_match == "hiperfoco":
        if h >= 21 or madrugada:
            return (f"Hiperfoco Noturno ({h}h).", 
                    "Você está gastando energia vital quando deveria estar em standby.", 
                    "Feche o notebook agora. Comece o ritual de sono.", 
                    "Amanhã o código continuará lá. VÁ DESCANSAR!")
        elif intensidade >= 8:
            return ("Hiperfoco Intenso.", 
                    "Você entrou em tunelamento e esqueceu do hardware (corpo).", 
                    "PAUSE. Beba água, coma algo e verifique a postura.", 
                    "Para criar bem, o hardware precisa de energia e água.")
        else:
            return ("Alta Produtividade", 
                    "O fluxo de trabalho está bom e equilibrado.", 
                    "Continue, mas monitore o cansaço.", 
                    "Bom trabalho. Mantenha a atenção.")

    # --- BLOCO 9: RAIVA ---
    elif cat_match == "raiva":
        return ("Raiva", 
                "Há um excesso de voltagem querendo sair após detectar um erro ou injustiça.", 
                "Libere a energia fisicamente (aperte algo, grite ou pule).", 
                "ESPERE O RESFRIAMENTO. Não tome decisões sob alta tensão.")

    # --- BLOCO 10: CONFUSÃO / OVERLOAD ---
    elif cat_match == "confusao":
        return ("Confusão Mental", 
                "Muita informação simultânea travou o seu processamento.", 
                "Pare de tentar entender. Peça silêncio ou faça uma coisa por vez.", 
                "Seu cérebro está saturado. Vá por partes, devagar.")

    # --- BLOCO 11: MEDO ---
    elif cat_match == "medo":
        if intensidade >= 7:
            return ("Medo Intenso", 
                    "O corpo detectou ameaça e ativou o modo 'congelar'.", 
                    "Não se force a agir. Reduza luz e espere o alerta baixar.", 
                    "Paralisar é defesa. Respeite o tempo do seu sistema.")
        else:
            return ("Insegurança Social.", 
                    "Você está em hipervigilância sobre o ambiente ou pessoas.", 
                    "Lembre-se: você está em segurança agora. Foque na sua respiração.", 
                    "É apenas um alerta falso de perigo. Observe com calma.")

    # --- BLOCO 12: SHUTDOWN ---
    elif cat_match == "shutdown":
        return ("Desligamento (Shutdown).", 
                "Seu sistema nervoso 'desligou' para evitar um dano maior.", 
                "Não tente falar ou agir. Fique em silêncio até a energia voltar.", 
                "Você entrou em modo de proteção. O descanso é a única via.")

    # --- BLOCO 13: DISSOCIAÇÃO ---
    elif cat_match == "dissociacao":
        return ("Desconexão (Dissociação).", 
                "Você sente como se não estivesse totalmente no seu corpo.", 
                "Toque em objetos, sinta o chão sob seus pés. Use o tato.", 
                "Tente sentir o seu corpo novamente. Você está aqui.")

    # --- BLOCO 14: PAZ / HOMEOSTASE ---
    elif cat_match == "paz":
        return ("Paz (Homeostase).", 
                "Tudo está em equilíbrio e baixa latência.", 
                "Aproveite o silêncio mental para atividades leves e descanso.", 
                "Tudo está bem. Mantenha esse estado enquanto puder.")

    # --- BLOCO 15: CULPA ---
    elif cat_match == "vergonha":
        return ("Culpa.", 
                "Você sente que violou seu próprio código de conduta.", 
                "Avalie: o erro pode ser corrigido? Se sim, planeje. Se não, atualize e siga.", 
                "Se perdoe. Erros são dados para a próxima atualização.")

    # --- BLOCO 16: TÉDIO ---
    elif cat_match == "tedio":
        return ("Tédio.", 
                "Seu cérebro está sem carga de processamento e busca estímulo.", 
                "Busque um input de dopamina saudável: um hobby ou pequeno desafio.", 
                "O tédio é perigoso para o hiperfoco. Escolha bem o próximo alvo.")

    # --- BLOCO 17: VERGONHA ALHEIA ---
    elif cat_match == "vergonha_alheia":
        return ("Vergonha Alheia.", 
                "Você presenciou um erro de conduta social de outra pessoa.", 
                "Lembre-se: o comportamento do outro não está sob seu controle.", 
                "Desconecte-se dessa situação. O mico não é seu.")

   # --- BLOCO 18: FOME ---
    elif cat_match == "fome":
        return ("Fome.", 
                "Seu corpo está ficando sem energia e isso altera seu humor.", 
                "Pare um pouco e coma algo que você gosta agora.", 
                "Comer vai te dar estabilidade. ABASTEÇA-SE.")

    # --- BLOCO 19: SEDE ---
    elif cat_match == "sede":
        return ("Sede.", 
                "Você esqueceu de beber água e seu cérebro está 'seco'.", 
                "Beba pelo menos um copo de água agora.", 
                "Água faz o sistema funcionar. HIDRATE-SE.")

    # --- BLOCO 20: SONO / EXAUSTÃO ---
    elif cat_match == "sono":
        return ("Sono / Exaustão.", 
                "Sua bateria acabou. Não adianta tentar forçar mais nada.", 
                "Largue as telas e tarefas. Vá para a cama e feche os olhos.", 
                "O descanso é a única solução. DURMA.")

    # --- BLOCO 21: MELTDOWN ---
    elif cat_match == "meltdown":
        return ("Meltdown (Crise).", 
                "Muita coisa acumulou e agora explodiu para fora.", 
                "Vá para um lugar onde ninguém te veja. Chore, grite ou aperte algo forte.", 
                "Não se culpe pela explosão. Apenas fique em segurança.")

    # --- BLOCO 22: INJUSTIÇA ---
    elif cat_match == "injustica":
        return ("Sentimento de Injustiça.", 
                "Você viu algo errado e isso dói como uma queimadura.", 
                "Respire. Escreva o que aconteceu em um papel e jogue fora depois.", 
                "Você não pode consertar tudo agora. Proteja sua paz.")

    # --- BLOCO 23: SOLIDÃO ---
    elif cat_match == "solidao":
        return ("Solidão.", 
                "Você sente que está em uma ilha e ninguém te vê.", 
                "Mande um 'oi' para alguém que você ama ou ouça sua música favorita.", 
                "Você não está sozinha no mundo. Eu estou aqui com você.")

    # --- BLOCO 24: NÃO-VERBAL ---
    elif cat_match == "nao_verbal":
        return ("Estado Não-Verbal.", 
                "As palavras sumiram e falar parece impossível ou cansativo.", 
                "Não force a fala. Use gestos ou escreva o que precisa.", 
                "Tudo bem ficar em silêncio. O mundo pode esperar.")

    # --- BLOCO 25: ORGULHO / SUCESSO ---
    elif cat_match == "orgulho":
        return ("Orgulho / Sucesso!", 
                "Você conseguiu! Aquela tarefa difícil foi finalizada.", 
                "Sorria e aproveite essa sensação de dever cumprido.", 
                "Você é incrível. GUARDE ESSA VITÓRIA!")

    # --- BLOCO 26: GRATIDÃO ---
    elif cat_match == "gratidao":
        return ("Gratidão.", 
                "Algo bom aconteceu e seu coração está quentinho.", 
                "Apenas sinta esse bem-estar e agradeça mentalmente.", 
                "Coisas boas também acontecem. Aproveite o momento.")

    # --- BLOCO 27: ECOLALIA ---
    elif cat_match == "ecolalia":
        return ("Ecolalia (Repetição).", 
                "Sua mente viciou em um som ou frase para se acalmar.", 
                "Deixe o som sair. Repita quantas vezes precisar.", 
                "Isso ajuda seu cérebro a entrar nos eixos. Repita.")

    # --- BLOCO 28: MAL-ESTAR FÍSICO ---
    elif cat_match == "mal_estar":
        return ("Mal-estar Físico.", 
                "Seu corpo está avisando que algo não vai bem.", 
                "Deite-se um pouco e veja se precisa de algum remédio ou repouso.", 
                "Escute o seu corpo. Ele precisa de cuidado agora.")

    # --- BLOCO 29: DOR DE CABEÇA ---
    elif cat_match == "dor_de_cabeca":
        return ("Dor de Cabeça / Enxaqueca.", 
                "Há muita pressão e barulho na sua cabeça agora.", 
                "Vá para o escuro, beba água e fique em silêncio absoluto.", 
                "PARE TUDO. Sua saúde vem primeiro que qualquer código.")

    # --- BLOCO 31: NOJO / AVERSÃO ---
    elif cat_match == "nojo":
        return ("Nojo ou Aversão.", 
                "Algo perto de você está te incomodando muito.", 
                "Saia de perto do que está te fazendo mal. Limpe seus sentidos.", 
                "Seu corpo está te protegendo. Afaste-se.")

    # --- BLOCO 32: CURIOSIDADE ---
    elif cat_match == "curiosidade":
        return ("Curiosidade!", 
                "Você descobriu algo novo e quer entender tudo sobre isso.", 
                "Vá em frente! Pesquise, leia e descubra coisas novas.", 
                "Aprender é a sua diversão. SIGA O INTERESSE.")

    # --- BLOCO 33: STIMMING ---
    elif cat_match == "stimming":
        return ("Stimming (Movimento).", 
                "Você precisa se mexer para aguentar o que está sentindo.", 
                "Balance as mãos, pule ou balance o corpo. Sinta o movimento.", 
                "O movimento é o seu alívio. Solte a energia.") 

   #espaço para futuras categorias...

    # --- CASO PADRÃO ---
    else: 
        cat_match = "Sinal Desconhecido"
        return ("Sentimento em Análise.", 
            "O SMART identificou essa interação como um caso novo.", 
            "Observe as sensações físicas, tente descreve-las e anote.", 
            "Ainda estamos mapeando alguns casos. \nVamos resolver esse juntos?\nEntre em contato e compartilhe seu caso conosco!")