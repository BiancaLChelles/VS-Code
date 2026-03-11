#EXERCICIOS

#Exercício 1

aulas_concluidas = int(input("Digite o número de aulas concluídas: "))
if aulas_concluidas >= 5:
    print("Bom progresso!")
else:
    print("Continue se estudando")


# Exercício 2

n = 0

while n < 10:
    n += 1
    print(n)

# Exercício 3

for n in range(1, 6):
    print(f"Aula {n} concluída")


# Exercício 4
dias_da_semana_estudados = ["Segunda", "Quarta", "Sexta"]
for dia in dias_da_semana_estudados:
    print(f"Hoje é {dia}, um dia de estudo!")


# Exercício 5

idade = int(input("Digite sua idade: "))

if idade >= 16:
    print(f"Você tem {idade}, você pode se increver no curso. Parabéns!")
else:   
    print(f"Você tem {idade}, infelizmente você não pode se increver no curso. Tente novamente quando tiver 16 anos ou mais.")