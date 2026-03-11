# Dicionario de Dados em Python
# Dicionário é uma coleção de dados que armazena pares de chave-valor. Ele é mutável, o que significa que você pode alterar seus valores após a criação. Os dicionários são úteis para armazenar dados relacionados e acessar informações de forma eficiente.


#aqui temos um dicionário chamado "aluna" com as seguintes chaves: "nome", "idade", "curso" e "status". Cada chave tem um valor associado a ela. Podemos acessar os valores usando as chaves correspondentes, como mostrado no exemplo acima, onde acessamos o valor da chave "nome" e o imprimimos.
aluna = {
    "nome": "Ana",
    "idade": 45,
    "curso": "Python",
    "status": True
}

print(aluna["nome"])

#aqui, estamos atualizando o valor da chave "idade" para 54 e adicionando uma nova chave "cidade" com o valor "São Paulo". Depois disso, imprimimos o dicionário atualizado para mostrar as mudanças feitas.
aluna["idade"] = 54

aluna["cidade"] = "São Paulo"

print(aluna)


#aqui, estamos removendo a chave "idade" do dicionário usando o método pop(). O método pop() remove a chave especificada e retorna o valor associado a ela. Depois de remover a chave "idade", imprimimos o dicionário atualizado para mostrar que a chave foi removida.

aluna.pop("idade")

print(aluna)

