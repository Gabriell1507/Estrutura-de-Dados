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

def decimal_para_binario(decimal):
    pilha = Pilha()
    
    while decimal > 0:
        resto = decimal % 2
        pilha.empilhar(resto)
        decimal = decimal // 2

    binario = ""
    while not pilha.vazia():
        binario += str(pilha.desempilhar())

    return binario

decimal = int(input("Digite um número decimal: "))
binario = decimal_para_binario(decimal)
print(f'O número binário equivalente é: {binario}')
