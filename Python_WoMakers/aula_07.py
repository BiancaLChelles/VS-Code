# Aula 07 - Exercício 01


#nesta aula, vamos calcular a diferença entre o valor normal por minuto e o valor promocional de um serviço.

preco = input('Valor normal por minuto: ')
preco_promocional = float(input('Valor promocional: '))

# Para calcular a diferença, basta subtrair o valor promocional do valor normal.

print("Diferença de valor:", round( float(preco) - preco_promocional, 2) )