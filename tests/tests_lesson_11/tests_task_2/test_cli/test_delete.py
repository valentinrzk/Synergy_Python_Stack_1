import builtins

import pytest

from src.lesson_11.task_2.cli import PetRegistryCLI


def test_delete(
    cli_with_pets: PetRegistryCLI,
    monkeypatch,
    capsys,
) -> None:
    monkeypatch.setattr(
        builtins,
        "input",
        lambda _: "2",
    )

    cli_with_pets._delete()

    captured = capsys.readouterr()

    assert captured.out == "Питомец с id=2 успешно удален.\n"

    with pytest.raises(
        ValueError,
        match=r"Питомец с id=2 не найден\.",
    ):
        cli_with_pets._registry.read(2)


def test_delete_invalid_id(
    cli_with_pets: PetRegistryCLI,
    monkeypatch,
    capsys,
) -> None:
    inputs = iter(
        [
            "abc",
            "2",
        ]
    )

    monkeypatch.setattr(
        builtins,
        "input",
        lambda _: next(inputs),
    )

    cli_with_pets._delete()

    captured = capsys.readouterr()

    assert captured.out == ("ID должен быть целым числом.\nПитомец с id=2 успешно удален.\n")
