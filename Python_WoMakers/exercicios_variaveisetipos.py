#Exercicio 1
nome = input("Digite seu nome: ")
interesse = input("Digite sua área de interesse: ")
tempo = int(input("Quanto tempo que você tem disponível para estudar (em horas)? "))

print("ola", nome, "você tem interesse em", interesse, "e tem", tempo, "horas disponíveis para estudar.")

#Exercicio 2

aulas_assistidas = int(input("Quantas aulas você assistiu? "))
aulas_totais = int(input("Quantas aulas tem o curso? "))

aulas_restantes = aulas_totais - aulas_assistidas

print("Você ainda tem", aulas_restantes, "aulas para assistir.")

#Exercicio 3

estudo_diario = float(input("Quantas horas você estuda por dia? "))

print("Você estuda", estudo_diario, "horas por dia.")

#Exercicio 4

estudos_semanais = int(input("Quantas horas você estuda por semana? "))
if estudos_semanais % 2 == 0:
    print("Você estuda um número par de horas por semana.")
else:
    print("Você estuda um número ímpar de horas por semana.")


#Exercicio 5

semanas_estudadas = int(input("Quantas semanas você já estudou? "))

semanas_estudadas += 1
print("Quando essa semana encerrar, você terá", semanas_estudadas, "semanas de estudo.")