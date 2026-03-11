#Listas em pyhton
#lista é uma coleção de itens ordenada e mutável. Permite elementos duplicados.
#As listas são definidas usando colchetes [] e os elementos são separados por vírgulas.

cursos = ["Python", "Git", "Design", "CV"]

print(cursos)
print(cursos[0]) #Acessando o primeiro elemento da lista
print(cursos[1]) #Acessando o segundo elemento da lista
print(cursos[2]) #Acessando o terceiro elemento da lista
print(cursos[3]) #Acessando o quarto elemento da lista

#Modificando elementos da lista

# aqui estamos modificando o segundo elemento da lista, que é "Git", para "Git e GitHub"
cursos[1] = "Git e GitHub"

# aqui estamos modificando o quarto elemento da lista, que é "CV", para "Currículo"
cursos[3] = "Currículo"

#aqui estamos imprimindo a lista modificada, que agora contém "Git e GitHub" e "Currículo" em vez de "Git" e "CV"
print(cursos)

#aqui estamos adicionando um novo elemento "Dados" ao final da lista usando o método append()
cursos.append("Dados") #Adiciona um elemento ao final da lista

print(cursos)

#aqui estamos removendo o elemento "Design" da lista usando o método remove()
cursos.remove("Design") #Remove o elemento "Design" da lista

#aqui estamos removendo através do índice, ou seja, o elemento na posição 0 da lista, que é "Python", usando o método pop()
cursos.pop(0) #Remove o elemento na posição 0 da lista


#aqui estamos inserindo um novo elemento "Python" na posição 0 da lista usando o método insert()
cursos.insert(0, "Python") #Insere o elemento "Python" na posição 0 da lista

print(cursos)