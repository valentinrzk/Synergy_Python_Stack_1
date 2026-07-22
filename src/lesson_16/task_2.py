from math import ceil


class Turtle:
    def __init__(self, x: int = 0, y: int = 0, step: int = 1):
        self.x = x
        self.y = y
        self.s = step

    def go_up(self) -> None:
        self.y += self.s

    def go_down(self) -> None:
        self.y -= self.s

    def go_left(self) -> None:
        self.x -= self.s

    def go_right(self) -> None:
        self.x += self.s

    def evolve(self) -> None:
        self.s += 1

    def degrade(self) -> None:
        if self.s <= 1:
            raise ValueError("Шаг черепашки не может стать меньше или равен нулю.")

        self.s -= 1

    def count_moves(self, x2: int, y2: int) -> int:
        x_moves = ceil(abs(x2 - self.x) / self.s)
        y_moves = ceil(abs(y2 - self.y) / self.s)

        return x_moves + y_moves


Cherepashka = Turtle
Черепашка = Turtle
