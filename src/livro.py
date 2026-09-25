class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def mostrar(self):
        status = "Disponível" if self.disponivel else "Emprestado"

        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Status: {status}")