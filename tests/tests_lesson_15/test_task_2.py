from src.lesson_15 import task_2


def test_autobus_inherits_transport() -> None:
    assert issubclass(task_2.Autobus, task_2.Transport)


def test_autobus_seating_capacity_default_value() -> None:
    autobus = task_2.Autobus("Renaul Logan", 180, 12)

    assert autobus.seating_capacity() == "Вместимость одного автобуса Renaul Logan: 50 пассажиров"


def test_autobus_seating_capacity_custom_value() -> None:
    autobus = task_2.Autobus("Renaul Logan", 180, 12)

    assert autobus.seating_capacity(30) == "Вместимость одного автобуса Renaul Logan: 30 пассажиров"
