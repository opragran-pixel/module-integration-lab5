
def input_matrix(name):
    """Ввод матрицы натуральных чисел. Возвращает список списков."""
    while True:
        try:
            rows = int(input(f"Введите количество строк матрицы {name} (1-10): "))
            cols = int(input(f"Введите количество столбцов матрицы {name} (1-10): "))
            if not (1 <= rows <= 10 and 1 <= cols <= 10):
                print("Ошибка: размеры должны быть от 1 до 10.")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число.")

    matrix = []
    for i in range(rows):
        while True:
            try:
                row = list(map(int, input(f"Строка {i + 1} ({cols} чисел): ").split()))
                if len(row) != cols:
                    print(f"Ошибка: нужно ровно {cols} чисел.")
                    continue
                if any(x <= 0 for x in row):
                    print("Ошибка: элементы должны быть натуральными (положительными).")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Ошибка: вводите целые числа через пробел.")
    return matrix

