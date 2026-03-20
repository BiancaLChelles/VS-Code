import customtkinter as ctk
import sqlite3
from tkinter import messagebox
import os
import sys

# Configuração de estilo
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class SistemaMemoria(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Configurações da Janela Principal
        self.title("Dicionário de Memória")
        self.geometry("700x550") # Aumentei um pouco a altura para caber o novo botão

        self.configurar_banco()

        # --- Título ---
        self.label_titulo = ctk.CTkLabel(self, text="Arquivo de Memória e Força Feminina", font=("Roboto", 24, "bold"))
        self.label_titulo.pack(pady=20)

        # --- Frame de Ações Superiores ---
        self.frame_acoes = ctk.CTkFrame(self, fg_color="transparent")
        self.frame_acoes.pack(pady=10)

        # --- Botão para Abrir Cadastro ---
        self.btn_abrir_cadastro = ctk.CTkButton(
            self.frame_acoes, 
            text="+ Adicionar Nova Personalidade", 
            fg_color="#58A7D4", 
            hover_color="#3777A1",
            command=self.abrir_janela_cadastro
        )
        self.btn_abrir_cadastro.grid(row=0, column=0, padx=10)

        # --- NOVO BOTÃO: Memória Prévia ---
        self.btn_memoria_previa = ctk.CTkButton(
            self.frame_acoes, 
            text="Adicionar Personalidades Famosas", 
            fg_color="#58A7D4", 
            hover_color="#3777A1",
            command=self.rodar_alimentacao
        )
        self.btn_memoria_previa.grid(row=0, column=1, padx=10)

        # --- Frame de Filtros ---
        self.frame_filtros = ctk.CTkFrame(self)
        self.frame_filtros.pack(pady=10, padx=20, fill="x")

        self.btn_todas = ctk.CTkButton(self.frame_filtros, text="Ver Todas", width=150, command=self.listar_todas)
        self.btn_todas.grid(row=0, column=0, padx=15, pady=10)

        self.btn_autistas = ctk.CTkButton(self.frame_filtros, text="Autistas", fg_color="#6A5ACD", width=150, command=self.listar_autistas)
        self.btn_autistas.grid(row=0, column=1, padx=15, pady=10)

        self.btn_50mais = ctk.CTkButton(self.frame_filtros, text="Feitos 50+", fg_color="#D2691E", width=150, command=self.listar_50mais)
        self.btn_50mais.grid(row=0, column=2, padx=15, pady=10)

        # --- Área de Exibição ---
        self.texto_resultado = ctk.CTkTextbox(self, width=650, height=250, font=("Consolas", 12))
        self.texto_resultado.pack(pady=20, padx=20)

   
    def rodar_alimentacao(self):
        try:
            # Usamos a conexão que você já criou no configurar_banco
            cursor = self.conexao.cursor()

            # A lista de mulheres incríveis (Seeding)
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
                ("Greta Thunberg", "Ativismo/Ecologia", 1, 15, "Líder ambiental que mobilizou o mundo para a crise climática."),
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

            contador = 0
            for mulher in dados_para_inserir:
                cursor.execute("SELECT * FROM mulheres WHERE nome = ?", (mulher[0],))
                if cursor.fetchone() is None:
                    cursor.execute('''
                        INSERT INTO mulheres (nome, area, e_autista, idade_feito_relevante, descricao)
                        VALUES (?, ?, ?, ?, ?)
                    ''', mulher)
                    contador += 1
            
            self.conexao.commit()
            
            if contador > 0:
                messagebox.showinfo("Sucesso", f"Arquivo de Memória inicializado!\n{contador} novas personalidades adicionadas.")
            else:
                messagebox.showinfo("Sistema", "A memória prévia já está carregada no sistema.")
            
            self.listar_todas() # Atualiza a tela automaticamente

        except Exception as e:
            messagebox.showerror("Erro", f"Ocorreu um erro ao alimentar o banco: {e}")

    def abrir_janela_cadastro(self):
        # Cria uma nova janela (Toplevel)
        self.janela_cad = ctk.CTkToplevel(self)
        self.janela_cad.title("Cadastrar Personalidade")
        self.janela_cad.geometry("450x450")
        self.janela_cad.attributes("-topmost", True) # Mantém a janela na frente

        # Interface dentro da nova janela
        ctk.CTkLabel(self.janela_cad, text="Nova Personalidade", font=("Roboto", 18, "bold")).pack(pady=15)

        self.entry_nome = ctk.CTkEntry(self.janela_cad, placeholder_text="Nome da Mulher", width=350)
        self.entry_nome.pack(pady=5)

        self.entry_area = ctk.CTkEntry(self.janela_cad, placeholder_text="Área (Ciência, Artes...)", width=350)
        self.entry_area.pack(pady=5)

        self.entry_idade = ctk.CTkEntry(self.janela_cad, placeholder_text="Idade do Feito", width=350)
        self.entry_idade.pack(pady=5)

        self.check_artista = ctk.CTkCheckBox(self.janela_cad, text="É Autista?")
        self.check_artista.pack(pady=10)

        self.entry_desc = ctk.CTkTextbox(self.janela_cad, width=350, height=100)
        self.entry_desc.pack(pady=5)
        self.entry_desc.insert("1.0", "Descrição do feito...") # Placeholder manual para Textbox

        self.btn_salvar = ctk.CTkButton(self.janela_cad, text="Salvar no Banco", fg_color="#2E8B57", command=self.salvar_mulher)
        self.btn_salvar.pack(pady=20)

    def configurar_banco(self):
        self.conexao = sqlite3.connect("memoria_mulheres.db")
        cursor = self.conexao.cursor()
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
        self.conexao.commit()

    def salvar_mulher(self):
        nome = self.entry_nome.get()
        area = self.entry_area.get()
        autista = 1 if self.check_artista.get() else 0
        idade = self.entry_idade.get()
        # Pegando texto do CTkTextbox (da linha 1 caractere 0 até o fim)
        desc = self.entry_desc.get("1.0", "end-1c")

        if nome == "" or idade == "":
            messagebox.showwarning("Erro", "Nome e Idade são obrigatórios!")
            return

        try:
            cursor = self.conexao.cursor()
            cursor.execute('''
                INSERT INTO mulheres (nome, area, e_autista, idade_feito_relevante, descricao)
                VALUES (?, ?, ?, ?, ?)
            ''', (nome, area, autista, int(idade), desc))
            self.conexao.commit()
            
            messagebox.showinfo("Sucesso", f"{nome} foi adicionada!")
            self.janela_cad.destroy() # Fecha a janela após salvar
            self.listar_todas() # Atualiza a lista automaticamente
        except ValueError:
            messagebox.showerror("Erro", "A idade deve ser um número!")

    def exibir_na_tela(self, mulheres):
        self.texto_resultado.delete("1.0", "end")
        if not mulheres:
            self.texto_resultado.insert("end", "Nenhum registro encontrado.")
            return

        for m in mulheres:
            aut = "Sim" if m[3] else "Não"
            info = f"NOME: {m[1].upper()}\nÁREA: {m[2]} | AUTISTA: {aut} | IDADE: {m[4]}\nFEITO: {m[5]}\n"
            info += "="*60 + "\n"
            self.texto_resultado.insert("end", info)

    def listar_todas(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM mulheres")
        self.exibir_na_tela(cursor.fetchall())

    def listar_autistas(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM mulheres WHERE e_autista = 1")
        self.exibir_na_tela(cursor.fetchall())

    def listar_50mais(self):
        cursor = self.conexao.cursor()
        cursor.execute("SELECT * FROM mulheres WHERE idade_feito_relevante >= 50")
        self.exibir_na_tela(cursor.fetchall())

if __name__ == "__main__":
    app = SistemaMemoria()
    app.mainloop()