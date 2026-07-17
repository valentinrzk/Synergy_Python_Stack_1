from src.lesson_13.task_1 import multiply_matrices


def test_multiply_matrices() -> None:
    matrix_1 = [
        [1, 2],
        [3, 4],
    ]

    matrix_2 = [
        [5, 6],
        [7, 8],
    ]

    expected = [
        [19, 22],
        [43, 50],
    ]

    assert multiply_matrices(matrix_1, matrix_2) == expected
