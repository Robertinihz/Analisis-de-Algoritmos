import time
import random
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# --- Algoritmos ---
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

# --- Función que se ejecuta al presionar el botón ---
def ejecutar_comparativa():
    try:
        inicio = int(entry_inicio.get())
        paso = int(entry_paso.get())
        final = int(entry_final.get())
        
        if inicio <= 0 or paso <= 0 or final < inicio:
            messagebox.showerror("Error", "Ingresa números válidos (Inicio > 0, Paso > 0, Final >= Inicio).")
            return

        # Genera el rango de tamaños (ej. 20, 40, 60... hasta 1000)
        tamanos = list(range(inicio, final + 1, paso))

        tiempos_bubble = []
        tiempos_selection = []

        # --- Experimento ---
        for size in tamanos:
            lista_original = [random.randint(0, 10000) for _ in range(size)]
            
            # Medir Bubble Sort
            copia_b = lista_original.copy()
            t0 = time.perf_counter()
            bubble_sort_brute_force(copia_b)
            tiempos_bubble.append(time.perf_counter() - t0)
            
            # Medir Selection Sort
            copia_s = lista_original.copy()
            t0 = time.perf_counter()
            selection_sort(copia_s)
            tiempos_selection.append(time.perf_counter() - t0)

        # --- Gráfica ---
        plt.figure(figsize=(8, 5))
        plt.plot(tamanos, tiempos_bubble, label='Bubble Sort')
        plt.plot(tamanos, tiempos_selection, label='Selection Sort')

        plt.title(f'Comparativa de Tiempo ({inicio} a {final} elementos)')
        plt.xlabel('Cantidad de elementos (N)')
        plt.ylabel('Tiempo (segundos)')
        plt.legend()
        plt.grid(True)
        plt.show()

    except ValueError:
        messagebox.showerror("Error", "Por favor ingresa únicamente números enteros.")

# --- Interfaz Gráfica con Tkinter ---
root = tk.Tk()
root.title("Configuración de Algoritmos")
root.geometry("300x230")
root.resizable(False, False)

# Campo: Valor Inicial
tk.Label(root, text="Valor inicial:").pack(pady=(10, 0))
entry_inicio = tk.Entry(root, justify="center")
entry_inicio.insert(0, "20")
entry_inicio.pack()

# Campo: Paso / Incremento
tk.Label(root, text="Paso / Incremento:").pack(pady=(5, 0))
entry_paso = tk.Entry(root, justify="center")
entry_paso.insert(0, "20")
entry_paso.pack()

# Campo: Valor Final
tk.Label(root, text="Valor final:").pack(pady=(5, 0))
entry_final = tk.Entry(root, justify="center")
entry_final.insert(0, "1000")
entry_final.pack()

# Botón para ejecutar
btn_ejecutar = tk.Button(
    root, 
    text="Graficar Comparativa", 
    command=ejecutar_comparativa, 
    bg="#1785DF", 
    fg="white", 
    font=("Arial", 10, "bold")
)
btn_ejecutar.pack(pady=15)

root.mainloop()