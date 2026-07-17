from .cli import PetRegistryCLI
from .pet_registry import PetRegistry


def main() -> None:
    """Важно. Чтобы импорты сработали корректно, запускать python -m src.lesson_11.task_2.main"""
    registry = PetRegistry()
    cli = PetRegistryCLI(registry)
    cli.run()


if __name__ == "__main__":
    main()
