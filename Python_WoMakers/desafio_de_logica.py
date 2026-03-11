

nome = input("Digite seu nome: ")
opçao1 = "inscrição"
opcao2= "desafio"
opcao3 = "resultado"
rodadas = 0
quer_encerrar = False

print(f"Olá, {nome}! Bem-vindo ao desafio de lógica.")
print("Começaremos a apresentar o menu.")

while not quer_encerrar:

    if rodadas >= 3:
        print("Número máximo de rodadas atingido. Encerrando o programa.")     
        quer_encerrar = True
        continue

    print("\nMenu:")
    print(f"Olá {nome}, escolha uma das opções abaixo:")
    print(f"1. {opçao1}")
    print(f"2. {opcao2}")
    print(f"3. {opcao3}")
    print("4. Encerrar")
    print(f"Este menu ira aparecer novamente {3-rodadas} vezes.")



    escolha = input("\nEscolha uma opção de 1-4: ")
    rodadas += 1
    
    if escolha == '1':
        print("Você escolheu a Opção 1.")   
        print(f"{nome}, você escolheu a opção {opçao1}.")
        print("esta opção é para se inscrever no desafio.")

    elif escolha == '2':
        print("Você escolheu a Opção 2.")
        print(f"{nome}, você escolheu a opção {opcao2}.")
        print("esta opção é para participar do desafio.")

    elif escolha == '3':
        print("Você escolheu a Opção 3.")
        print(f"{nome}, você escolheu a opção {opcao3}.")
        print("esta opção é para ver o resultado do desafio.")

    elif escolha == '4':
        print("Você escolheu a Opção 4.")
        print(f"{nome}, você escolheu a opção Encerrar.")
        print("Encerrando o programa. Até mais!")
        quer_encerrar = True

    else:
        print("Erro: Opção inválida. Por favor, escolha uma opção entre 1 e 4.")

