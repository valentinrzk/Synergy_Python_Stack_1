import pytest

from src.lesson_11.task_2.pet_registry import PetRegistry


def test_update_all_fields(registry_with_pets: PetRegistry) -> None:
    registry_with_pets.update(
        pet_id=1,
        name="Рыжик",
        pet_type="Собака",
        age=7,
        owner_name="Сергей",
    )

    assert registry_with_pets.read(1) == {
        "Кличка питомца": "Рыжик",
        "Вид питомца": "Собака",
        "Возраст питомца": 7,
        "Имя владельца": "Сергей",
    }


def test_update_single_field(registry_with_pets: PetRegistry) -> None:
    registry_with_pets.update(
        pet_id=2,
        age=6,
    )

    assert registry_with_pets.read(2) == {
        "Кличка питомца": "Шарик",
        "Вид питомца": "Собака",
        "Возраст питомца": 6,
        "Имя владельца": "Петр",
    }


def test_update_unknown_pet_raises(registry: PetRegistry) -> None:
    with pytest.raises(
        ValueError,
        match=r"Питомец с id=1 не найден\.",
    ):
        registry.update(
            pet_id=1,
            name="Барсик",
        )
