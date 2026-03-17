import tkinter as tk
from tkinter import simpledialog, messagebox
import os
from datetime import datetime
import varredura_fisica 
import dicionario 

def obter_relatorio(cat_match, intensidade, hora_atual):
    madrugada = (0 <= hora_atual <= 5)
    tardeNoite = (18 <= hora_atual <= 23)
    hora_refeicao = (7 <= hora_atual <= 9) or (11 <= hora_atual <= 14) or (18 <= hora_atual <= 21)
    h = hora_atual

    # --- DICIONÁRIO DE SENTIMENTOS (MANEJO E DIAGNÓSTICO) ---
    
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
                    "Use fones de ouvido ou mude para um lugar silencioso e escuro IMEDIATAMENTE.", 
                    "Se o excesso de sons questiona o sistema, silenciar é a melhor resposta.")
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
                    "Superaquecimento precoce por excesso de estímulos ou sono anterior de má qualidade.", 
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

    # Mensagem padrão para casos não mapeados
    return ("Sinal não identificado.", 
            f"Um novo estado foi detectado às {h}h, mas ainda não possui um manual específico.", 
            "Observe os sintomas físicos e anote para criarmos um novo 'case' no futuro.", 
            "Continue aprendendo sobre seu sistema. VAMOS IDENTIFICAR ESSE BUG!")
def ponte_link(sentimento_varredura):
   
    dicionario_ponte = {
        "FOME": "fome", 
        "SEDE": "sede", 
        "SONO / EXAUSTÃO": "cansaco",
        "MAL-ESTAR FÍSICO": "mal_estar", 
        "DOR DE CABEÇA / ENXAQUECA": "dor_cabeca",
        "MELTDOWN (CRISE EXTERNA)": "sensorial", 
        "SHUTDOWN (CRISE INTERNA)": "shutdown",
        "SOBRECARGA SENSORIAL": "sensorial", 
        "BURNOUT (ESGOTAMENTO)": "burnout",
        "DISSOCIAÇÃO": "dissociacao", 
        "INÉRCIA EXECUTIVA": "inercia", 
        "HIPERFOCO / EMPOLGAÇÃO": "hiperfoco",
        "CONFUSÃO / OVERLOAD COGNITIVO": "confusao", 
        "ECOLALIA (REPETIÇÃO)": "looping", 
        "CURIOSIDADE": "curiosidade",
        "ANSIEDADE / PÂNICO": "ansiedade", 
        "RSD (DISFORIA SENSÍVEL À REJEIÇÃO)": "rejeicao", 
        "TRISTEZA / ANGÚSTIA": "tristeza", 
        "AFETO / AMOR": "afeto",
        "RAIVA": "raiva", 
        "MEDO / INSEGURANÇA": "medo", 
        "FRUSTRAÇÃO": "frustracao", 
        "SOLIDÃO": "solidao", 
        "ORGULHO / SUCESSO": "orgulho", 
        "GRATIDÃO": "gratidao", 
        "PAZ / HOMEOSTASE": "paz", 
        "INJUSTIÇA": "injustica", 
        "NOJO / AVERSÃO": "nojo",
        "STIMMING (AUTORREGULAÇÃO)": "stimming"
    }
    
    # Normalizamos a entrada para evitar erros de espaços ou letras minúsculas
    busca = sentimento_varredura.strip().upper()
    return dicionario_ponte.get(busca, "outro")
def iniciar_app():
    root = tk.Tk()
    root.withdraw()
    agora = datetime.now()
    
    sabendo = messagebox.askyesno("Scanner", "Você sabe o que está sentindo agora?")
    cat_match = None
    intensidade = 5

    if sabendo:
        entrada = simpledialog.askstring("Manejo", "O que você está sentindo?")
        if entrada:
            intensidade = simpledialog.askinteger("Intensidade", "De 1 a 10:", minvalue=1, maxvalue=10) or 5
            cat_match = dicionario.buscar_sentimento(entrada)
            if not cat_match:
                cat_match = dicionario.aprender_novo_termo(entrada) 
    else:
        sinal_fisico = simpledialog.askstring("Scanner", "Quais sensações físicas você percebe?")
        if sinal_fisico:
            detectado = varredura_fisica.tradutor_fisico(sinal_fisico)
            cat_match = ponte_link(detectado)

    if cat_match:
        diag, expl, instr, frase = obter_relatorio(cat_match, intensidade, agora.hour)
        relatorio_texto = f"DIAGNÓSTICO: {diag}\n\nPOR QUE OCORRE: {expl}\n\nAÇÃO DE MANEJO: {instr}\n\nSISTEMA: {frase}"
        messagebox.showinfo("Relatório de Sistema", relatorio_texto)
            
    root.destroy()

if __name__ == "__main__":
    iniciar_app()
