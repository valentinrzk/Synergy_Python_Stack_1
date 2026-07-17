import builtins

from src.lesson_11.task_2.cli import PetRegistryCLI


def test_read_invalid_id_then_success(
    cli_with_pets: PetRegistryCLI,
    monkeypatch,
    capsys,
) -> None:
    inputs = iter(["abc", "2"])

    monkeypatch.setattr(
        builtins,
        "input",
        lambda _: next(inputs),
    )

    cli_with_pets._read()

    captured = capsys.readouterr()

    assert captured.out.startswith("ID должен быть целым числом.\n")
    assert captured.out.endswith(
        "Это Собака по кличке Шарик. Возраст питомца: 5 лет. Имя владельца: Петр.\n"
    )
