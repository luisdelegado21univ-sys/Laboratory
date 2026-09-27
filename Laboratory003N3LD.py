numbers = [35, 1, 23, 7, 99, 100, 62, 5, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 22, 23, 95]

ederly = numbers[0]
minor = numbers[0]

for number in numbers:
    if number > ederly:
        ederly = number
    if number < minor:
        minor = number

print(f"El número más grande es: {ederly}")
print(f"El número más pequeño es: {minor}")