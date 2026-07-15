import pytest

from src.lesson_8 import task_2
from tests.tests_lesson_8.cases import task_2_cases as cases


@pytest.mark.parametrize("case", cases)
def test_shift_numbers(case):
    assert (
        task_2.shift_numbers(
            case["numbers"],
        )
        == case["result"]
    )
