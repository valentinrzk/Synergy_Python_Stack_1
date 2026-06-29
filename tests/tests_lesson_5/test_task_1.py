import pytest

from src.lesson_5 import task_1 as task
from tests.tests_lesson_5.cases import task_1_cases as cases


@pytest.mark.parametrize("case", cases)
def test_describe_number(case):
    assert task.describe_number(case["input_value"]) == case["result"]
