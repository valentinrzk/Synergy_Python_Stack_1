from src.lesson_11.task_2.cli import PetRegistryCLI


def test_help(cli: PetRegistryCLI, capsys) -> None:
    cli._help()

    captured = capsys.readouterr()

    assert captured.out == (
        "Доступные команды:\n  create\n  read\n  read all\n  update\n  delete\n  help\n  stop\n"
    )
