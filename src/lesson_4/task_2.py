def validate_number(input_value: str) -> dict[str, int]:
    try:
        number = abs(int(input_value))
    except ValueError as error:
        raise ValueError("Ошибка: необходимо ввести целое число.") from error

    if number < 10000 or number > 99999:
        raise ValueError("Ошибка: необходимо ввести пятизначное число.")

    digits = {
        "ten_thousands": number // 10000,
        "thousands": number // 1000 % 10,
        "hundreds": number // 100 % 10,
        "tens": number // 10 % 10,
        "ones": number % 10,
    }

    if digits["ten_thousands"] == digits["thousands"]:
        raise ValueError("Ошибка: количество десятков тысяч не должно быть равно количеству тысяч.")

    return digits


def main():
    number = input("Введите пятизначное число: ")

    try:
        digits = validate_number(number)

        result = (
            digits["tens"] ** digits["ones"]
            * digits["hundreds"]
            / (digits["ten_thousands"] - digits["thousands"])
        )

        print(result)

    except ValueError as error:
        print(error)


if __name__ == "__main__":
    main()
