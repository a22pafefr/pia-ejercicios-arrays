import random

# Generar la lista de 20 números enteros entre 100 y 999
numbers = [random.randint(100, 999) for _ in range(20)]

# Crear la lista de listas con 4 filas y 5 columnas
matrix = [numbers[i * 5:(i + 1) * 5] for i in range(4)]

# Mostrar la matriz y calcular las sumas parciales de filas y columnas
for row in matrix:
    print(row, "| Suma parcial:", sum(row))

column_sums = [sum(matrix[i][j] for i in range(4)) for j in range(5)]
print("\nSumas parciales por columna:")
for i, col_sum in enumerate(column_sums):
    print(f"Columna {i + 1} Suma parcial:", col_sum)

total_sum = sum(numbers)
print("\nSuma total:", total_sum)
