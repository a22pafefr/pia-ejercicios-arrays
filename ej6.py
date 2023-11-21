import numpy as np

numbers = np.random.randint(100, 1000, (4, 5))
row_sums = np.sum(numbers, axis=1)
column_sums = np.sum(numbers, axis=0)

print("Matriz de números:")
print(numbers)
print("\nSumas parciales por fila:")
print(row_sums)
print("\nSumas parciales por columna:")
print(column_sums)
print("\nSuma total:", np.sum(numbers))
