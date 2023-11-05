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

def fila_ordenada_crescente(fila):
    if fila.esta_vazia():
        return True  # A fila vazia é considerada ordenada

    elemento_anterior = fila.desenfileirar()
    ordenada = True

    while not fila.esta_vazia():
        elemento_atual = fila.desenfileirar()
        if elemento_atual < elemento_anterior:
            ordenada = False
            break
        elemento_anterior = elemento_atual

    return ordenada

# Exemplo de uso
minha_fila = Fila()
minha_fila.enfileirar(1)
minha_fila.enfileirar(2)
minha_fila.enfileirar(3)
minha_fila.enfileirar(5)

if fila_ordenada_crescente(minha_fila):
    print("A fila está ordenada de forma crescente.")
else:
    print("A fila não está ordenada de forma crescente.")
