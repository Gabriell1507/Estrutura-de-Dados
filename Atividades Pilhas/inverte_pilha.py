class Pilha:
    def __init__(self):
        self.itens = []

    def vazia(self):
        return len(self.itens) == 0

    def empilhar(self, item):
        self.itens.append(item)

    def desempilhar(self):
        if not self.vazia():
            return self.itens.pop()
        else:
            return None

    def topo(self):
        if not self.vazia():
            return self.itens[-1]
        else:
            return None

    def inverter(self):
        self.itens = self.itens[::-1]

# Exemplo de uso:
pilha = Pilha()

pilha.empilhar(1)
pilha.empilhar(2)
pilha.empilhar(3)

print("Pilha original:", pilha.itens)

pilha.inverter()

print("Pilha invertida:", pilha.itens)
