import pytest

from src.lesson_7 import task_1

from .cases import task_1_cases as cases


@pytest.mark.parametrize("case", cases)
def test_is_palindrome(case):
    assert task_1.is_palindrome(case["text"]) == case["result"]
