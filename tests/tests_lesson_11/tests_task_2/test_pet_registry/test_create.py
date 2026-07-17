from src.lesson_11.task_2.pet_registry import PetRegistry


def test_create_returns_created_pet(registry: PetRegistry) -> None:
    pet = registry.create(
        name="Барсик",
        pet_type="Кот",
        age=3,
        owner_name="Иван",
    )

    assert pet == {
        1: {
            "Кличка питомца": "Барсик",
            "Вид питомца": "Кот",
            "Возраст питомца": 3,
            "Имя владельца": "Иван",
        }
    }


def test_create_saves_pet(registry: PetRegistry) -> None:
    registry.create(
        name="Барсик",
        pet_type="Кот",
        age=3,
        owner_name="Иван",
    )

    assert registry.read(1) == {
        "Кличка питомца": "Барсик",
        "Вид питомца": "Кот",
        "Возраст питомца": 3,
        "Имя владельца": "Иван",
    }


def test_create_increments_id(registry: PetRegistry) -> None:
    first_pet = registry.create(
        name="Барсик",
        pet_type="Кот",
        age=3,
        owner_name="Иван",
    )

    second_pet = registry.create(
        name="Шарик",
        pet_type="Собака",
        age=5,
        owner_name="Петр",
    )

    assert first_pet == {
        1: {
            "Кличка питомца": "Барсик",
            "Вид питомца": "Кот",
            "Возраст питомца": 3,
            "Имя владельца": "Иван",
        }
    }

    assert second_pet == {
        2: {
            "Кличка питомца": "Шарик",
            "Вид питомца": "Собака",
            "Возраст питомца": 5,
            "Имя владельца": "Петр",
        }
    }
