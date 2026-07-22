from src.lesson_15 import task_1


def test_autobus_inherits_transport() -> None:
    assert issubclass(task_1.Autobus, task_1.Transport)


def test_autobus_string_representation() -> None:
    autobus = task_1.Autobus("Renaul Logan", 180, 12)

    assert str(autobus) == "Название автомобиля: Renaul Logan Скорость: 180 Пробег: 12"
