import pytest

from src.lesson_11.task_2.pet_registry import PetRegistry


@pytest.mark.parametrize(
    ("age", "expected_suffix"),
    [
        (1, "год"),
        (2, "года"),
        (3, "года"),
        (4, "года"),
        (5, "лет"),
        (11, "лет"),
        (12, "лет"),
        (13, "лет"),
        (14, "лет"),
        (21, "год"),
        (22, "года"),
        (24, "года"),
        (25, "лет"),
        (31, "год"),
        (32, "года"),
        (111, "лет"),
        (121, "год"),
        (122, "года"),
    ],
)
def test_get_suffix(age: int, expected_suffix: str) -> None:
    assert PetRegistry.get_suffix(age) == expected_suffix
