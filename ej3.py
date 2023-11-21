import numpy as np

random_numbers = np.random.randint(0, 101, 20)
even_numbers = random_numbers[random_numbers % 2 == 0]
odd_numbers = random_numbers[random_numbers % 2 != 0]

result = np.empty_like(random_numbers)
result[:len(even_numbers)] = even_numbers
result[len(even_numbers):] = odd_numbers

print(result)
