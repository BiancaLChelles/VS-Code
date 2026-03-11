// Este código foi construído como um "Exoesqueleto Mental". 
// serve para traduzir sensações físicas e mentais que o próprio corpo às vezes não consegue nomear sozinho (Alexitimia).
 
//==============================================================================================================================

//  AQUI O USUÁRIO NÃO DEVE MEXER
// Esta é a função principal. O nome 'investigarBugHumano' indica que estamos abrindo uma sessão de diagnóstico técnico sobre o nosso próprio estado.
const investigarBugHumano = (sintomaDetectado , horarioAtual) => {

    // O 'switch' funciona como uma central de triagem. 
    // ele vai receber o que você está sentindo e procurar na lista qual é o protocolo de resolução cíadequado para aquele caso espefico.
  
    switch (sintomaDetectado) {

//=========================================================================================================================================================
        
        //  SETOR DE SOFTWARE ( MENTE ) 

        case "medo paralisante":
            // O 'return' é a resposta final que o sistema cospe para fora da gaveta.
            return {
                diagnostico: "O sistema travou por excesso de ameaças detectadas.",
                explicacao: "O hardware identificou um risco real ou não e cortou a energia dos movimentos para ampliar a proteção.",
                instrucao: "Não force ação. Reduza luz, som e estimulos. Espere o sistema  processar, equalizar e sinalizar segurança.",
                frase: "Paralisar, as vezes é defesa, não falha. \n DESCANSE!"
            };

        case "hiperfoco":
      // vamos afunilar ainda mais os auxilioas refentes ao hiperfoco
      //criando possibilidades de analise de horario, tempo de foco, etc

      if ( horarioAtual >= 21 ) {
       return { diagnostico: "Hiperfoco noturno detectado, cuidado, 'essa produção' pode custar caro amanhã.",
               explicacao: "Neste momento, você esta em foco, porem precisa descansar, comece o processo de transição.",
               instrucao: "Diminua a carga da atividade atual, inicie o planejamento mental de atividades substitutivas e mais relaxantes, se permita descansar",
               frase: "O hiperfoco é tipo um superpoder, mas você não é o batman, vai descansar gotham está segura! \n VOCÊ NÂO È UM MORCEGO!"
              };
      } else {
            return {
                diagnostico: "Processador operando em 100% de capacidade, voltado a somente uma única tarefa.",
                explicacao: "A atenção está em modo túnel, ignorando alertas de manutenção do corpo.",
                instrucao: "Agendar alarmes regulares para checagem de sede, fome, cansço e postura. Planejar o 'manejo' da atividade.",
                frase: "O hiperfoco pode ser quase um superpoder, mas, como dizem em homem-aranha, grandes poderes vem com grandes responsabilidades. \n SE ORGANIZE! SE CUIDE!"
            };
      }
        case "ruminacao":
            return {
                diagnostico: "Loop infinito de processamento de dados passados e/ou futuros.",
                explicacao: "A mente tenta reprocessar um erro antigo, ou tenta prever e 'arrumar' um erro futuro, buscando alterar uma variável que não pode ser mudada.",
                instrucao: "Mudar o ambiente sensorial, buscar novas perspectivas, reconectar -se com o ambiente a sua volta retornando ao momento presente.",
                frase: "Ficar rodando código com erro não conserta arquivo corrompido. \n VOLTE Á REALIDADE, RETORNE AO MOMENTO PRESENTE! "
            };

        //  SETOR DE HARDWARE (CORPO) 

        case "fome":
            return {
                diagnostico: "Nível de combustível crítico.",
                explicacao: "Falha no sensor de interocepção; o alerta só veio com o sistema quase desligando.",
                instrucao: "Pausa obrigatória para nutrição. Priorise a ingestão de proteínas e carboidratos.",
                frase: "Sem combustível, não nos movemos na estrada. \n ABASTEÇA-SE!"
            };

           case "sede":
            return {
                diagnostico: "Nível de hidratção crítico.",
                explicacao: "Falha no sensor de interocepção; o alerta só veio com o sistema quase colapsando.",
                instrucao: "Pausa obrigatória para hidratação. Priorise a ingestão de água nas próximas horas.",
                frase: "Sem hidratação, o motor superaquece.\n HIDRATE-SE!"
            };

        case "cansaco":
            return {
                diagnostico: "Superaquecimento e esgotamento de mental.",
                explicacao: "O excesso de processamento de estímulos durante um longo periodo pode ter fritado os capacitores mentais.",
                instrucao: "Ativar modo de hibernação: fique no escuro, em silêncio, faça coisas conforatveis e relaxantes. Isso irá te acalmar e permitir o real descanço",
                frase: "Descanso é cuidado, não punição. \n CUIDE-SE! DESCANSE!"
            };

        case "falta de sol":
            return {
                diagnostico: "Dessincronização do Ciclo Circadiano.",
                explicacao: "A falta de luz natural impede a calibração de hormônios essenciais como os de alerta e sono.",
                instrucao: "Vá para para aréa externa imediatamente. Você precisa de sol. Sincronize sua melatonina.",
                frase: "A luz do sol é um principal fator, capaz de controlar todo o ciclo da vida que conhecemos. \n VOCÊ PRECISA DESSA LUZ TAMBEM!"
            };

        // O 'default' é o que acontece quando o sintoma não está na lista.
        // Atualizo a lista de case's continuamente, apartir de experiencias prévias.
        // Estou trabalhando para que o defaut quase não seja acionado
        // Afinal, o intuito é criar um código que de respostas e ajude, não um código que tambem não sabe.
        
        default:
            return {
                diagnostico: "Sinal não identificado no banco de dados.",
                explicacao: "Um novo comportamento ou acontecimento que ainda precisa de investigação e análises detalhadas.",
                instrucao: "Observar e anotar os sintomas físicos e mentais para criar um novo 'case'.",
                frase: "Continue aprendendo sobre seu sistema, um commit de cada vez. \n VAMOS IDENTIFICAR E RESOLVER ESSE BUG!"
            };
    }
};



//=================================================================================================================================================
//  AQUI O USUÁRIO DEVE PREENCHER
// Dentro dos parênteses abaixo, escreva o que você está sentindo entre as aspas.
// Exemplo: "fome", "cansaco", "hiperfoco", "ruminacao", etc.



const meuStatusAgora = investigarBugHumano("hiperfoco" , 14 );



//===================================================================================================================================================






// [AQUI O USUÁRIO NÃO DEVE MEXER]
// Comando que imprime o resultado na tela do computador.


console.log ( `
    === RELATÓRIO TÉCNICO DE SISTEMA ===
  
O QUE ESTÁ ACONTECENDO: ${meuStatusAgora.diagnostico}

POR QUE ISSO ACONTECE: ${meuStatusAgora.explicacao}

O QUE FAZER: ${meuStatusAgora.instrucao}

MENSAGEM:  ${meuStatusAgora.frase}

    `

)