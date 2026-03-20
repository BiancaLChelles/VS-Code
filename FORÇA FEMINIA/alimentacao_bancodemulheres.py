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
     # --- ORIGINAIS (TODAS MULHERES) ---
    ("Bell Hooks", "Literatura/Filosofia", 0, 30, "Autora fundamental que discutiu a interseccionalidade entre raça, gênero e classe."),
    ("Temple Grandin", "Ciência/Zootecnia", 1, 35, "Revolucionou a indústria pecuária e é uma das vozes mais famosas sobre o autismo."),
    ("Marie Curie", "Ciência/Física", 0, 36, "Primeira pessoa a ganhar dois prêmios Nobel em áreas diferentes (Física e Química)."),
    ("Ada Lovelace", "Ciência/Matemática", 0, 27, "Escreveu o primeiro algoritmo da história para ser lido por uma máquina."),
    ("Susan Boyle", "Artes/Música", 1, 47, "Cantora de sucesso mundial que descobriu o autismo na vida adulta."),
    ("Grace Hopper", "Ciência/Computação", 0, 53, "Criadora da linguagem COBOL e uma das primeiras programadoras da Marinha dos EUA."),
    ("Nise da Silveira", "Ciência/Psiquiatria", 0, 40, "Médica brasileira que lutou contra tratamentos agressivos usando a arte."),
    ("Toni Morrison", "Literatura", 0, 62, "Ganhou o Nobel de Literatura após décadas de produção intelectual profunda."),
    ("Hedy Lamarr", "Ciência/Invenção", 0, 28, "Atriz que inventou a base da tecnologia que usamos hoje para o Wi-Fi."),
    ("Greta Thunberg", "Ativismo/Ecologia", 1, 15, "Líder ambiental que mobilizou o mundo para a crise climática."),

    # --- MULHERES AUTISTAS (Totalizando 20+) ---
    ("Daryl Hannah", "Artes/Cinema", 1, 21, "Atriz e ativista que revelou como o autismo impactou sua carreira em Hollywood."),
    ("Sia Furler", "Artes/Música", 1, 47, "Compositora e cantora pop que compartilhou publicamente seu diagnóstico tardio."),
    ("Courtney Love", "Artes/Música", 1, 28, "Líder da banda Hole e figura grunge, diagnosticada com autismo na infância."),
    ("Donna Williams", "Literatura/Artes", 1, 29, "Autora autista que escreveu 'Meu mundo não é o seu', ajudando a entender a neurodiversidade."),
    ("Hannah Gadsby", "Artes/Comédia", 1, 39, "Comediante que discute abertamente seu diagnóstico e a percepção visual do autismo."),
    ("Kayla Cromer", "Artes/Cinema", 1, 21, "Primeira atriz autista a interpretar uma personagem principal autista em uma série."),
    ("Anne Hegerty", "Televisão/Lógica", 1, 45, "Famosa competidora de quizzes que descobriu o autismo na vida adulta."),
    ("Wendy Lawson", "Psicologia", 1, 42, "Psicóloga e pesquisadora autista que foca em como o cérebro processa informações."),
    ("Liane Holliday Willey", "Educação", 1, 35, "Doutora em educação que cunhou termos sobre a experiência feminina no espectro."),
    ("Talia Grant", "Artes/Atuação", 1, 16, "Atriz que trouxe visibilidade para jovens mulheres negras autistas na TV."),
    ("Fern Brady", "Artes/Literatura", 1, 34, "Comediante e autora que descreve a experiência de ser diagnosticada tardiamente."),
    ("Chloé Hayden", "Ativismo/Artes", 1, 24, "Autora e atriz que promove a aceitação da neurodivergência de forma vibrante."),

    # --- MULHERES 50+ (Feitos após os 50 anos - Totalizando 20+) ---
    ("Gladys West", "Ciência/Geodésia", 0, 56, "Desenvolveu os modelos matemáticos que permitiram a criação do GPS."),
    ("Dorothy Vaughan", "Ciência/Matemática", 0, 51, "Liderou a transição da NASA para computadores digitais ensinando Fortran."),
    ("Julia Child", "Gastronomia", 0, 51, "Lançou seu primeiro programa de TV, revolucionando o ensino culinário."),
    ("Anna Mary Robertson", "Artes/Pintura", 0, 78, "Conhecida como Grandma Moses, iniciou sua carreira artística de sucesso na velhice."),
    ("Laura Ingalls Wilder", "Literatura", 0, 65, "Começou a publicar sua famosa série de livros biográficos."),
    ("Mary Delany", "Artes/Botânica", 0, 71, "Criou um novo estilo de arte botânica com colagens de papel precisas."),
    ("Vera Wang", "Moda", 0, 50, "Embora tenha começado aos 40, consolidou seu império de moda global após os 50."),
    ("Wangari Maathai", "Ativismo/Ecologia", 0, 64, "Primeira mulher africana a ganhar o Nobel da Paz pelo Movimento Cinturão Verde."),
    ("Lise Meitner", "Ciência/Física", 0, 60, "Física que identificou a fissão nuclear, feito reconhecido mundialmente na maturidade."),
    ("Ruth Bader Ginsburg", "Direito/Justiça", 0, 60, "Tornou-se juíza da Suprema Corte dos EUA, onde lutou pela igualdade de gênero."),
    ("Louise Bourgeois", "Artes/Escultura", 0, 71, "Alcançou o auge da fama mundial com suas esculturas de aranhas gigantes após os 70."),
    ("Emmeline Pankhurst", "Política/Ativismo", 0, 50, "Liderou as ações mais intensas do movimento sufragista britânico na maturidade."),
    ("Beatrix Potter", "Ciência/Literatura", 0, 50, "Focou em conservação ambiental e gestão de terras agrícolas após o sucesso literário."),
    ("Rachel Carson", "Ciência/Ecologia", 0, 55, "Publicou 'Primavera Silenciosa', mudando a legislação ambiental do mundo."),
    ("Alice Munro", "Literatura", 0, 82, "Venceu o Nobel de Literatura após décadas aprimorando a arte do conto."),
    ("Margaret Thatcher", "Política", 0, 53, "Primeira mulher a se tornar Primeira-Ministra do Reino Unido."),
    ("Zora Neale Hurston", "Antropologia/Literatura", 0, 50, "Publicou trabalhos fundamentais sobre folclore e identidade negra na maturidade."),
    ("Estée Lauder", "Negócios/Beleza", 0, 55, "Consolidou sua empresa como uma gigante global de cosméticos na maturidade."),
    ("Diana Nyad", "Esportes", 0, 64, "Nadadora que completou a travessia de Cuba à Flórida sem gaiola de tubarões aos 64."),
    ("Mary Jackson", "Ciência/Engenharia", 0, 51, "Tornou-se a primeira engenheira negra da NASA após lutar pelo direito de estudar."),

    # --- OUTRAS MULHERES: CIÊNCIA, TECNOLOGIA E CULTURA ---
    ("Katherine Johnson", "Ciência/Matemática", 0, 43, "Matemática cujos cálculos manuais garantiram o retorno seguro de astronautas da NASA."),
    ("Margaret Hamilton", "Ciência/Computação", 0, 33, "Liderou o software da Apollo 11; cunhou o termo 'Engenharia de Software'."),
    ("Radia Perlman", "Ciência/Redes", 0, 34, "Inventou o protocolo STP, sem o qual a internet moderna não funcionaria."),
    ("Rosalind Franklin", "Ciência/Biologia", 0, 31, "Obteve a Foto 51, essencial para descobrir a estrutura em dupla hélice do DNA."),
    ("Enedina Alves Marques", "Ciência/Engenharia", 0, 32, "Primeira engenheira negra do Brasil, pioneira em grandes obras no Paraná."),
    ("Annie Easley", "Ciência/Computação", 0, 40, "Desenvolveu códigos para foguetes que serviram de base para baterias de carros híbridos."),
    ("Chien-Shiung Wu", "Ciência/Física", 0, 44, "Conhecida como 'Rainha da Física', realizou experimentos que mudaram a física quântica."),
    ("Evelyn Boyd Granville", "Ciência/Matemática", 0, 32, "Uma das primeiras doutoras negras em matemática, trabalhou em cálculos orbitais."),
    ("Sophie Germain", "Ciência/Matemática", 0, 35, "Estudou teoria dos números e elasticidade sob um pseudônimo masculino para ser ouvida."),
    ("Hypatia de Alexandria", "Filosofia/Astronomia", 0, 40, "Matemática e astrônoma que liderou o pensamento filosófico no Egito antigo."),
    ("Valentina Tereshkova", "Ciência/Aeroespacial", 0, 26, "Primeira mulher a orbitar a Terra, completando 48 voltas no espaço."),
    ("Bertha Lutz", "Ciência/Política", 0, 40, "Bióloga brasileira que liderou a conquista do voto feminino no Brasil."),
    ("Dandara dos Palmares", "Política/Guerra", 0, 30, "Líder guerreira que lutou pela liberdade no Quilombo dos Palmares."),
    ("Shirley Ann Jackson", "Ciência/Física", 0, 30, "Suas pesquisas em física teórica permitiram a invenção da fibra óptica e do fax."),
    ("Elizabeth Blackwell", "Ciência/Medicina", 0, 28, "Primeira mulher a se formar médica nos EUA, abrindo caminho para outras mulheres."),
    ("Mary Kenneth Keller", "Ciência/Computação", 0, 51, "Primeira mulher a receber um doutorado em computação; ajudou a desenvolver o BASIC."),
    ("Carol Shaw", "Ciência/Jogos", 0, 27, "Primeira mulher designer e programadora de jogos eletrônicos profissional."),
    ("Lynn Conway", "Ciência/Hardware", 0, 40, "Pioneira em design de chips VLSI e defensora dos direitos de pessoas trans.")
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