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

class Pilha:
    def __init__(self):
        self.items = []

    def empilhar(self, item):
        self.items.append(item)

    def desempilhar(self):
        if not self.esta_vazia():
            return self.items.pop()
        else:
            return None

    def esta_vazia(self):
        return len(self.items) == 0

def inverter_fila_com_pilha(F1):
    F2 = Fila()  # Fila invertida
    pilha_temporaria = Pilha()

    while not F1.esta_vazia():
        elemento = F1.desenfileirar()
        pilha_temporaria.empilhar(elemento)

    while not pilha_temporaria.esta_vazia():
        elemento = pilha_temporaria.desempilhar()
        F2.enfileirar(elemento)

    return F2

# Exemplo de uso
fila_original = Fila()
fila_original.enfileirar(1)
fila_original.enfileirar(2)
fila_original.enfileirar(3)
fila_original.enfileirar(4)

print("Fila original:")
while not fila_original.esta_vazia():
    elemento = fila_original.desenfileirar()
    print(elemento, end=' ')

fila_original.enfileirar(1)
fila_original.enfileirar(2)
fila_original.enfileirar(3)
fila_original.enfileirar(4)

fila_invertida = inverter_fila_com_pilha(fila_original)

print("\nFila invertida:")
while not fila_invertida.esta_vazia():
    print(fila_invertida.desenfileirar(), end=' ')
