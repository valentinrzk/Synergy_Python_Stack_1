import pytest

from src.lesson_8 import task_2
from tests.tests_lesson_8.cases import task_2_negative_cases as negative_cases
from tests.tests_lesson_8.cases import task_2_positive_cases as positive_cases


@pytest.mark.parametrize("case", positive_cases)
def test_shift_numbers(case):
    assert (
        task_2.shift_numbers(
            case["numbers"],
            case["numbers_count"],
        )
        == case["result"]
    )


@pytest.mark.parametrize("case", negative_cases)
def test_shift_numbers_exception(case):
    with pytest.raises(case["exception"]):
        task_2.shift_numbers(
            case["numbers"],
            case["numbers_count"],
        )
