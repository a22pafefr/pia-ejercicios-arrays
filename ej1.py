import random

number = [random.randint(0, 100) for _ in range(20)]
square = [num ** 2 for num in number]
cube = [num ** 3 for num in number]

print("Number   Square   Cube")
for n, s, c in zip(number, square, cube):
    print(f"{n:<9}{s:<9}{c}")
