import pytest

from src.lesson_16.task_2 import Turtle


def test_turtle_moves_by_current_step() -> None:
    turtle = Turtle(x=0, y=0, step=3)

    turtle.go_up()
    turtle.go_right()
    turtle.go_down()
    turtle.go_left()

    assert (turtle.x, turtle.y) == (0, 0)


def test_evolve_increases_step() -> None:
    turtle = Turtle(step=2)

    turtle.evolve()

    assert turtle.s == 3


def test_degrade_decreases_step() -> None:
    turtle = Turtle(step=2)

    turtle.degrade()

    assert turtle.s == 1


def test_degrade_raises_error_when_step_becomes_not_positive() -> None:
    turtle = Turtle(step=1)

    with pytest.raises(ValueError, match="меньше или равен нулю"):
        turtle.degrade()


def test_count_moves_returns_minimal_number_of_moves() -> None:
    turtle = Turtle(x=1, y=1, step=3)

    assert turtle.count_moves(8, -5) == 5
