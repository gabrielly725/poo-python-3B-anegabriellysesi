class Conteudo:
    def __init__(self, titulo, genero):


        
        self.titulo = titulo
        self.genero = genero

    def exibir_info(self):
        print(f"Título: {self.titulo} | Gênero: {self.genero}")


class Filme(Conteudo):
    def __init__(self, titulo, genero, duracao):
        super().__init__(titulo, genero)
        self.duracao = duracao

    def exibir_info(self):
        print(f"Filme: {self.titulo} | Gênero: {self.genero} | Duração: {self.duracao} minutos")


class Serie(Conteudo):
    def __init__(self, titulo, genero, temporadas):
        super().__init__(titulo, genero)
        self.temporadas = temporadas

    def exibir_info(self):
        print(f"Série: {self.titulo} | Gênero: {self.genero} | Temporadas: {self.temporadas}")


class Documentario(Conteudo):
    def __init__(self, titulo, genero, tema):
        super().__init__(titulo, genero)
        self.tema = tema

    def exibir_info(self):
        print(f"Documentário: {self.titulo} | Gênero: {self.genero} | Tema: {self.tema}")


class Podcast(Conteudo):
    def __init__(self, titulo, genero, episodios):
        super().__init__(titulo, genero)
        self.episodios = episodios

    def exibir_info(self):
        print(f"Podcast: {self.titulo} | Gênero: {self.genero} | Episódios: {self.episodios}")


catalogo = [
    Filme("A hora do rush", "Acao", 98),
    Filme("As branquelas", "Comedia", 109),
    Serie("Stranger Things", "Terror", 5),
    Serie("O mentalista", "Investigacao", 7),
    Documentario("Senna", "Esporte", "Carreira"),
    Documentario("Amy", "Musical", "Vicios"),
    Podcast("Podpah", "Entretenimento", 1090)
]


for item in catalogo:
    item.exibir_info()
         


