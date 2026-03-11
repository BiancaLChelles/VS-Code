


#Tratamento de Erros

""" 
try:
    numero = int(input("Digite um numero: "))

    resultado = 10/ numero



except ZeroDivisionError:
    print("Não é possivel dividir por zero!")

except  ValueError:
    print("Digite somente números!")


else:
     print(f"Resulstado:{resultado}")     """


try:
    aqruivo = open("dados.txt", mode= "r")
    conteudo = arquivo.read()

except FileNotFoundError:
    print("arquivo não encontrado")    


finally:
    print("Operação finalizada!")    