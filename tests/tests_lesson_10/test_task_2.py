import pytest

from src.lesson_10 import task_2
from tests.tests_lesson_10.cases import task_2_cases as cases


@pytest.mark.parametrize("case", cases)
def test_get_numbers_powers(case):
    assert (
        task_2.get_numbers_powers(
            case["start"],
            case["end"],
        )
        == case["result"]
    )
