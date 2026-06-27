import pytest

from src.lesson_4 import task_2
from .cases import task_2_cases as cases


@pytest.mark.parametrize("case", cases)
def test_task_2(case, monkeypatch, capsys):
    monkeypatch.setattr("builtins.input", lambda _: case["number"])

    task_2.main()

    captured = capsys.readouterr()

    assert captured.out == case["result"]