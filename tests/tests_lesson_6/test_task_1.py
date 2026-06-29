import pytest

from src.lesson_6 import task_1
from tests.tests_lesson_6.cases import task_1_cases as cases


@pytest.mark.parametrize("case", cases)
def test_count_zeros(case):
    assert task_1.count_zeros(case["numbers"]) == case["result"]
