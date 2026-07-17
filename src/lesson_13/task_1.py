from random import randint

MIN_VALUE = -50
MAX_VALUE = 50


def generate_matrix(rows: int, cols: int) -> list[list[int]]:
    """Создает матрицу указанного размера со случайными числами."""
    return [[randint(MIN_VALUE, MAX_VALUE) for _ in range(cols)] for _ in range(rows)]


def print_matrix(matrix: list[list[int]], title: str) -> None:
    """Красиво выводит матрицу."""
    print(title)

    for row in matrix:
        print("\t".join(f"{value:5}" for value in row))

    print()


def add_matrices(
    matrix_1: list[list[int]],
    matrix_2: list[list[int]],
) -> list[list[int]]:
    """Возвращает сумму двух матриц."""

    result = []

    for i in range(len(matrix_1)):
        row = []

        for j in range(len(matrix_1[0])):
            row.append(matrix_1[i][j] + matrix_2[i][j])

        result.append(row)

    return result


def multiply_matrices(
    matrix_1: list[list[int]],
    matrix_2: list[list[int]],
) -> list[list[int]]:
    """Возвращает произведение двух матриц."""

    result = []

    for i in range(len(matrix_1)):
        row = []

        for j in range(len(matrix_2[0])):
            value = 0

            for k in range(len(matrix_2)):
                value += matrix_1[i][k] * matrix_2[k][j]

            row.append(value)

        result.append(row)

    return result


def main() -> None:
    print("Введите размеры первой матрицы")
    rows_1 = int(input("Количество строк: "))
    cols_1 = int(input("Количество столбцов: "))

    print("\nВведите размеры второй матрицы")
    rows_2 = int(input("Количество строк: "))
    cols_2 = int(input("Количество столбцов: "))

    matrix_1 = generate_matrix(rows_1, cols_1)
    matrix_2 = generate_matrix(rows_2, cols_2)

    print_matrix(matrix_1, "Матрица №1")
    print_matrix(matrix_2, "Матрица №2")

    if rows_1 == rows_2 and cols_1 == cols_2:
        matrix_sum = add_matrices(matrix_1, matrix_2)
        print_matrix(matrix_sum, "Сумма матриц")
    else:
        print("Сложение невозможно: размеры матриц должны совпадать.\n")

    if cols_1 == rows_2:
        matrix_product = multiply_matrices(matrix_1, matrix_2)
        print_matrix(matrix_product, "Произведение матриц")
    else:
        print(
            "Умножение невозможно: "
            "число столбцов первой матрицы должно быть "
            "равно числу строк второй матрицы."
        )


if __name__ == "__main__":
    main()
