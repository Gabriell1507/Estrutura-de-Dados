def torre_hanoi(n, origem, auxiliar, destino):
    if n == 1:
        print(f'Mova o disco 1 da torre {origem} para a torre {destino}')
        return
    torre_hanoi(n-1, origem, destino, auxiliar)
    print(f'Mova o disco {n} da torre {origem} para a torre {destino}')
    torre_hanoi(n-1, auxiliar, origem, destino)

# Solicita o número de discos ao usuário
n = int(input("Quantos discos você deseja inserir? "))

# Chama a função para resolver o problema das Torres de Hanoi
torre_hanoi(n, 'A', 'B', 'C')
