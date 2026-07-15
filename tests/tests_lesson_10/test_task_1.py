import pytest

from src.lesson_10 import task_1
from tests.tests_lesson_10.cases import task_1_age_cases as age_cases
from tests.tests_lesson_10.cases import task_1_cases as cases


@pytest.mark.parametrize("case", cases)
def test_format_pet_info(case):
    assert (
        task_1.format_pet_info(
            case["pet_name"],
            case["pet"],
        )
        == case["result"]
    )


@pytest.mark.parametrize("case", age_cases)
def test_get_age_word(case):
    assert task_1.get_age_word(case["age"]) == case["result"]
