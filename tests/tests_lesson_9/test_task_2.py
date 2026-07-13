import pytest

from src.lesson_9 import task_2
from tests.tests_lesson_9.cases import task_2_cases as cases


@pytest.mark.parametrize("case", cases)
def test_get_common_numbers_count(case):
    assert (
        task_2.get_common_numbers_count(
            case["first_numbers"],
            case["second_numbers"],
        )
        == case["result"]
    )
