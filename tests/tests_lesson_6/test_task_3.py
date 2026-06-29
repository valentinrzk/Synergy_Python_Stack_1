import pytest

from src.lesson_6 import task_3
from tests.tests_lesson_6.cases import task_3_cases as cases


@pytest.mark.parametrize("case", cases)
def test_get_even_numbers(case):
    assert task_3.get_even_numbers(case["start"], case["end"]) == case["result"]
