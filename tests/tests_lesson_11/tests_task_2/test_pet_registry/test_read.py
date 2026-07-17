import pytest

from src.lesson_11.task_2.pet_registry import PetRegistry


def test_read_existing_pet(registry_with_pets: PetRegistry) -> None:
    assert registry_with_pets.read(2) == {
        "Кличка питомца": "Шарик",
        "Вид питомца": "Собака",
        "Возраст питомца": 5,
        "Имя владельца": "Петр",
    }


def test_read_unknown_pet_raises(registry: PetRegistry) -> None:
    with pytest.raises(
        ValueError,
        match=r"Питомец с id=1 не найден\.",
    ):
        registry.read(1)
