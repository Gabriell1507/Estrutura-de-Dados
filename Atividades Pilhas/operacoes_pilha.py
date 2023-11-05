class Pilha:
    def __init__(self, tamanho_maximo):
        self.tamanho_maximo = tamanho_maximo
        self.itens = [None] * tamanho_maximo
        self.topo = -1

    def vazia(self):
        return self.topo == -1

    def cheia(self):
        return self.topo == self.tamanho_maximo - 1

    def push(self, item):
        if not self.cheia():
            self.topo += 1
            self.itens[self.topo] = item
        else:
            print("A pilha está cheia. Não é possível empilhar mais itens.")

    def pop(self):
        if not self.vazia():
            item = self.itens[self.topo]
            self.topo -= 1
            return item
        else:
            print("A pilha está vazia. Não é possível desempilhar.")

    def top(self):
        if not self.vazia():
            return self.itens[self.topo]
        else:
            print("A pilha está vazia. Não há elemento no topo.")

# Exemplo de uso:
tamanho_maximo = 10
pilha = Pilha(tamanho_maximo)

print("A pilha está vazia?", pilha.vazia())
print("A pilha está cheia?", pilha.cheia())

pilha.push(1)
pilha.push(2)
pilha.push(3)

print("Topo da pilha:", pilha.top())
print("Desempilhando:", pilha.pop())

print("Topo da pilha após desempilhar:", pilha.top())
print("A pilha está vazia?", pilha.vazia())
