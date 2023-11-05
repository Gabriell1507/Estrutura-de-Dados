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

    def __eq__(self, outra_pilha):
        if len(self.itens) != len(outra_pilha.itens):
            return False

        for item1, item2 in zip(self.itens, outra_pilha.itens):
            if item1 != item2:
                return False

        return True

def sao_pilhas_iguais(pilha1, pilha2):
    return pilha1 == pilha2

# Criar duas pilhas
pilha1 = Pilha()
pilha2 = Pilha()

# Preencher as pilhas
pilha1.empilhar(1)
pilha1.empilhar(2)
pilha1.empilhar(3)

pilha2.empilhar(1)
pilha2.empilhar(2)
pilha2.empilhar(3)

# Verificar se as pilhas são iguais
resultado = sao_pilhas_iguais(pilha1, pilha2)
print("As pilhas são iguais?", resultado)
