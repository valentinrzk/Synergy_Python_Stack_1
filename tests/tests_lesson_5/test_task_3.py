import pytest

from src.lesson_5 import task_3 as task
from tests.tests_lesson_5.cases import task_3_cases as cases


@pytest.mark.parametrize("case", cases)
def test_get_investment_result(case):
    assert (
        task.get_investment_result(
            case["min_amount"],
            case["mike_amount"],
            case["ivan_amount"],
        )
        == case["result"]
    )
