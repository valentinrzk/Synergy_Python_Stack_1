from src.lesson_13.task_1 import add_matrices


def test_add_matrices() -> None:
    matrix_1 = [
        [1, 2],
        [3, 4],
    ]

    matrix_2 = [
        [5, 6],
        [7, 8],
    ]

    expected = [
        [6, 8],
        [10, 12],
    ]

    assert add_matrices(matrix_1, matrix_2) == expected
