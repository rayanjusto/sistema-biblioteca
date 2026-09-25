class Biblioteca:

    def __init__(self):
        self.livros = []
        self.usuarios = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def cadastrar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_livros(self):

        if len(self.livros) == 0:
            print("Nenhum livro cadastrado.")
            return

        for i, livro in enumerate(self.livros, 1):
            print(f"\nLivro {i}")
            livro.mostrar()

    def buscar_livro(self, titulo):

        for livro in self.livros:

            if livro.titulo.lower() == titulo.lower():
                return livro

        return None

    def emprestar_livro(self, titulo):

        livro = self.buscar_livro(titulo)

        if livro is None:
            print("Livro não encontrado.")

        elif not livro.disponivel:
            print("Livro já está emprestado.")

        else:
            livro.disponivel = False
            print("Livro emprestado com sucesso!")

    def devolver_livro(self, titulo):

        livro = self.buscar_livro(titulo)

        if livro is None:
            print("Livro não encontrado.")

        elif livro.disponivel:
            print("Esse livro já está disponível.")

        else:
            livro.disponivel = True
            print("Livro devolvido com sucesso!")