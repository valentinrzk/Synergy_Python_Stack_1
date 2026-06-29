import pytest

from src.lesson_5 import task_2 as task
from tests.tests_lesson_5.cases import task_2_cases as cases


@pytest.mark.parametrize("case", cases)
def test_analyze_word(case):
    assert task.analyze_word(case["word"]) == case["result"]
