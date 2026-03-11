
// Este código foi construído como um "Exoesqueleto Mental" 
// serve para traduzir sensações físicas e mentais que o próprio corpo às vezes não consegue nomear sozinho (Alexitimia)

//==============================================================================================================================

//  AQUI O USUÁRIO NÃO DEVE MEXER

//===============================================================================================================================

    // Aqui vamos criar uma constante para termos o registro de data e hora de cada diagnóstico executado
    // o intuito é manter tudo registrado e organizado
    // para no futuro poder desenvolver e manter um banco de dados com os diagnósticos anteriores 
    // para que o sistema possa aprender com o tempo e identificar padrões, gatilhos, etc

    const dataEHora = new Date().toLocaleString();


//=========================================================================================================================================================

// Esta é a função principal
// ela é responsavel por entregar pro nosso sistema tudo que ele precisa saber pra poder ajudar
//  O nome 'investigarBugHumano' indica que estamos abrindo uma sessão de diagnóstico técnico sobre o nosso próprio estado

const investigarBugHumano = (sintomaDetectado , intensidade, h = new Date().getHours()) => {

    // nesse "new Date" puxamos no sitema o momento exato em que o codigo esta rodando
    // no ".getHours()" puxamos só a hora, e temos um numero inteiro entre 0 e 23
    // ou seja, o codigo sabe o horário exato de agora, e usa essa informação


    // O 'switch' funciona como uma central de triagem 
    // ele vai receber o que você está sentindo e procurar na lista qual é o protocolo de resolução adequado para aquele caso espefico
    
    // Aqui tambem criamos uma normalização (mandamos todas as letras ficarem minusculas e tirar espaços desencessarios) 
    // para evitar erros de leitura de código causados pela digitação do usuário

    const entrada = sintomaDetectado.toLowerCase().trim();

    // Definimos os contextos de acorodo com o horário, para o sistema poder diferenciar
    // Até por que, sentir coisas em horarios diferentes do dia, podem significar sentimentos diferentes

    const madrugada = (h >= 0 && h <= 5);
    const horaRefeicao = (h >= 7 && h <= 9) || (h >= 11 && h <= 14) || (h >= 18 && h <= 21);
    const tardeNoite = (h >= 20|| madrugada);


    switch (entrada) {

//=========================================================================================================================================================
        
        //  SETOR DE SOFTWARE ( MENTE ) 

        case "medo paralisante":
            // O 'return' é a resposta final que o sistema cospe para fora da gaveta
            return {
                diagnostico: "O sistema travou por excesso de ameaças detectadas.",
                explicacao: "O hardware identificou um risco real ou não e cortou a energia dos movimentos para ampliar a proteção.",
                instrucao: "Não force ação. Reduza luz, som e estimulos. Espere o sistema  processar, equalizar e sinalizar segurança.",
                frase: "Paralisar, as vezes é defesa, não falha. \n DESCANSE!"
            };

        case "hiperfoco":
            // vamos afunilar ainda mais os auxilios refentes ao hiperfoco
            //criando possibilidades de analise de horario, tempo de foco, etc

            if ( h >= 21 || madrugada ) {
                return { 
                    diagnostico: `Hiperfoco detectado às ${h}h, cuidado, 'essa produção' pode custar caro amanhã.`,
                    explicacao: "Neste momento, você esta em foco, porem precisa descansar, comece o processo de transição.",
                    instrucao: "Diminua a carga da atividade atual, inicie o planejamento mental de atividades substitutivas e mais relaxantes, se permita descansar",
                    frase: "O hiperfoco é tipo um superpoder, mas você não é o batman, vai descansar gotham está segura! \n VOCÊ NÂO È UM MORCEGO!"
                };
            } else {
                return {
                    diagnostico: `Processador operando em 100% de capacidade, agora são ${h}h e seu cerébro está voltado a somente uma única tarefa.`,
                    explicacao: "A atenção está em modo túnel, ignorando todos os alertas de manutenção do corpo.",
                    instrucao: "Agende alarmes regulares para checagem de sede, fome, cansço e postura. Planeje o 'manejo' da atividade.",
                    frase: "O hiperfoco pode ser quase um superpoder, mas, como dizem em homem-aranha, grandes poderes vem com grandes responsabilidades. \n SE ORGANIZE! SE CUIDE!"
                };
            }

        case "ruminacao":
        case "pensamento em looping":
            if (madrugada) {
                return {
                    diagnostico: `Loop infinito de processamento às ${h}h (Bug Crítico de Madrugada).`,
                    explicacao: "A mente tenta reprocessar um erro antigo num horário de baixa energia química. Isso gera arquivos corrompidos.",
                    instrucao: "O sistema não resolve problemas após as 0h, só os amplia. Beba água, descanse, force o reset.",
                    frase: "Ficar rodando código com erro não conserta arquivo corrompido, principalmente de madrugada, né? \n VOLTE Á REALIDADE!"
                };
            } else {
                return {
                    diagnostico: "Ruminação / Loop do Passado.",
                    explicacao: "Tentando editar logs de eventos que já foram fechados.",
                    instrucao: "O passado é codigo apenas para leitura. Saia desse arquivo.",
                    frase: "Pare de rodar um script que só retorna erro! Mude a programação"
                };
            }

            case "análise de padrões sociais":
            return {
                diagnostico: "Scanner de Padrões Ativo.",
                explicacao: "Tentativas lógicas de entender comportamentos humanos complexos.",
                instrucao: "Finalize a análise, salve o que aprendeu e mude o foco.",
                frase: "Padrão identificado. Conteúdo aprendido. Evolua para a próxima fase."
            };

        case "olhar travado":
        case "olhar fixo":
            case "olhar pesado":
            if (tardeNoite) {
                return {
                    diagnostico: `Sensor de Sono ativado, agora já são ${h}h.`,
                    explicacao: "O hardware está tentando desligar tudo possivel para economizar a bateria que resta .",
                    instrucao: "Não force o processamento. Inicie o protocolo de descanso imediatamente.",
                    frase: "O olhar travou porque o sistema quer 'Desligar'. Respeite o hardware. Descanse."
                };
            }
            return {
                diagnostico: "Dissociação ou Shutdown iminente.",
                explicacao: "O sistema está tentando desligar para se proteger. Reduza IMEDIATAMENTE as luzes e sons.",
                instrucao: "Não tente processar informações agora. Tudo está corrompido. Espere o sistema normalizar a segurança dos processamentos.",
                frase: "Seu sistema está se protegendo de um pico de energia. Aguarde o reset."
            };

            case "tristesa profunda":
                case "vontade de chorar":
            return {
                diagnostico: "Tristeza Profunda / Sobrecarga de Pressão.",
                explicacao: "O reservatório emocional atingiu o limite crítico de carga.",
                instrucao: "Permita o choro. Busque um ambiente seguro e reduza luzes.",
                frase: "As veses 'lavar' o sistema evita danos maiores no futuro. LIBERE A PRESSÃO!"
            };

        case "angustia leve":
            case "peso por algo que foi ou não dito":
            return {
                diagnostico: "Angústia Leve ",
                explicacao: "Existe um dado não processado sobre uma interação social ou algum acontecimento.",
                instrucao: "Tente escrever o que ficou pendente ou apenas observe os pensamentos que aparecerem sobre o assunto.",
                frase: "Pequenos tópicos também precisam de processamento."
            };

        case "desespero":
            case "panico":
            return {
                diagnostico: "Desespero ou Pânico.",
                explicacao: "O sistema detectou uma ameaça crítica e ativou o modo de fuga total.",
                instrucao: "FOCO NO HARDWARE: Toque em algo gelado. Respire contando até 4. Volte pro presente. SE ACALME!",
                frase: "Isso é uma descarga química, está acontecendo dentro da sua cabeça, isso não é um fato real. VOCÊ ESTÁ SEGURO!"
            };

        case "ansiedade":
        case "sobrecarga":
            return {
                diagnostico: "Ansiedade / Muitas abas abertas.",
                explicacao: "Excesso de processamento tentando prever múltiplas variáveis ao mesmo tempo.",
                instrucao: "Feche as tarefas secundárias. Foque apenas no que é vital para o sistema funcionar agora.",
                frase: "Reduza preocupações. Aumente o foco. O presente está aqui."
            };


        case "agitação sensorial":
        case "estresse":
            return {
                diagnostico: "Agitação Sensorial.",
                explicacao: "O ambiente está enviando dados demais e o sistema está superaquecendo.",
                instrucao: "Use fones de ouvido ou mude para um ambiente com menos estímulos.",
                frase: "Se o excesso de sons nos questiona o funcionamento. Silenciar pode ser a melhor resposta."
            };

        case "empolgação":
        case "alegria":
            return {
                diagnostico: "Dopamina Alta / Empolgação.",
                explicacao: "Pico de energia positiva no sistema, ela esta buscando formas de saída.",
                instrucao: "Aproveite o momento e deixe o corpo se expressar livremente.",
                frase: "O sistema está celebrando! ISSO É BOM!"
            };

        case "dissociação" :
            case "shutdown iminente":
            return {
                diagnostico: "Shutdown.",
                explicacao: "Proteção de hardware: o sistema se desligou do mundo para evitar  maiores danos.",
                instrucao: "Não force o retorno. Fique em silêncio e escuro absoluto, aguarde o reset automatico do sistema.",
                frase: "Protocolos de segurança estão em execução. Respeite o tempo do seu sistema."
            };

        case "devaneio":
            case "processamento em segundo plano":
            return {
                diagnostico: "Devaneio / Organização de Cache.",
                explicacao: "O sistema está desfragmentando o disco interno e organizando pastas.",
                instrucao: "Deixe fluir, é uma manutenção necessária para organizar pensamento e estimular a criatividade.",
                frase: "Sistema organizando arquivos internos... Aguarde... Resultados incríveis virão em breve..."
            };

        case "sobrecarga sensorial":
            case "crise de ansiedade":
            return {
                diagnostico: "Sobrecarga Sensorial Crítica.",
                explicacao: "Entrada de dados está corrompida por excesso de luz, som ou toques.",
                instrucao: "Vá para um local escuro e silencioso imediatamente. Remova estímulos.",
                frase: "Fonte de entrada de dados corrompida. Aguarde o auto-reparo."
            };

        case "inquietude":
            case "nervosismo":
                case "impaciência":
            return {
                diagnostico: "Inquietude / Nervosismo.",
                explicacao: "Ruído no sistema causado por tedio ou processamento lento do ambiente.",
                instrucao: "Mude de atividade, busque fazer algo manualmente ou faça uma caminhada curta.",
                frase: "Ajuste a atividade ao alto nivel de energia que está no sistema no momento."
            };

        case "irritabilidade":
            case "pré-meltdown":
            return {
                diagnostico: "Alerta de Meltdown.",
                explicacao: "O Scanner emocional está corrompido. Risco alto de colapso do sistema.",
                instrucao: "AVISO: Entre em modo de isolamento total. Evite contato agora.",
                frase: "Bugs de processamento críticos foram detectados. MODO DE DEFESA ATIVADO!"
            };

        case "foco em ruídos":
            return {
                diagnostico: "Falha no Filtro Acústico.",
                explicacao: "O hardware está corrompido e dando prioridade máxima para sons irrelevantes.",
                instrucao: "Use fones com cancelamento de ruído ou música de conforto. Logo essa falha será resolvida.",
                frase: "Filtro de ruídos desnecessários do ambiente está quebrado. Espere o conserto em silencio ou com 'conforto'."
            };

        case "tédio ou desatenção":
            return {
                diagnostico: "Sistema Ocioso.",
                explicacao: "Falta de estrada de dados estimulante. O seu processador está 'buscando atividade'.",
                instrucao: "Busque uma atividade interessante ou uma nova tarefa que seja desafiadora.",
                frase: "Alto processamento não foi feito pra ficar ocioso. Utilise a capacidade do sistema."
            };

        case "medo":
        case "ansiedade social":
            return {
                diagnostico: "Bug Social.",
                explicacao: "Sensor de ameaças está focado na interpretação de outros usuários (pessoas).",
                instrucao: "Lembre-se: as informações estão sendo processadas de forma corrompida neste momento. Está tudo bem! Você está seguro.",
                frase: "O ruído é apenas o medo. As interações são a melodia."
            };


        case "esgotamento verbal (não verbal)":
            return {
                diagnostico: "Modo Não Verbal.",
                explicacao: "A bateria zerou. O módulo de fala foi desligado para poupar energia.",
                instrucao: "Não force a fala. Use escrita, gestos ou simplesmente use o silêncio.",
                frase: "Módulo de fala offline. Aguarde a auto-recarga da bateria."
            };

        case "cansaço mental":
            return {
                diagnostico: "Colapso da CPU",
                explicacao: "Sobrecarga no sistema, causado pelo alto funcionamento durante um periodo muito longo e sem pausas.",
                instrucao: "Restrinja o processamento ao essencial. Descanse a mente.",
                frase: "Sistema corrompido. Aguarde o reset para voltar ao funcionamnto normal."
            };

        case "crise ansiosa": 
        case "loop de tag":
            return {
                diagnostico: "Loop de TAG (Ansiedade Geral).",
                explicacao: "O sistema travou em uma sequência de 'E se?' que não tem fim.",
                instrucao: "Force um reset com estímulo físico (ex: banho gelado ou exercício). Volte pro presente.",
                frase: "Quebre o loop, saia do bug, resete o processamento."
            };

        case "ansiedade antecipatória":
            return {
                diagnostico: "Simulação de Futuro Inexistente.",
                explicacao: "Sistema tentando processar um código que ainda nem foi compilado.",
                instrucao: "Volte para o momento presente. O futuro é um arquivo bloqueado.",
                frase: "Pare de corrigir bugs em um código que ainda não existe!"
            };

// ===========================================================================================================================================================================
        //  SETOR DE HARDWARE (CORPO) 

        case "fome":
            if (horaRefeicao) {
                return {
                    diagnostico: `Nível de combustível crítico. Agora são ${h}h, hora de se alimentar.`,
                    explicacao: " O sistema consumiu suas energias e agora atingiu o horário previsto para o reabastecimento.",
                    instrucao: "Pausa obrigatória para nutrição. Priorize a ingestão de proteínas e carboidratos.",
                    frase: "Sem combustível, não nos movemos na estrada. \n ABASTEÇA-SE!"
                };
            }
            return {
                diagnostico: `Fome fora de hora detectada, agora são ${h}h, era pra voce já ter se alimentado e estar saciado.`,
                explicacao: "Fome fora de hora pode ser sinal de que não houve alimentação adequada. Busque ingerir algo saudavel.",
                instrucao: "Nutra-se corretamente! Certifique-se que esta disponibilizando para o seu sistema todos os insumos necessarios.",
                frase: "Alimentação é sobre nutrição, não mastigação. \n NUTRA-SE!"
            };

        case "sede":
            return {
                diagnostico: "Nível de hidratção crítico.",
                explicacao: "Falha nos sensores de hidratação, o alerta só veio com o sistema quase colapsando.",
                instrucao: "Pausa obrigatória para hidratação. Priorize a ingestão de água nas próximas horas.",
                frase: "Sem hidratação, o motor superaquece.\n HIDRATE-SE!"
            };

        case "cansaço":
            if (h >= 18 || madrugada) {
                return {
                    diagnostico: `Esgotamento de Fim de Dia, já são ${h}h, hora de encerrar por hoje.`,
                    explicacao: "O excesso de processamento de estímulos durante o dia sobrecarregou os capacitores mentais. Hora do reset.",
                    instrucao: "Inicie o modo 'noturno': pare as atividades estimulantes, inicie atividades mais relaxantes, vá para o escuro e fique em silêncio. Isso permitirá o inicio do real descanço.",
                    frase: "Descanso é cuidado, não punição. \n CUIDE-SE! DESCANSE!"
                };
            }
            return {
                diagnostico: `Cansaço Diurno detectado (são ${h}h) .`,
                explicacao: "Superaquecimento por excesso de estímulos. O sistema 'fritou' antes do horário e precisa dormir.",
                instrucao: "Faça um reset (soneca curta) ou fique 15 min no escuro total. Cansaço se resolve com descanso.",
                frase: "Resfrie o sistema para não queimar os circuitos antes do fim do dia! Descanso tambem é progresso! "
            };

        case "desconforto ambiental":
            return {
                diagnostico: "Erro de Hardware Externo.",
                explicacao: "Luz, temperatura ou texturas estão sobrecarregando o sistema.",
                instrucao: "Ajuste o ambiente: troque de roupa ou ajuste a iluminação. Busque conforto",
                frase: "Às vezes o erro está no cenário. Não no ator. Refaça a cena."
            };

        
        case "necessidade de autorregulação (stimming)":
            return {
                diagnostico: "Necessidade de Autorregulação.",
                explicacao: "O corpo precisa de movimentos repetitivos para organizar o funcionamento do sistema nervoso.",
                instrucao: "Não reprima os movimentos. Use seus 'fidget toys'.",
                frase: "Stimming é manutenção do sistema, não bug!"
            };


        // O 'default' é o que acontece quando o sintoma não está na lista
        // estou trabalhando continuamente para adicionar sintomas a lista
        // o intuito é que o default quase não seja acionado 
    
        default:
            return {
                diagnostico: "Sinal não identificado no banco de dados.",
                explicacao: `Um novo sentimento está sento detectado agora (${h}h),  mas ele ainda precisa de investigação.`,
                instrucao: "Observe e anote os sintomas físicos e mentais para criar um novo 'case'.",
                frase: "Continue aprendendo sobre seu sistema, um commit de cada vez. \n VAMOS IDENTIFICAR ESSE BUG!"
            };
    }
};

//=================================================================================================================================================

//  AQUI O USUÁRIO DEVE PREENCHER

// EXEMPLO: investigarBugHumano ("sentimento" , intensidade , horário é opcional)
// se não colocar o horario, o código vai puxar sozinho o horário atual no sistema) )

const meuStatusAgora = investigarBugHumano ("Medo" , 7,);


//=================================================================================================================================================


// AQUI O USUÁRIO NÃO DEVE MEXER
// Aqui damos o comando que imprime o resultado na tela do computador


console.log ( `

    === RELATÓRIO TÉCNICO DE SISTEMA ===
  
O QUE ESTÁ ACONTECENDO: ${meuStatusAgora.diagnostico}

POR QUE ISSO ACONTECE: ${meuStatusAgora.explicacao}

O QUE FAZER: ${meuStatusAgora.instrucao}

MENSAGEM:  ${meuStatusAgora.frase}


Diagnóstico realizado em: ${dataEHora}

` )