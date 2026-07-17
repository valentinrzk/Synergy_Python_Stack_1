import pytest

from src.lesson_11.task_2.cli import PetRegistryCLI
from src.lesson_11.task_2.pet_registry import PetRegistry


@pytest.fixture
def registry():
    registry = PetRegistry()
    return registry


@pytest.fixture
def registry_with_pets():
    registry = PetRegistry()

    registry.create("Барсик", "Кот", 3, "Иван")
    registry.create("Шарик", "Собака", 5, "Петр")
    registry.create("Мурка", "Кот", 3, "Анна")

    return registry


@pytest.fixture
def cli(registry):
    return PetRegistryCLI(registry)


@pytest.fixture
def cli_with_pets(registry_with_pets):
    return PetRegistryCLI(registry_with_pets)
