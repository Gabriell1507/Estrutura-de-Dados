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

def verifica_parenteses(equacao):
    pilha = Pilha()
    abertos = 0  # Contador de parênteses abertos
    fechados = 0  # Contador de parênteses fechados

    for caractere in equacao:
        if caractere == '(':
            pilha.empilhar(caractere)
            abertos += 1
        elif caractere == ')':
            if not pilha.vazia():
                pilha.desempilhar()
                fechados += 1
            else:
                return False, 0  # Parêntese fechado sem correspondente aberto

    if pilha.vazia():
        return abertos == fechados, abertos
    else:
        return False, 0  # Parêntese aberto sem correspondente fechado

# Exemplo de uso:
equacao = "((2 + 3) * (4 - 1))"
equilibrio, num_pares = verifica_parenteses(equacao)

if equilibrio:
    print(f"Os parênteses estão balanceados. Total de pares: {num_pares}")
else:
    print("Os parênteses não estão balanceados.")
