from src.lesson_13.task_1 import generate_matrix


def test_generate_matrix() -> None:
    rows = 3
    cols = 4

    matrix = generate_matrix(rows, cols)

    assert len(matrix) == rows

    for row in matrix:
        assert len(row) == cols

        for value in row:
            assert -50 <= value <= 50
