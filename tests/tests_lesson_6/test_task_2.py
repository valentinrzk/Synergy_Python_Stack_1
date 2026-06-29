import pytest

from src.lesson_6 import task_2
from tests.tests_lesson_6.cases import task_2_cases as cases


@pytest.mark.parametrize("case", cases)
def test_count_divisors(case):
    assert task_2.count_divisors(case["number"]) == case["result"]
