import pytest

from src.lesson_4 import task_1
from .cases import task_1_cases as cases


@pytest.mark.parametrize("case", cases)
def test_rectangle(case, monkeypatch, capsys):
    answers = iter(
        [
            case["side_1"],
            case["side_2"],
        ]
    )

    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    task_1.main()

    captured = capsys.readouterr()

    assert captured.out == case["result"]