from livro import Livro
from usuario import Usuario
from biblioteca import Biblioteca


biblioteca = Biblioteca()


while True:

    print("\n===== SISTEMA DE BIBLIOTECA =====")
    print("1 - Cadastrar livro")
    print("2 - Listar livros")
    print("3 - Buscar livro")
    print("4 - Cadastrar usuário")
    print("5 - Emprestar livro")
    print("6 - Devolver livro")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")

        livro = Livro(titulo, autor)

        biblioteca.cadastrar_livro(livro)

        print("Livro cadastrado com sucesso!")

    elif opcao == "2":

        biblioteca.listar_livros()

    elif opcao == "3":

        titulo = input("Digite o título do livro: ")

        livro = biblioteca.buscar_livro(titulo)

        if livro:
            livro.mostrar()
        else:
            print("Livro não encontrado.")

    elif opcao == "4":

        nome = input("Digite o nome do usuário: ")

        usuario = Usuario(nome)

        biblioteca.cadastrar_usuario(usuario)

        print("Usuário cadastrado com sucesso!")

    elif opcao == "5":

        titulo = input("Digite o título do livro: ")

        biblioteca.emprestar_livro(titulo)

    elif opcao == "6":

        titulo = input("Digite o título do livro: ")

        biblioteca.devolver_livro(titulo)

    elif opcao == "0":

        print("Programa encerrado.")
        break

    else:

        print("Opção inválida.")