import pytest

from src.lesson_16.task_1 import CashRegister


def test_top_up_adds_money() -> None:
    cash_register = CashRegister(1500)

    cash_register.top_up(700)

    assert cash_register.money == 2200


def test_count_1000_returns_full_thousands() -> None:
    cash_register = CashRegister(2750)

    assert cash_register.count_1000() == 2


def test_take_away_subtracts_money() -> None:
    cash_register = CashRegister(3000)

    cash_register.take_away(1200)

    assert cash_register.money == 1800


def test_take_away_raises_error_when_money_is_not_enough() -> None:
    cash_register = CashRegister(500)

    with pytest.raises(ValueError, match="Недостаточно денег"):
        cash_register.take_away(700)
