import sqlite3

def configurar_sistema_completo():
    # 1. Cria ou conecta ao arquivo do banco
    conexao = sqlite3.connect("memoria_mulheres.db")
    cursor = conexao.cursor()

    print("--- Inicializando Arquivo de Memória ---")

    # 2. Cria a tabela (mesmo código que você já tem, para garantir que o arquivo exista)
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

    # 3. Lista completa para alimentar o sistema (Seeding)
    # Note que aqui já padronizei os nomes para você
    dados_para_inserir = [
        ("Bell Hooks", "Literatura/Filosofia", 0, 30, "Autora fundamental que discutiu a interseccionalidade entre raça, gênero e classe."),
        ("Temple Grandin", "Ciência/Zootecnia", 1, 35, "Revolucionou a indústria pecuária e é uma das vozes mais famosas sobre o autismo."),
        ("Marie Curie", "Ciência/Física", 0, 36, "Primeira pessoa a ganhar dois prêmios Nobel em áreas diferentes (Física e Química)."),
        ("Ada Lovelace", "Ciência/Matemática", 0, 27, "Escreveu o primeiro algoritmo da história para ser lido por uma máquina."),
        ("Susan Boyle", "Artes/Música", 1, 47, "Cantora de sucesso mundial que descobriu o autismo na vida adulta."),
        ("Grace Hopper", "Ciência/Computação", 0, 53, "Criadora da linguagem COBOL e uma das primeiras programadoras da Marinha dos EUA."),
        ("Nise da Silveira", "Ciência/Psiquiatria", 0, 40, "Médica brasileira que lutou contra tratamentos agressivos usando a arte."),
        ("Toni Morrison", "Literatura", 0, 62, "Ganhou o Nobel de Literatura após décadas de produção intelectual profunda."),
        ("Hedy Lamarr", "Ciência/Invenção", 0, 28, "Atriz que inventou a base da tecnologia que usamos hoje para o Wi-Fi."),
        ("Greta Thunberg", "Ativismo/Ecologia", 1, 15, "Líder ambiental que mobilizou o mundo para a crise climática.")
    ]

    # 4. Inserindo os dados com segurança
    for mulher in dados_para_inserir:
        # Verificamos se já existe para não duplicar se você rodar sem querer de novo
        cursor.execute("SELECT * FROM mulheres WHERE nome = ?", (mulher[0],))
        if cursor.fetchone() is None:
            cursor.execute('''
                INSERT INTO mulheres (nome, area, e_autista, idade_feito_relevante, descricao)
                VALUES (?, ?, ?, ?, ?)
            ''', mulher)
            print(f"✓ {mulher[0]} adicionada com sucesso.")
        else:
            print(f"! {mulher[0]} já está no banco.")

    # 5. Salva e fecha
    conexao.commit()
    conexao.close()
    print("\n--- Sistema alimentado e pronto para uso! ---")

if __name__ == "__main__":
    configurar_sistema_completo()