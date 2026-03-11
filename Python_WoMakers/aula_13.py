# Repetindo tarefas com for

#tecnologias = ['Python', 'Dados', 'IA',]
 # aqui o for percorre a lista e imprime cada item
 #range significa intervalo, ou seja, o for vai percorrer o intervalo de 0 até o tamanho da lista
 #len significa comprimento, ou seja, o tamanho da lista
#for item in range(len(tecnologias)):
    #print(tecnologias[item])
   


#perfil = {"nome": "Ana", "estado" : "RS"}

#for chave in perfil:
 #print (chave, perfil[chave])



# aqui o for percorre o intervalo de 0 até 4, ou seja, 5 vezes
#for indice in range (5):
    # aqui o for imprime o valor do indice, ou seja, o número da repetição
 #   print("Repetindo" ,  indice)
  #  print ("Oi Wo Makers")

indice = 0

for item in range(5):
    indice += item
    print("Número atual", indice)
