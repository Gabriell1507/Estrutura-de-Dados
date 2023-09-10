class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x}, {self.y})'

class Reta:
    def __init__(self, ponto1, ponto2):
        self.ponto1 = ponto1
        self.ponto2 = ponto2

    def __str__(self):
        return f'Reta de {self.ponto1} para {self.ponto2}'

class PolinomioGrau2:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calcular(self, x):
        return self.a * x**2 + self.b * x + self.c

    def __str__(self):
        return f'{self.a}x^2 + {self.b}x + {self.c}'

# Exemplo de uso das classes:
ponto1 = Ponto(1, 2)
ponto2 = Ponto(3, 4)
reta = Reta(ponto1, ponto2)
polinomio = PolinomioGrau2(1, -3, 2)

print(f"Ponto 1: {ponto1}")
print(f"Reta: {reta}")
print(f"Polinômio: {polinomio}")
x = 5
resultado_polinomio = polinomio.calcular(x)
print(f"Valor do polinômio para x = {x}: {resultado_polinomio}")
