import pytest

from src.lesson_9 import task_1
from tests.tests_lesson_9.cases import task_1_cases as cases


@pytest.mark.parametrize("case", cases)
def test_get_unique_numbers_count(case):
    assert task_1.get_unique_numbers_count(case["numbers"]) == case["result"]
