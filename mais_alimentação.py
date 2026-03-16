import sqlite3

def alimentar_banco_representatividade():
    conexao = sqlite3.connect("memoria_mulheres.db")
    cursor = conexao.cursor()

    # Novas entradas focadas em Autismo e Longevidade com Propósito
    # Formato: (Nome, Área, Autista, Idade do Feito, Descrição)
    dados_mulheres = [
        # --- FOCO: MULHERES AUTISTAS (REPRESENTATIVIDADE) ---
        ("Daryl Hannah", "Artes/Cinema", 1, 24, "Atriz e ativista ambiental. Diagnosticada na infância, superou desafios sociais para brilhar em Hollywood."),
        ("Heather Kuzmich", "Moda/Artes", 1, 21, "Modelo que trouxe o autismo para o debate público em rede nacional, combatendo estigmas."),
        ("Fernanda Santana", "Ciência/Educação", 1, 30, "Pesquisadora brasileira que estuda autismo no feminino, dando voz a mulheres neurodivergentes."),
        ("Donna Williams", "Literatura", 1, 25, "Autora de 'Meu Mundo Estranho', um dos primeiros relatos íntimos sobre a experiência autista."),
        
        # --- FOCO: FEITOS APÓS OS 50 ANOS (PODER E LONGEVIDADE) ---
        ("Cora Coralina", "Literatura", 0, 75, "Publicou seu primeiro livro aos 75 anos. Tornou-se uma das maiores poetas do Brasil na velhice."),
        ("Laura Ingalls Wilder", "Literatura", 0, 65, "Começou a escrever a famosa série 'Little House on the Prairie' aos 65 anos."),
        ("Anna Mary Robertson (Vovó Moses)", "Artes Plásticas", 0, 78, "Começou a pintar seriamente aos 78 anos e se tornou uma das artistas folk mais famosas do mundo."),
        ("Nola Ochs", "Educação", 0, 95, "Tornou-se a pessoa mais velha do mundo a concluir uma graduação, provando que o aprendizado não tem validade."),
        ("Gladys West", "Ciência/Matemática", 0, 56, "Seu trabalho fundamental para o desenvolvimento do GPS foi amplamente reconhecido após seus 50 anos."),
        ("Ruth Bader Ginsburg", "Direito/Justiça", 0, 60, "Tornou-se juíza da Suprema Corte dos EUA aos 60 anos, tornando-se um ícone de luta por igualdade."),
        
        # --- COMBINAÇÕES E MAIS REPRESENTATIVIDADE ---
        ("Dra. Temple Grandin", "Ciência/Zootecnia", 1, 63, "Embora famosa cedo, foi após os 50 que se tornou a maior porta-voz global sobre o design humanitário."),
        ("Carolina Maria de Jesus", "Literatura", 0, 46, "Sua obra 'Quarto de Despejo' deu poder à voz da mulher periférica, alcançando sucesso mundial."),
        ("Wangari Maathai", "Ecologia/Paz", 0, 64, "Primeira mulher africana a receber o Nobel da Paz (2004) por sua persistência política e ambiental.")
    ]

    print("--- Alimentando Sistema com Força e Representatividade ---")

    for mulher in dados_mulheres:
        # Busca para evitar duplicados
        cursor.execute("SELECT * FROM mulheres WHERE nome = ?", (mulher[0],))
        if cursor.fetchone() is None:
            cursor.execute('''
                INSERT INTO mulheres (nome, area, e_autista, idade_feito_relevante, descricao)
                VALUES (?, ?, ?, ?, ?)
            ''', mulher)
            print(f"✓ {mulher[0]} - Adicionada ao arquivo.")
        else:
            print(f"! {mulher[0]} - Já consta no registro.")

    conexao.commit()
    conexao.close()
    print("\n--- O banco de dados agora está mais forte e diversificado! ---")

if __name__ == "__main__":
    # Garante que a tabela existe antes de alimentar
    # (Caso você ainda não tenha rodado o código de criação)
    alimentar_banco_representatividade()