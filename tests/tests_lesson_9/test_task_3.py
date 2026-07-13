import pytest

from src.lesson_9 import task_3
from tests.tests_lesson_9.cases import task_3_cases as cases


@pytest.mark.parametrize("case", cases)
def test_check_numbers(case):
    assert task_3.check_numbers(case["numbers"]) == case["result"]
