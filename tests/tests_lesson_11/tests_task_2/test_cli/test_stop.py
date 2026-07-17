import builtins

from src.lesson_11.task_2.cli import PetRegistryCLI


def test_run_stop(cli: PetRegistryCLI, monkeypatch, capsys) -> None:
    inputs = iter(["stop"])

    monkeypatch.setattr(
        builtins,
        "input",
        lambda _: next(inputs),
    )

    cli.run()

    captured = capsys.readouterr()

    assert captured.out == ("Введите команду (help - список команд).\nРабота завершена.\n")
