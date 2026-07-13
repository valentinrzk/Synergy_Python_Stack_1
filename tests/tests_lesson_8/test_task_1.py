import pytest

from src.lesson_8 import task_1

from .cases import task_1_cases as cases


@pytest.mark.parametrize("case", cases)
def test_reverse_numbers(case):
    assert task_1.reverse_numbers(case["numbers"]) == case["result"]
