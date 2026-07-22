class Transport:
    def __init__(self, name: str, max_speed: int, mileage: int):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def __str__(self) -> str:
        return f"Название автомобиля: {self.name} Скорость: {self.max_speed} Пробег: {self.mileage}"


class Autobus(Transport):
    pass


def main() -> None:
    autobus = Autobus("Renaul Logan", 180, 12)
    print(autobus)


if __name__ == "__main__":
    main()
