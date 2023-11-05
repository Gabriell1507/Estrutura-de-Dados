class FilaGenerica:
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

# Exemplo de uso
fila = FilaGenerica()

fila.enfileirar(1)
fila.enfileirar('A')
fila.enfileirar("Estrutura de Dados")
fila.enfileirar("ADS M4")

while not fila.esta_vazia():
    elemento = fila.desenfileirar()
    print(elemento)
