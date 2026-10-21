
def is_positive_column(column):
    """Проверяет, что все элементы столбца кратны 5 или 7."""
    return all(x % 5 == 0 or x % 7 == 0 for x in column)


def find_columns(matrix):
    """Возвращает список номеров столбцов (1-based), удовлетворяющих условию."""
    if not matrix:
        return []
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        column = [matrix[i][j] for i in range(len(matrix))]
        if is_positive_column(column):
            result.append(j + 1)
    return result


def print_result(matrix, name):
    """Форматированный вывод результата для одной матрицы."""
    print(f"\n=== Матрица {name} ===")
    for row in matrix:
        print("  " + " ".join(f"{x:4d}" for x in row))

    columns = find_columns(matrix)
    if columns:
        print(f"Столбцы, содержащие только кратные 5 или 7: {columns}")
    else:
        print("Столбцов, содержащих только кратные 5 или 7, нет.")

