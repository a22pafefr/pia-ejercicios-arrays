numbers = []

for _ in range(5):
    num = int(input("Introduce un número: "))
    numbers.append(num)

numbers = numbers[-1:] + numbers[:-1]

print(numbers)
