dados_curso = ("Intensivo Python" , 3 , 60)

opcao4 = False

menu = '''
        MENU

        Escolha a opção desejada:
        1 - Cadastrar participante
        2 - Mostrar participantes
        3 - Mostrar análises
        4 - Sair

        '''

novo_cadastro = ('''
                    Por favor insira seus dados:
''')

cadastros = [
    { "NOME": "Paula",
      "IDADE": 19,
      "HORAS DE ESTUDO": 7,
      "ÁREA DE INTERESSE": "Python"}
]

while not opcao4:

    # O input do menu precisa ser convertido para int para os IFs funcionarem
    escolha = int(input(menu))

    if escolha == 1:
        print("Faça um novo cadastro:")
        # Para o sistema de análise (opção 3) funcionar, 
        # precisamos preencher os campos do dicionário:
        nome = input("NOME: ")
        idade = int(input("IDADE: "))
    
      # 1ª Trava: Verificação de Idade
        if idade < 18:
            print(f" Erro: {nome} você tem {idade} anos. Apenas maiores de idade podem se cadastrar.")
        else:
            horas = int(input("HORAS DE ESTUDO: "))
            
            # 2ª Trava: Verificação de Horas Negativas
            if horas < 0:
                print(" Erro: As horas de estudo não podem ser negativas!")
            else:
                area = input("ÁREA DE INTERESSE: ")
                
                # Só adiciona se passar em todas as verificações acima
                cadastros.append({
                    "NOME": nome, 
                    "IDADE": idade, 
                    "HORAS DE ESTUDO": horas, 
                    "ÁREA DE INTERESSE": area
                })
                print(" Cadastro realizado com sucesso!")

    elif escolha == 2:
        print("Aqui está o cadastro de todas as participantes:")
        print( "=" * 30)
        for pessoa in cadastros:
            print(f"Nome: {pessoa['NOME']} | Idade: {pessoa['IDADE']} | Horas: {pessoa['HORAS DE ESTUDO']} area: {pessoa['ÁREA DE INTERESSE']}")
        
            print("="*30)

    elif escolha == 3:
        print("\n--- Relatório de Análises ---")
        
        if len(cadastros) > 0:
          
            lista_horas = [pessoa["HORAS DE ESTUDO"] for pessoa in cadastros]
            total_horas = sum(lista_horas)
            quantidade = len(cadastros)
            media_horas = total_horas / quantidade
            
            #  análise: Lista de Áreas de Interesse (sem repetição)
            # Usamos set() para não mostrar "Python" várias vezes
            areas_unicas = set([pessoa["ÁREA DE INTERESSE"] for pessoa in cadastros])
            
            # 3. Alunas destaque
            acima_media = [pessoa["NOME"] for pessoa in cadastros if pessoa["HORAS DE ESTUDO"] > media_horas]

            print(f"TOTAL DE ALUNAS: {quantidade}")
            print(f"MÉDIA DE HORAS: {media_horas:.2f}")
            print(f"ÁREAS PRESENTES NO CURSO: {', '.join(areas_unicas)}")
            print(f"ALUNAS DESTAQUE: {acima_media}")
            
        else:
            print("Nenhum dado para analisar.")

    elif escolha == 4:
        print("MENU ENCERRANDO")
        opcao4 = True
    
    else:
        print("Opção inválida.")