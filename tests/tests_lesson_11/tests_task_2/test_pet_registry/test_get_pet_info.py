from src.lesson_11.task_2.pet_registry import PetRegistry


def test_get_pet_info() -> None:
    pet = {
        "Кличка питомца": "Шарик",
        "Вид питомца": "Собака",
        "Возраст питомца": 5,
        "Имя владельца": "Петр",
    }

    assert PetRegistry.get_pet_info(pet) == (
        "Это Собака по кличке Шарик. Возраст питомца: 5 лет. Имя владельца: Петр."
    )
