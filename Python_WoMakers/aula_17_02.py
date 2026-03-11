#Dicionario  e listas de Dados em python


escola = [
 {"nome": "Ana",
    "idade": 45,
    "curso": "Python",
    "status": True
 },
 {"nome": "Cynthia",
    "idade":34,
    "curso": "C#",
    "status": True
 },
 {"nome": "Clarice",
    "idade": 23,
    "curso": "Dados",
    "status": False
 }
]

nome_de_escola = "WoMakesCode"

 #aqui temos uma lista de dicionarios, onde cada dicionario tem as chaves nome, idade, curso e status.

 #estamos imprimindo a lista de dicionarios, onde cada dicionario representa uma aluna da escola
 # .print(escola)

#dessa forma a impressão fica mais organizada, onde cada aluna é impressa em uma linha diferente.

for aluna in escola:
    print(f"Intituição de ensino: {nome_de_escola}")
    print(f"Nome: {aluna["nome"]}")
    print(f"Curso: {aluna["curso"]}")
    #aqui estamos imprimindo o nome da instituição de ensino, o nome da aluna e o curso que ela está cursando.

    #aqui estamos verificando o status da aluna, se ela está ativa ou inativa, e imprimindo a mensagem correspondente.
    if aluna["status"]:
        print("Matricula: Ativa")
    else:
        print("Matricula: Inativa")
    print("-" * 20)
    #aqui criamos uma divisão entre cada aluna, para deixar a impressão mais organizada.




