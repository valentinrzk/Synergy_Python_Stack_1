from src.lesson_13.task_1 import print_matrix


def test_print_matrix(capsys) -> None:
    matrix = [
        [1, 2],
        [3, 4],
    ]

    print_matrix(matrix, "Матрица")

    captured = capsys.readouterr()

    assert "Матрица" in captured.out
    assert "1" in captured.out
    assert "2" in captured.out
    assert "3" in captured.out
    assert "4" in captured.out
