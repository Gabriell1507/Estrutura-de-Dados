class Livro:
    def __init__(self, nome):
        self.nome = nome
        self.disponivel = True
        self.fila_espera = Fila()

class Fila:
    def __init__(self):
        self.items = []

    def enfileirar(self, item):
        self.items.append(item)

    def desenfileirar(self):
        if not self.esta_vazia():
            return self.items.pop(0)
        else:
            return None

    def esta_vazia(self):
        return len(self.items) == 0

class Biblioteca:
    def __init__(self):
        self.livros = {}

    def cadastrar_livro(self, nome):
        if nome not in self.livros:
            self.livros[nome] = Livro(nome)
        else:
            print(f"O livro '{nome}' já está cadastrado na biblioteca.")

    def retirar_livro(self, nome, nome_pessoa):
        if nome in self.livros:
            livro = self.livros[nome]
            if livro.disponivel:
                livro.disponivel = False
                print(f"{nome_pessoa} retirou o livro '{nome}'.")
            else:
                print(f"O livro '{nome}' não está disponível. {nome_pessoa} foi adicionado à fila de espera.")
                livro.fila_espera.enfileirar(nome_pessoa)
        else:
            print(f"O livro '{nome}' não está cadastrado na biblioteca.")

    def devolver_livro(self, nome, nome_pessoa):
        if nome in self.livros:
            livro = self.livros[nome]
            if not livro.disponivel:
                livro.disponivel = True
                print(f"{nome_pessoa} devolveu o livro '{nome}'.")
                if not livro.fila_espera.esta_vazia():
                    proximo_na_fila = livro.fila_espera.desenfileirar()
                    print(f"{proximo_na_fila} retirou o livro '{nome}' da fila de espera.")
            else:
                print(f"O livro '{nome}' já está disponível.")
        else:
            print(f"O livro '{nome}' não está cadastrado na biblioteca.")

    def status_livro(self, nome):
        if nome in self.livros:
            livro = self.livros[nome]
            status = "disponível" if livro.disponivel else "não disponível"
            print(f"O livro '{nome}' está {status}.")
            if not livro.fila_espera.esta_vazia():
                fila = "Fila de espera: " + ", ".join(livro.fila_espera.items)
                print(fila)
        else:
            print(f"O livro '{nome}' não está cadastrado na biblioteca.")

# Exemplo de uso
biblioteca = Biblioteca()
biblioteca.cadastrar_livro("O Pequeno Príncipe")
biblioteca.cadastrar_livro("Maze Runner")

biblioteca.retirar_livro("O Pequeno Príncipe", "Alice")
biblioteca.retirar_livro("O Pequeno Príncipe", "Luis")  # Bob entra na fila de espera
biblioteca.retirar_livro("Maze Runner", "Anna")

biblioteca.status_livro("O Pequeno Príncipe")
biblioteca.devolver_livro("O Pequeno Príncipe", "Alice")  # Devolve o livro e passa para o próximo da fila
biblioteca.status_livro("O Pequeno Príncipe")
biblioteca.devolver_livro("Maze Runner", "Anna")  # Devolve o livro e passa para o próximo da fila

biblioteca.retirar_livro("O Pequeno Príncipe", "Gabriel")  # Próximo da fila retira o livro
