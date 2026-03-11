


// Neste código busco desenvolver um "sensor"
//  que analise sensações fisicas e traduza em sentimentos
// o intuito é auxiliar individuos com alexitima 
// (A alexitimia é um condição neurodivergente onde o individuo possui dificuldade em compreender ou detectar as proprias emoções)
// o intuito é ajudar a compreender, identificar , gerir e reagir melhor as proprias emoções





function tradutorDeSentimentos(sinalFisico, intensidade) {
   

    switch (sinalFisico) {
        case "nó na garganta":
            case "vontade de chorar":
                case "choro preso":
            if (intensidade >= 7) {
                return {
                    emocao: "Tristeza Profunda ou Vontade de chorar",
                    instrucao: "O sistema precisa de liberação de pressão. Procure um lugar seguro para chorar."
                };
            } else {
                return {
                    emocao: "Angústia leve ou peso por algo que foi ou não dito",
                    instrucao: "Tente escrever o que aconteceu no dia de hoje, tente identificar algum possivel gatilho."
                };
            }

        case "peito apertado":
            case "aperto no peito":
                case "coração apertado":
             if (intensidade >= 7) {
                return {
                    emocao: "Desespero / Pãnico",
                    instrucao: "O sistema tem que voltar ao funcionamento básico urgentemente. Procure um lugar seguro. Converse com alguém."
                };
            } else {
            return {
                emocao: "Ansiedade ou Sobrecarga",
                instrucao: "Reduza os estímulos sensoriais. Busque silêncio e o escuro. \n Ative o modo de respiração profunda e retorne ao momento presente."
            };
        }

        case "mãos agitadas":
            case "flappin hands":
                case "mãos tremendo":
            if (intensidade >= 5) {
                return {
                    emocao: "Agitação Sensorial ou Estresse",
                    instrucao: "Use um objeto de regulação (fidget toy) ou faça alguma atividade que estimule suas mãos."
                };
            } else {
                return {
                    emocao: "Empolgação / Alegria (Stimming)",
                    instrucao: "O seu sistema está em um pico de energia positiva. Aproveite esse momento! ISSO É BOM!"
                };
            }

            case "olhar fixo":
                case  "olhar desligando":
                    case "olhar travado":
                        case "olhar morto":
                            case "olhar pesado":
                                case "olhar pesando":
            if (intensidade >= 6) {
                return {
                    emocao: "Dissociação ou Shutdown iminente",
                    instrucao: "CRITICO: O sistema está tentando desligar para se proteger. Reduza IMEDIATAMENTE as luzes e sons. Não tente processar informações agora."
                };
            } else {
                return {
                    emocao: "Devaneio ou Processamento em segundo plano",
                    instrucao: "Seu cérebro está organizando uma alta quantidade de dados. Deixe esse processamento fluir. Se possivel reduza os estimulos, busque voltar para o momemto presente."
                };
            }

            case "respiração rápida":
                case "respiração acelerada":
                    case "respiração forte":
            if (intensidade >= 7) {
                return {
                    emocao: "Sobrecarga Sensorial ou Crise de Ansiedade",
                    instrucao: "O sistema está em modo 'Luta ou Fuga'. Foque apenas em respirar lentamente (soltar o ar (e os pensamentos) é mais importante que puxar agora)."
                };
            } else {
                return {
                    emocao: "Inquietude, Nervosismo ou Impaciência",
                    instrucao: "Seu processamento está acelerado. Tente levantar, se alongar ou caminhar para gastar um pouco dessa energia acumulada."
                };
            }

        case "sensibilidade ao som":
            case "sons muito altos":
                case " sons incomodando":
            if (intensidade >= 6) {
                return {
                    emocao: "Irritabilidade ou Pré-Meltdown",
                    instrucao: "Sinal de que uma crise sensorial está proxima. Ative isolamento acústico (fones) ou mude para uma 'sala silenciosa' imediatamente."
                };
            } else {
                return {
                    emocao: "Foco em ruídos",
                    instrucao: "Seu sistema de filtragem de ruidos está baixo. Tente colocar um som ambiente, uma musica de conforto ou um ruído branco para mascarar um pouco dos sons externos."
                };
            }

        case "pernas agitadas":
            case "pernas tremendo":
            if (intensidade >= 5) {
                return {
                    emocao: "Necessidade de autorregulação (Stimming)",
                    instrucao: "Energia acumulada detectada. Deixe os movimentos acontecerem, a liberação de energia ajuda a manter o sistema estável."
                };
            } else {
                return {
                    emocao: "Tédio ou Desatenção",
                    instrucao: "O sistema precisa de novos estímulos. Troque de tarefa, busque um novo interesse, sua mente está precisando ser utilzada."
                };
            }

        case "mãos geladas":
            case "mãos frias":
            if (intensidade >= 6) {
                return {
                    emocao: "Medo ou Ansiedade Social",
                    instrucao: "O foco está no funcionamento vital agora. Aqueça as mãos com água morna, busque conforto, e diminua os estimulos. Vamos enviar um sinal de 'segurança' para o cérebro."
                };
            } else {
                return {
                    emocao: "Desconforto Ambiental",
                    instrucao: "Verifique a temperatura do local. Às vezes o bug é físico, não emocional. Você deve estar com frio. Vista um casaco."
                };
            }

        case "dificuldade em falar":
            case "dificuldade em formular frases":
                case "fala lenta":
                    case "fala travada":
                        case "dissociação":
            if (intensidade >= 6) {
                return {
                    emocao: "Esgotamento Verbal (NÃO VERBAL)",
                    instrucao: "O sistema de linguagem está offline para previvinir danos com a sobrecarga de energia. Use gestos, textos ou apenas descanse. Nem tudo tem que ser comunicado agora."
                };
            } else {
                return {
                    emocao: "Cansaço Mental",
                    instrucao: "Processamento de saída lento. Não se force a falar frases complexas agora. Respostas curtas também são aceitáveis."
                };
            }

            case "pensamento acelerado":
        case "mente com vários cenários ao mesmo tempo":
            case "mente acelerada":
                case "pensamentos caóticos":
                    case "pensamentos acelerados":
                        case "mente um caos":
            if (intensidade >= 8) {
                return {
                    emocao: "Crise Ansiosa ou Loop de TAG",
                    instrucao: "O processador está superaquecendo com simulações do futuro. Volte ao momento presente."
                };
            } else {
                return {
                    emocao: "Ansiedade Antecipatória",
                    instrucao: "Muitas abas estão abertas mentalmente. Tente minimizar o funcionamento para que o sistema possa se regular."
                };
            }

        case "pensamento em looping":
        case "ruminando o passado":
            case "ruminação":
                case "mente presa":
                    case "mente em looping":
            if (intensidade >= 7) {
                return {
                    emocao: "Ruminação (Bug de Autocrítica)",
                    instrucao: "O sistema travou em um erro do passado. Lembre-se: código executado, não pode ser editado. Reprograme, recomece."
                };
            } else {
                return {
                    emocao: "Análise de Padrões Sociais",
                    instrucao: "Você está tentando entender uma interação. Dê um tempo limite para isso, analise, processe e depois faça uma tarefa manual para sair deste foco."
                };
            }
        default:
            return {
                emocao: "uma Emoção não reconhecida",
                instrucao: "Beba água, busque silêncio e faça um scan corporal da cabeça aos pés. \n VAMOS ENTENDER ISSO! CALMA!"
            };
    }
}


// Testando o sensor ======================================================================================================================================================================



const meuSentimento = tradutorDeSentimentos("mãos frias", 7);

 console.log ( ` 
    === ANALISANDO SINAIS CORPORAIS ===
    
    EMOÇÃO: Neste momento você está sentindo ${meuSentimento.emocao}
    Lembre-se que esse sentimento também irá passar, assim como todos os outros.

    O QUE FAZER?: ${meuSentimento.instrucao}

    ` ) 