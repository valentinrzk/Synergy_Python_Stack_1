import builtins

from src.lesson_11.task_2.cli import PetRegistryCLI


def test_read_all(cli_with_pets: PetRegistryCLI, monkeypatch, capsys) -> None:
    inputs = iter(
        [
            "",
            "",
            "",
        ]
    )

    monkeypatch.setattr(
        builtins,
        "input",
        lambda _: next(inputs),
    )

    cli_with_pets._read_all()

    captured = capsys.readouterr()

    assert captured.out == (
        "Это Кот по кличке Барсик. Возраст питомца: 3 года. Имя владельца: Иван.\n"
        "Это Собака по кличке Шарик. Возраст питомца: 5 лет. Имя владельца: Петр.\n"
        "Это Кот по кличке Мурка. Возраст питомца: 3 года. Имя владельца: Анна.\n"
    )


def test_read_all_with_filter(
    cli_with_pets: PetRegistryCLI,
    monkeypatch,
    capsys,
) -> None:
    inputs = iter(
        [
            "Кот",
            "",
            "",
        ]
    )

    monkeypatch.setattr(
        builtins,
        "input",
        lambda _: next(inputs),
    )

    cli_with_pets._read_all()

    captured = capsys.readouterr()

    assert captured.out == (
        "Это Кот по кличке Барсик. Возраст питомца: 3 года. Имя владельца: Иван.\n"
        "Это Кот по кличке Мурка. Возраст питомца: 3 года. Имя владельца: Анна.\n"
    )


def test_read_all_no_matches(
    cli_with_pets: PetRegistryCLI,
    monkeypatch,
    capsys,
) -> None:
    inputs = iter(
        [
            "Попугай",
            "",
            "",
        ]
    )

    monkeypatch.setattr(
        builtins,
        "input",
        lambda _: next(inputs),
    )

    cli_with_pets._read_all()

    captured = capsys.readouterr()

    assert captured.out == "Питомцы не найдены.\n"


def test_read_all_invalid_age(
    cli_with_pets: PetRegistryCLI,
    monkeypatch,
    capsys,
) -> None:
    inputs = iter(
        [
            "",
            "abc",
        ]
    )

    monkeypatch.setattr(
        builtins,
        "input",
        lambda _: next(inputs),
    )

    cli_with_pets._read_all()

    captured = capsys.readouterr()

    assert captured.out == "Возраст должен быть целым числом.\n"
