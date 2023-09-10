class Agenda:
    def __init__(self):
        # Inicializa a agenda como um dicionário vazio (nome: endereço)
        self.contatos = {}

    def esta_na_lista(self, nome):
        # Verifica se um nome está na lista de contatos
        return nome in self.contatos
    
    def poe_na_lista(self, nome, endereco):
        # Adiciona um contato à lista
        self.contatos[nome] = endereco

    def tira_da_lista(self, nome):
        # Remove um contato da lista, se existir
        if nome in self.contatos:
            del self.contatos[nome]
        else:
            print(f"{nome} não está na lista.")  # Exibe mensagem de erro se o nome não estiver na lista

    def pega_o_endereco(self, nome):
        # Obtém o endereço de um contato, se existir
        endereco = self.contatos.get(nome, 'Contato não encontrado')
        if endereco == 'Contato não encontrado':
            print(f"{nome} não está na lista.")  # Exibe mensagem de erro se o nome não estiver na lista
        return endereco
    
def main():
    agenda = Agenda()

    while True:
        print("\nEscolha uma opção:")
        print("1 - Está na lista")
        print("2 - Adicionar à lista")
        print("3 - Remover da lista")
        print("4 - Pegar endereço")
        print("5 - Sair")

        escolha = input("Digite o número da opção que deseja realizar: ")

        if escolha == "1":
            nome = input("Digite o nome para verificar se está na lista: ")
            if agenda.esta_na_lista(nome):
                print(f"{nome} está na lista.")
            else:
                print(f"{nome} não está na lista.")

        elif escolha == "2":
            nome = input("Digite o nome para adicionar à lista: ")
            endereco = input("Digite o endereço: ")
            agenda.poe_na_lista(nome, endereco)
            print(f"{nome} foi adicionado à lista.")

        elif escolha == "3":
            nome = input("Digite o nome para remover da lista: ")
            agenda.tira_da_lista(nome)

        elif escolha == "4":
            nome = input("Digite o nome para pegar o endereço: ")
            endereco = agenda.pega_o_endereco(nome)
            if endereco != 'Contato não encontrado':
                print(f"Endereço de {nome}: {endereco}")

        elif escolha == "5":
            print("Saindo da agenda.")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
