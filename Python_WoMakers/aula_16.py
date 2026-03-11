# Tuplas em python
# As tuplas são imutáveis, ou seja, não podem ser alteradas depois de criadas
# Elas são definidas usando parênteses () ou sem parênteses, separando os elementos por vírgulas

dias_da_semana = ("Segunda", "Terça", "Quarta", "Quinta", "Sexta")

print(dias_da_semana(0))  # Acessando o primeiro elemento da tupla
print(dias_da_semana[1])  # Acessando o segundo elemento da tupla
print(dias_da_semana[2])  # Acessando o terceiro elemento da tupla
print(dias_da_semana[3])  # Acessando o quarto elemento da tupla
print(dias_da_semana[4])  # Acessando o quinto elemento da tupla                            

# Tuplas são imutáveis, então não podemos alterar seus elementos
# dias_da_semana[0] = "Domingo"  # Isso causará um  erro, pois as tuplas não podem ser modificadas



cordenadas = (10, 20)
print(cordenadas[0])  # Acessando a coordenada x
print(cordenadas[1])  # Acessando a coordenada y