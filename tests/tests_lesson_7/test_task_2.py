import pytest

from src.lesson_7 import task_2
from .cases import task_2_cases as cases


@pytest.mark.parametrize("case", cases)
def test_normalize_spaces(case):
    assert task_2.normalize_spaces(case["text"]) == case["result"]