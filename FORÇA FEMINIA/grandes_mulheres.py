import sqlite3

def inicializar_banco():
    # Conecta ao arquivo de banco de dados (se não existir, o Python cria um novo)
    conexao = sqlite3.connect("memoria_mulheres.db")
    cursor = conexao.cursor() # O cursor é o "braço" que executa os comandos SQL
    
    # Criamos a tabela com colunas específicas para os dados que queremos rastrear
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS mulheres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            area TEXT,
            e_autista BOOLEAN,
            idade_feito_relevante INTEGER,
            descricao TEXT
        )
    ''')
    conexao.commit() # Salva as alterações no banco
    return conexao

def adicionar_mulher(conexao):
    print("\n--- Adicionar Nova Personalidade ---")
    nome = input("Nome: ")
    area = input("Área de atuação (ex: Ciência, Artes, Política): ").capitalize()
    # Transformamos o 's' ou 'n' em um valor Booleano (True/False)
    autista = input("É autista? (s/n): ").lower() == 's'
    idade = int(input("Com qual idade realizou seu principal feito? "))
    descricao = input("Breve descrição do feito: ")

    cursor = conexao.cursor()
    # Usamos '?' para evitar ataques de SQL Injection e manter o código seguro
    cursor.execute('''
        INSERT INTO mulheres (nome, area, e_autista, idade_feito_relevante, descricao)
        VALUES (?, ?, ?, ?, ?)
    ''', (nome, area, autista, idade, descricao))
    conexao.commit()
    print(f"✓ {nome} adicionada com sucesso!")

def exibir_registros(titulo, lista):
    # Função auxiliar para imprimir os resultados na tela de forma organizada
    print(f"\n--- {titulo} ---")
    if not lista:
        print("Nenhum registro encontrado.")
    for m in lista:
        # m[3] corresponde à coluna 'e_autista' no banco de dados
        autista_str = "Sim" if m[3] else "Não"
        print(f"Nome: {m[1]} | Área: {m[2]} | Autista: {autista_str} | Idade do Feito: {m[4]}")
        print(f"Descrição: {m[5]}")
        print("-" * 30)

def menu_principal():
    conexao = inicializar_banco()
    
    while True: # Loop infinito para manter o menu rodando até o usuário sair
        print("\n=== ARQUIVO DE MEMÓRIA: MULHERES HISTÓRICAS ===")
        print("1. Adicionar nova mulher")
        print("2. Ver todos os registros")
        print("3. Ver mulheres das Ciências")
        print("4. Ver mulheres autistas")
        print("5. Ver mulheres com grandes feitos após os 50 anos")
        print("6. Sair")
        
        opcao = input("\nEscolha uma opção: ")
        cursor = conexao.cursor()

        if opcao == '1':
            adicionar_mulher(conexao)
        elif opcao == '2':
            # SELECT * seleciona todas as colunas da tabela
            cursor.execute("SELECT * FROM mulheres")
            exibir_registros("Todos os Registros", cursor.fetchall())
        elif opcao == '3':
            # LIKE permite buscar palavras parciais (ex: 'Ciência' ou 'Neurociência')
            cursor.execute("SELECT * FROM mulheres WHERE area LIKE '%Ciencia%' OR area LIKE '%Ciência%'")
            exibir_registros("Mulheres nas Ciências", cursor.fetchall())
        elif opcao == '4':
            # 1 representa 'True' (Verdadeiro) no banco de dados SQLite
            cursor.execute("SELECT * FROM mulheres WHERE e_autista = 1")
            exibir_registros("Mulheres Autistas", cursor.fetchall())
        elif opcao == '5':
            # Operador >= filtra apenas valores numéricos a partir de 50
            cursor.execute("SELECT * FROM mulheres WHERE idade_feito_relevante >= 50")
            exibir_registros("Feitos Notáveis após os 50 anos", cursor.fetchall())
        elif opcao == '6':
            print("Encerrando sistema de memória...")
            conexao.close() # Sempre feche a conexão ao sair para não corromper o banco
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu_principal()