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

def editor_de_texto():
    pilha = Pilha()
    
    while True:
        print("Editor de Texto Simples")
        print("1. Digitar")
        print("2. Apagar último caractere (#)")
        print("3. Apagar tudo (@)")
        print("4. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            caractere = input("Digite um caractere: ")
            pilha.empilhar(caractere)
        elif opcao == "2":
            if not pilha.vazia():
                pilha.desempilhar()
            else:
                print("A pilha está vazia. Nada para apagar.")
        elif opcao == "3":
            pilha = Pilha()  # Apaga tudo, reinicializando a pilha
        elif opcao == "4":
            break
        else:
            print("Opção inválida. Tente novamente.")
        
        # Exibir o conteúdo da pilha (texto atual)
        texto = ''.join(pilha.itens)
        print("Texto atual:", texto)
        print()

# Executar o editor de texto
editor_de_texto()
