import pytest

from src.lesson_3 import task_2
from .cases import task_2_cases


@pytest.mark.parametrize("case", task_2_cases)
def test_task_2(case, monkeypatch, capsys):
    answers = iter(
        [
            case["stage_1"],
            case["stage_2"],
            case["stage_3"],
            case["stage_4"],
            case["stage_5"],
        ]
    )

    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    task_2.main()

    captured = capsys.readouterr()

    assert captured.out == case["result"]
