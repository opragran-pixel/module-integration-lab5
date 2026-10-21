
from input_module import input_matrix
from processing_output import print_result


def main():
    print("Лабораторная работа №5. Вариант 1.")
    print("Поиск столбцов, содержащих только элементы, кратные 5 или 7.\n")

    matrix1 = input_matrix("A")
    matrix2 = input_matrix("B")

    print_result(matrix1, "A")
    print_result(matrix2, "B")


if __name__ == "__main__":
    main()

