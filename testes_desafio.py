def analise (lideres, mulheres):

    porcentagem = (mulheres / lideres) * 100


    if porcentagem < 30:
        print("A empres está abaixo da meta de diversidade.")
    elif  30 <= porcentagem >= 50:
        print("A empresa está na meta de diversidade.")
    elif 50 <porcentagem >= 100:
        print("A empresa excedeu a meta de diversidade.")
    else:
        print ("Status da meta de diversidade não encontrado, reintroduza os dados.")             


analise(4,6)
