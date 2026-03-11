#Operadores relacionais

# Exempos de operadores
# Maior que >
# Menor que <
# Maior ou igual a >=
# Menor ou igual a <=
# Igual a ==
# Diferente de !=


valorA = int(input("Digite o valor A: "))
valorB = int(input("Digite o valor B: "))


print (valorA > valorB) # Maior que
print (valorA < valorB) # Menor que
print (valorA >= valorB) # Maior ou igual a
print (valorA <= valorB) # Menor ou igual a
print (valorA == valorB) # Igual a
print (valorA != valorB) # Diferente de 


# Precedência de operadores

# A ordem de precedência dos operadores é a seguinte:
# 1. Parênteses ()
# 2. Exponenciação (**)
# 3. Multiplicação (*) e Divisão (/)
# 4. Adição (+) e Subtração (-)


resultado = valorA + valorB *2
resultado_correto = (valorA + valorB) * 2
print(resultado)
print(resultado_correto)


verificacao = valorA + valorB >2
print(verificacao)
