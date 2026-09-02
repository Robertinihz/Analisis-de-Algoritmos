import time
import random
import matplotlib.pyplot as plt

#Algoritmos
def bubble_sort_brute_force(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

#Almacenar tiempos
tamanos = [100, 200, 400, 600, 800, 1000]
tiempos_bubble = []
tiempos_selection = []

for size in tamanos:
    # Generar lista aleatoria
    lista_original = [random.randint(0, 10000) for _ in range(size)]
    
    # Medir Bubble Sort
    copia_bubble = lista_original.copy()
    inicio = time.perf_counter()
    bubble_sort_brute_force(copia_bubble)
    fin = time.perf_counter()
    tiempos_bubble.append(fin - inicio)
    
    # Medir Selection Sort
    copia_selection = lista_original.copy()
    inicio = time.perf_counter()
    selection_sort(copia_selection)
    fin = time.perf_counter()
    tiempos_selection.append(fin - inicio)

#Grafica
plt.figure(figsize=(8, 5))
plt.plot(tamanos, tiempos_bubble, marker='o', label='Bubble Sort (Brute Force)')
plt.plot(tamanos, tiempos_selection, marker='s', label='Selection Sort')

plt.title('Comparativa de Tiempo: Bubble Sort vs Selection Sort')
plt.xlabel('Tamaño de la lista (N)')
plt.ylabel('Tiempo de ejecución (segundos)')
plt.legend()
plt.grid(True)
plt.show()