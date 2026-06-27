import pytest

from src.lesson_3 import task_1

from .cases import task_1_cases


@pytest.mark.parametrize("case", task_1_cases)
def test_task_1(case, monkeypatch, capsys):
    answers = iter(
        [
            case["pet_type"],
            str(case["pet_age"]),
            case["pet_name"],
        ]
    )

    monkeypatch.setattr("builtins.input", lambda _: next(answers))

    task_1.main()

    captured = capsys.readouterr()

    assert captured.out == case["result"]
