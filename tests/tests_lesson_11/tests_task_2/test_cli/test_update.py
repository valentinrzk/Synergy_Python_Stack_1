import builtins

from src.lesson_11.task_2.cli import PetRegistryCLI


def test_update_all_fields(
    cli_with_pets: PetRegistryCLI,
    monkeypatch,
    capsys,
) -> None:
    inputs = iter(
        [
            "2",
            "Бобик",
            "Пес",
            "6",
            "Сергей",
        ]
    )

    monkeypatch.setattr(
        builtins,
        "input",
        lambda _: next(inputs),
    )

    cli_with_pets._update()

    captured = capsys.readouterr()

    assert captured.out == (
        "Информация о питомце обновлена.\n"
        "Это Пес по кличке Бобик. "
        "Возраст питомца: 6 лет. "
        "Имя владельца: Сергей.\n"
    )


def test_update_single_field(
    cli_with_pets: PetRegistryCLI,
    monkeypatch,
    capsys,
) -> None:
    inputs = iter(
        [
            "2",
            "",
            "",
            "6",
            "",
        ]
    )

    monkeypatch.setattr(
        builtins,
        "input",
        lambda _: next(inputs),
    )

    cli_with_pets._update()

    captured = capsys.readouterr()

    assert captured.out == (
        "Информация о питомце обновлена.\n"
        "Это Собака по кличке Шарик. "
        "Возраст питомца: 6 лет. "
        "Имя владельца: Петр.\n"
    )


def test_update_invalid_age(
    cli_with_pets: PetRegistryCLI,
    monkeypatch,
    capsys,
) -> None:
    inputs = iter(
        [
            "2",
            "",
            "",
            "abc",
        ]
    )

    monkeypatch.setattr(
        builtins,
        "input",
        lambda _: next(inputs),
    )

    cli_with_pets._update()

    captured = capsys.readouterr()

    assert captured.out == "Возраст должен быть целым числом.\n"
