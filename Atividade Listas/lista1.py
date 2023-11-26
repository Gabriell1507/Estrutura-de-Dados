class Lista:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.lista = [None] * tamanho
        self.tamanho_atual = 0

    def inserir(self, elemento, posicao):
        if posicao < 0 or posicao > self.tamanho_atual or self.tamanho_atual == self.tamanho:
            raise IndexError("Posição inválida ou lista cheia")

        for i in range(self.tamanho_atual, posicao, -1):
            self.lista[i] = self.lista[i - 1]

        self.lista[posicao] = elemento
        self.tamanho_atual += 1

    def imprimir(self):
        print(self.lista[:self.tamanho_atual])

    def concatenar(self, outra_lista):
        nova_tamanho = self.tamanho_atual + outra_lista.tamanho_atual
        nova_lista = Lista(nova_tamanho)

        for i in range(self.tamanho_atual):
            nova_lista.inserir(self.lista[i], i)

        for i in range(outra_lista.tamanho_atual):
            nova_lista.inserir(outra_lista.lista[i], self.tamanho_atual + i)

        return nova_lista

    def dividir(self, posicao):
        if posicao < 0 or posicao >= self.tamanho_atual:
            raise IndexError("Posição inválida")

        lista1 = Lista(posicao)
        lista2 = Lista(self.tamanho_atual - posicao)

        for i in range(posicao):
            lista1.inserir(self.lista[i], i)

        for i in range(posicao, self.tamanho_atual):
            lista2.inserir(self.lista[i], i - posicao)

        return lista1, lista2

    def copiar(self):
        nova_lista = Lista(self.tamanho)

        for i in range(self.tamanho_atual):
            nova_lista.inserir(self.lista[i], i)

        return nova_lista

    def pesquisar(self, elemento):
        for i in range(self.tamanho_atual):
            if self.lista[i] == elemento:
                return i

        return -1

# Exemplo de uso:
lista1 = Lista(5)
lista1.inserir(1, 0)
lista1.inserir(2, 1)
lista1.inserir(3, 2)

lista2 = Lista(3)
lista2.inserir(4, 0)
lista2.inserir(5, 1)

# Concatenação
lista_concatenada = lista1.concatenar(lista2)
print('Lista concatenada:')
lista_concatenada.imprimir()  # Saída: [1, 2, 3, 4, 5]

# Divisão
lista_dividida1, lista_dividida2 = lista_concatenada.dividir(3)
print('Lista dividida:')
lista_dividida1.imprimir()  # Saída: [1, 2, 3]
lista_dividida2.imprimir()  # Saída: [4, 5]

# Cópia
copia_lista1 = lista1.copiar()
print('Cópia da lista 1:')
copia_lista1.imprimir()  # Saída: [1, 2, 3]

copia_lista2 = lista2.copiar()
print('Cópia da lista 2:')
copia_lista2.imprimir()  # Saída: [4, 5]

# Pesquisa
posicao_elemento = lista_concatenada.pesquisar(3)
print('Posição do elemento 3:')
print(posicao_elemento)  # Saída: 2
