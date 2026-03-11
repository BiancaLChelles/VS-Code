#SISTEMA DE CADASTRO



#FASE 1 - Coleta e Armazenamento de Dados


#Solicitar ao usuário que insira seu nome
nome = input("Digite seu nome: ")

#Solicitar ao usuário que insira sua idade
#usei o int para converter a entrada do usuário em um número inteiro, pois a idade é um valor numérico
idade = int(input("Digite sua idade: "))

#Solicitar ao usuário que insira sua altura
#usei o float para converter a entrada do usuário em um número decimal, pois a altura pode conter casas decimais
altura = float(input("Digite sua altura: "))

#Solicitar ao usuário que insira o ano atual
#usei o int para converter a entrada do usuário em um número inteiro, pois o ano é um valor numérico
anoAtual = int(input("Digite o ano atual: "))



#FASE 2 - Interação personalizada


#Exibir uma mensagem personalizada usando o nome do usuário
print( "Olá," , nome , '! Seja bem vinda ao mundo do Python!')



#FASE 3 - Processamento e Cálculos


#Calcular o ano de nascimento do usuário
ano_nascimento = anoAtual - idade

#Calcular a idade do usuário em 5 anos
idade_futuro = idade + 5

#Calcular o dobro da idade do usuário
dobro_idade = idade * 2

#Calcular a idade do usuário elevada ao quadrado
idade_elevada = idade ** 2



#FASE 4 - Lógica e Comparação


#Verificar se o usuário é maior de idade
maior_idade = idade > 18

#Verificar se a altura do usuário é maior ou igual a 1.60
altura_minima = altura >= 1.60


#Exibir os resultados das comparações em formato booleano (True ou False)
print("Maior de idade?", maior_idade)
print("Altura maior ou igual a 1.60?", altura_minima)


#FASE 5 - Documentação (Cometários)

# Este código é um sistema de cadastro que coleta informações do usuário, realiza cálculos e exibe resultados personalizados.
# utilizando variáveis para armazenar os dados, operadores para realizar cálculos e comparações
# Possui também comentários para explicar cada etapa do processo.