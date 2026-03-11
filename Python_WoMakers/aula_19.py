#Manipulação de arquivos

import os




arquivo = "alunas.txt"
alunas =[]

#with open(arquivo, mode= "w", encoding= "utf-8") as lista:
  #  lista.write("Ana\n")
   # lista.write("Beatriz\n")
    #lista.write("Gisele\n")




#with open(arquivo , mode = "r" , encoding="utf-8") as lista:
    #conteudo = lista.read()    



#with open(arquivo , mode = "r" , encoding="utf-8") as lista:
 #   for linha in lista: 
  #      print(linha.strip())   


#with open(arquivo , mode = "r" , encoding="utf-8") as lista:
 #  alunas = lista.readlines()

#alunas_atualizadas= []

#for aluna in alunas :
 #  nome = aluna.strip()
  # if nome != "Gisele":
   #   alunas_atualizadas.append(nome)



#with open (arquivo, mode= "w", encoding = "utf-8") as lista :
 #   for aluna in alunas_atualizadas:
  #      lista.write(aluna + "\n" )

        
#with open (arquivo, mode= "a", encoding = "utf-8") as lista :
 #  lista.write("Daniela\n")



 

if os.path.exists(arquivo):
    os.remove(arquivo)
    print ("Arquivo removido!")

else :
    print("Arquivo não encontrado!")




