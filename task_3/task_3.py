def find_min_max():
    with open('z3.1-1.txt', 'r') as file:
        numbers = list(map(int, file.read().split()))

    min_num = min(numbers)
    max_num = max(numbers)

    with open('srez.txt', 'w') as file:
        file.write(f"Минимальное число: {min_num}\n")
        file.write(f"Максимальное число: {max_num}\n")


find_min_max()