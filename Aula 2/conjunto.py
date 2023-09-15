#Atividade feita junto com o aluno Armando Pereira de Sousa


class ConjuntoInteiro:
    def __init__(self):
        self.elementos = set()

    # Metodos basicos
    def adicionar(self, elemento):
        self.elementos.add(elemento)

    def remover(self, elemento):
        self.elementos.remove(elemento)

    def contem(self, elemento):
        return elemento in self.elementos

    def tamanho(self):
        return len(self.elementos)

    # Operacoes
    def uniao(self, conjunto):
        uniao = ConjuntoInteiro()
        for elemento in self.elementos:
            if elemento not in conjunto.elementos:
                uniao.adicionar(elemento)
        for elemento in conjunto.elementos:
            if elemento not in self.elementos:
                uniao.adicionar(elemento)
        return uniao

    def intersecao(self, conjunto):
        intersecao = ConjuntoInteiro()
        for elemento in self.elementos:
            if elemento in conjunto.elementos:
                intersecao.adicionar(elemento)
        return intersecao

    def diferenca(self, conjunto):
        diferenca = ConjuntoInteiro()
        for elemento in self.elementos:
            if elemento not in conjunto.elementos:
                diferenca.adicionar(elemento)
        return diferenca

    def membro(self, elemento):
        return elemento in self.elementos

    def atribuir(self, conjunto):
        self.elementos = conjunto.elementos

    def minimo(self):
        valorminimo = None
        for elemento in self.elementos:
            if valorminimo is None or elemento < valorminimo:
                valorminimo = elemento
        return valorminimo

    def maximo(self):
        valormaximo = None
        for elemento in self.elementos:
            if valormaximo is None or elemento > valormaximo:
                valormaximo = elemento
        return valormaximo

    def igual(self, conjunto):
        return self.elementos == conjunto.elementos

    def liberar(self):
        self.elementos = set()

    def imprimir(self):
        print(self.elementos)


# Criar conjuntos
conjuntoA = ConjuntoInteiro()
conjuntoB = ConjuntoInteiro()

# Adicionar elementos
conjuntoA.adicionar(1)
conjuntoA.adicionar(2)
conjuntoA.adicionar(3)

conjuntoB.adicionar(3)
conjuntoB.adicionar(4)
conjuntoB.adicionar(5)

# Imprimir conjuntos
print("Conjunto A:")
conjuntoA.imprimir()  # Deve imprimir: {1, 2, 3}

print("\nConjunto B:")
conjuntoB.imprimir()  # Deve imprimir: {3, 4, 5}

# Verificar pertencimento
print("\nVerificação de pertencimento:")
print("2 pertence ao conjunto A:", conjuntoA.contem(2))  # Deve imprimir: True
print("6 pertence ao conjunto A:", conjuntoA.contem(6))  # Deve imprimir: False

# Realizar operações de conjunto
conjuntoC = conjuntoA.uniao(conjuntoB)
print("\nUnião de A e B em C:")
conjuntoC.imprimir()  # Deve imprimir: {1, 2, 3, 4, 5}

conjuntoD = conjuntoA.intersecao(conjuntoB)
print("\nInterseção de A e B em D:")
conjuntoD.imprimir()  # Deve imprimir: {3}

conjuntoE = conjuntoA.diferenca(conjuntoB)
print("\nDiferença de A - B em E:")
conjuntoE.imprimir()  # Deve imprimir: {1, 2}

# Remover um elemento
conjuntoA.remover(1)
print("\nRemoção do elemento 1 de A:")
conjuntoA.imprimir()  # Deve imprimir: {2, 3}

# Atribuir um conjunto a outro
conjuntoF = ConjuntoInteiro()
conjuntoF.atribuir(conjuntoA)
print("\nAtribuição de A para F:")
conjuntoF.imprimir()  # Deve imprimir: {2, 3}

# Encontrar o mínimo e o máximo
print("\nMínimo de A:", conjuntoA.minimo())  # Deve imprimir: 2
print("Máximo de A:", conjuntoA.maximo())  # Deve imprimir: 3

# Verificar igualdade
print("\nIgualdade entre A e B:", conjuntoA.igual(conjuntoB))  # Deve imprimir: False
print("Igualdade entre A e F:", conjuntoA.igual(conjuntoF))  # Deve imprimir: True

# Liberar um conjunto
conjuntoA.liberar()
print("\nConjunto A após liberação:")
conjuntoA.imprimir()  # Deve imprimir: {}
