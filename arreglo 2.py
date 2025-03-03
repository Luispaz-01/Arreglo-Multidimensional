def bubble_sort(fila):
    n = len(fila)
    for i in range(n):
        for j in range(0, n-i-1):
            if fila[j] > fila[j+1]:
                # Intercambiar si el elemento encontrado es mayor que el siguiente
                fila[j], fila[j+1] = fila[j+1], fila[j]

def ordenar_fila(matriz, fila_index):
    if 0 <= fila_index < len(matriz):
        bubble_sort(matriz[fila_index])
    else:
        print("Índice de fila fuera de rango.")

# Definimos una matriz 3x3
matriz = [
    [9, 2, 5],
    [4, 8, 1],
    [7, 3, 6]
]

# Mostramos la matriz original
print("Matriz original:")
for fila in matriz:
    print(fila)

# Fila a ordenar (por ejemplo, la fila 1)
fila_a_ordenar = 1

# Llamamos a la función para ordenar la fila
ordenar_fila(matriz, fila_a_ordenar)

# Mostramos la matriz con la fila ordenada
print("\nMatriz con la fila ordenada:")
for fila in matriz:
    print(fila)