def validate_sides(side_1: str, side_2: str) -> tuple[bool, float, float]:
    try:
        side_1 = float(side_1)
        side_2 = float(side_2)
    except ValueError:
        return False, 0, 0

    if side_1 <= 0 or side_2 <= 0:
        return False, 0, 0

    return True, side_1, side_2


def main():
    side_1 = input("Введите длину первой стороны прямоугольника: ")
    side_2 = input("Введите длину второй стороны прямоугольника: ")

    is_valid, side_1, side_2 = validate_sides(side_1, side_2)

    if not is_valid:
        print("Ошибка: стороны должны быть положительными числами.")
        return

    area = side_1 * side_2
    perimeter = 2 * (side_1 + side_2)

    print(f"Площадь: {area}\nПериметр: {perimeter}")


if __name__ == "__main__":
    main()