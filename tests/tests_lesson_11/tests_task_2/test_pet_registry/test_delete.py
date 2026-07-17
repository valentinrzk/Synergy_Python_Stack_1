import pytest

from src.lesson_11.task_2.pet_registry import PetRegistry


def test_delete_existing_pet(registry_with_pets: PetRegistry) -> None:
    registry_with_pets.delete(2)

    assert registry_with_pets.read_all() == {
        1: {
            "Кличка питомца": "Барсик",
            "Вид питомца": "Кот",
            "Возраст питомца": 3,
            "Имя владельца": "Иван",
        },
        3: {
            "Кличка питомца": "Мурка",
            "Вид питомца": "Кот",
            "Возраст питомца": 3,
            "Имя владельца": "Анна",
        },
    }

    with pytest.raises(
        ValueError,
        match=r"Питомец с id=2 не найден\.",
    ):
        registry_with_pets.read(2)


def test_delete_unknown_pet_raises(registry: PetRegistry) -> None:
    with pytest.raises(
        ValueError,
        match=r"Питомец с id=1 не найден\.",
    ):
        registry.delete(1)
