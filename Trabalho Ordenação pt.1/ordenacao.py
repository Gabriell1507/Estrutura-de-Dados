import random
import time

# Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

# Selection Sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# Função para gerar vetores de entrada
def generate_input_array(size, order):
    if order == 'crescente':
        return list(range(1, size + 1))
    elif order == 'decrescente':
        return list(range(size, 0, -1))
    elif order == 'aleatorio':
        return random.sample(range(1, size + 1), size)
    else:
        raise ValueError("Tipo de entrada inválido")

# Função para executar os testes
def run_tests(algorithm, order, sizes):
    for size in sizes:
        total_time = 0
        for _ in range(3):
            arr = generate_input_array(size, order)
            start_time = time.time()
            algorithm(arr)
            end_time = time.time()
            total_time += end_time - start_time
        average_time = total_time / 3
        print(f"Tamanho: {size}, Tipo de Entrada: {order}, Tempo Médio: {average_time:.6f} segundos")

# Tamanhos e tipos de entrada
sizes = [1000, 5000, 10000, 20000, 30000]
input_types = ['crescente', 'decrescente', 'aleatorio']

# Executar testes para os algoritmos
for input_type in input_types:
    print(f"Tipo de Entrada: {input_type}")
    print("Bubble Sort:")
    run_tests(bubble_sort, input_type, sizes)
    print("Insertion Sort:")
    run_tests(insertion_sort, input_type, sizes)
    print("Selection Sort:")
    run_tests(selection_sort, input_type, sizes)
    print("\n")

# Dicionário para armazenar os tempos médios dos algoritmos
average_times = {
    'Bubble Sort': [],
    'Insertion Sort': [],
    'Selection Sort': []
}

# Executar testes para os algoritmos
for input_type in input_types:
    print(f"Tipo de Entrada: {input_type}")
    bubble_sort_times = []
    insertion_sort_times = []
    selection_sort_times = []
    
    for size in sizes:
        total_time_bubble = 0
        total_time_insertion = 0
        total_time_selection = 0
        
        for _ in range(3):
            arr = generate_input_array(size, input_type)
            
            # Bubble Sort
            arr_copy = arr.copy()
            start_time = time.time()
            bubble_sort(arr_copy)
            end_time = time.time()
            total_time_bubble += end_time - start_time
            
            # Insertion Sort
            arr_copy = arr.copy()
            start_time = time.time()
            insertion_sort(arr_copy)
            end_time = time.time()
            total_time_insertion += end_time - start_time
            
            # Selection Sort
            arr_copy = arr.copy()
            start_time = time.time()
            selection_sort(arr_copy)
            end_time = time.time()
            total_time_selection += end_time - start_time
        
        # Calcular os tempos médios para cada algoritmo
        average_time_bubble = total_time_bubble / 3
        average_time_insertion = total_time_insertion / 3
        average_time_selection = total_time_selection / 3
        
        bubble_sort_times.append(average_time_bubble)
        insertion_sort_times.append(average_time_insertion)
        selection_sort_times.append(average_time_selection)
    
    # Armazenar os tempos médios no dicionário
    average_times['Bubble Sort'].append(bubble_sort_times)
    average_times['Insertion Sort'].append(insertion_sort_times)
    average_times['Selection Sort'].append(selection_sort_times)

# Calcular a média dos tempos para cada algoritmo
for algo in average_times:
    avg_times = [sum(times) / len(times) for times in average_times[algo]]
    print(f"Média de Tempo para {algo}:")
    for size, avg_time in zip(sizes, avg_times):
        print(f"Tamanho: {size}, Tempo Médio: {avg_time:.6f} segundos")
    print("\n")
