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

def interpretar_notacao_posfixa(expressao):
    pilha = Pilha()
    operadores = "+-*/"

    # Divide a expressão posfixa em tokens (números e operadores)
    tokens = expressao.split()

    for token in tokens:
        if token not in operadores:
            # Se for um operando, converta para número e empilhe
            pilha.empilhar(int(token))
        else:
            # Se for um operador, desempilhe operandos, calcule e empilhe o resultado
            operando2 = pilha.desempilhar()
            operando1 = pilha.desempilhar()
            if token == '+':
                resultado = operando1 + operando2
            elif token == '-':
                resultado = operando1 - operando2
            elif token == '*':
                resultado = operando1 * operando2
            elif token == '/':
                resultado = operando1 / operando2
            pilha.empilhar(resultado)

    # O resultado final estará no topo da pilha
    return pilha.desempilhar()

# Exemplo de uso:
expressao_posfixa = "150 2 * 33 +"
resultado = interpretar_notacao_posfixa(expressao_posfixa)
print("Resultado:", resultado)
