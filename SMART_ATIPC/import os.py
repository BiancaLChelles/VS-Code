import os

ARQUIVO_MEMORIA = "dicionario_sentimentos.json"

# Verifica o caminho completo de onde o Python está tentando ler/escrever
caminho_completo = os.path.abspath(ARQUIVO_MEMORIA)

if os.path.exists(ARQUIVO_MEMORIA):
    os.remove(ARQUIVO_MEMORIA)
    print(f"SUCESSO: O arquivo foi deletado em: {caminho_completo}")
else:
    print(f"ARQUIVO NÃO ENCONTRADO: O Python está procurando em: {caminho_completo}")
    print("Verifique se o nome do arquivo no seu código principal está EXATAMENTE igual.")