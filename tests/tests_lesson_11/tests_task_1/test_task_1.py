import pytest

from src.lesson_11 import task_1

from .cases import factorial_cases, factorial_sequence_cases


@pytest.mark.parametrize("case", factorial_sequence_cases)
def test_get_factorial_sequence(case):
    assert task_1.get_factorial_sequence(case["number"]) == case["result"]


@pytest.mark.parametrize("case", factorial_cases)
def test_get_factorial(case):
    assert task_1.get_factorial(case["number"]) == case["result"]
