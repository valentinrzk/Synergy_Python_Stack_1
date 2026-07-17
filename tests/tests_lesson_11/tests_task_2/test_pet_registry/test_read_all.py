from src.lesson_11.task_2.pet_registry import PetRegistry


def test_read_all_returns_all_pets(registry_with_pets: PetRegistry) -> None:
    assert registry_with_pets.read_all() == {
        1: {
            "Кличка питомца": "Барсик",
            "Вид питомца": "Кот",
            "Возраст питомца": 3,
            "Имя владельца": "Иван",
        },
        2: {
            "Кличка питомца": "Шарик",
            "Вид питомца": "Собака",
            "Возраст питомца": 5,
            "Имя владельца": "Петр",
        },
        3: {
            "Кличка питомца": "Мурка",
            "Вид питомца": "Кот",
            "Возраст питомца": 3,
            "Имя владельца": "Анна",
        },
    }


def test_read_all_filter_by_pet_type(registry_with_pets: PetRegistry) -> None:
    assert registry_with_pets.read_all(pet_type="Кот") == {
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


def test_read_all_filter_by_age(registry_with_pets: PetRegistry) -> None:
    assert registry_with_pets.read_all(age=5) == {
        2: {
            "Кличка питомца": "Шарик",
            "Вид питомца": "Собака",
            "Возраст питомца": 5,
            "Имя владельца": "Петр",
        },
    }


def test_read_all_filter_by_owner_name(registry_with_pets: PetRegistry) -> None:
    assert registry_with_pets.read_all(owner_name="Анна") == {
        3: {
            "Кличка питомца": "Мурка",
            "Вид питомца": "Кот",
            "Возраст питомца": 3,
            "Имя владельца": "Анна",
        },
    }


def test_read_all_filter_by_multiple_fields(registry_with_pets: PetRegistry) -> None:
    assert registry_with_pets.read_all(
        pet_type="Кот",
        age=3,
    ) == {
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


def test_read_all_returns_empty_when_no_matches(
    registry_with_pets: PetRegistry,
) -> None:
    assert (
        registry_with_pets.read_all(
            pet_type="Попугай",
        )
        == {}
    )
