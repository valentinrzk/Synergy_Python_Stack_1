import pytest

from src.lesson_8 import task_3
from tests.tests_lesson_8.cases import task_3_cases as cases


@pytest.mark.parametrize("case", cases)
def test_get_boats_count(case):
    assert (
        task_3.get_boats_count(
            case["max_weight"],
            case["weights"],
        )
        == case["result"]
    )
