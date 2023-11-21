import numpy as np

number = np.random.randint(0, 101, 20)
square = np.square(number)
cube = np.power(number, 3)

print(np.column_stack((number, square, cube)))
