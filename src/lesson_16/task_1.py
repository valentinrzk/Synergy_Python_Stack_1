class CashRegister:
    def __init__(self, money: int = 0):
        self.money = money

    def top_up(self, amount: int) -> None:
        self.money += amount

    def count_1000(self) -> int:
        return self.money // 1000

    def take_away(self, amount: int) -> None:
        if amount > self.money:
            raise ValueError("Недостаточно денег в кассе.")

        self.money -= amount


Kassa = CashRegister
Касса = CashRegister
