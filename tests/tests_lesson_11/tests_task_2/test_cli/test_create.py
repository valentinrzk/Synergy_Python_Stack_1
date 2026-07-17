import builtins

from src.lesson_11.task_2.cli import PetRegistryCLI


def test_create(cli: PetRegistryCLI, monkeypatch, capsys) -> None:
    inputs = iter(
        [
            "Барсик",
            "Кот",
            "3",
            "Иван",
        ]
    )

    monkeypatch.setattr(
        builtins,
        "input",
        lambda _: next(inputs),
    )

    cli._create()

    captured = capsys.readouterr()

    assert "Питомец успешно создан:" in captured.out
    assert "Это Кот по кличке Барсик." in captured.out
    assert "Возраст питомца: 3 года." in captured.out
    assert "Имя владельца: Иван." in captured.out
