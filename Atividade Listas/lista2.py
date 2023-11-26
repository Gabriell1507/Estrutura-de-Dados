class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def esta_vazia(self):
        return self.inicio is None

    def exibir(self):
        atual = self.inicio
        while atual:
            print(atual.dado, end=" -> ")
            atual = atual.proximo
        print("Nenhum")

    def inserir_no_meio(self, dado, posicao):
        novo_no = No(dado)

        if posicao == 0:
            novo_no.proximo = self.inicio
            self.inicio = novo_no
            return

        atual = self.inicio
        posicao_atual = 0

        while posicao_atual < posicao - 1 and atual.proximo is not None:
            atual = atual.proximo
            posicao_atual += 1

        if atual is None:
            raise Exception("Posição fora dos limites")

        novo_no.proximo = atual.proximo
        atual.proximo = novo_no

    def remover_do_meio(self, posicao):
        if self.esta_vazia():
            raise Exception("A lista está vazia")

        if posicao == 0:
            self.inicio = self.inicio.proximo
            return

        atual = self.inicio
        posicao_atual = 0

        while posicao_atual < posicao - 1 and atual.proximo is not None:
            atual = atual.proximo
            posicao_atual += 1

        if atual is None or atual.proximo is None:
            raise Exception("Posição fora dos limites")

        atual.proximo = atual.proximo.proximo

# Exemplo de Uso
lista = ListaEncadeada()

# Inserindo elementos no meio
lista.inserir_no_meio(1, 0)
print("Lista após inserção:")
lista.exibir()

lista.inserir_no_meio(3, 1)
print("\nLista após inserção:")
lista.exibir()
print('Insere 3 no meio da lista')


lista.inserir_no_meio(2, 1)

print("\nLista após inserção:")
lista.exibir()
print('Insere 2 no meio da lista')

# Removendo elemento do meio
lista.remover_do_meio(1)
print("\nLista após a remoção:")
lista.exibir()
print('Remove 2 do meio da lista')
