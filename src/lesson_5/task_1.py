def describe_number(input_value: str) -> str:
    try:
        number = int(input_value)
    except ValueError:
        return "не является целым числом"

    if number == 0:
        return "нулевое число"

    sign = "положительное" if number > 0 else "отрицательное"
    parity = "четное" if number % 2 == 0 else "нечетное"

    return f"{sign} {parity} число"


# Задание содержит взаимоисключающие требования.
# В начале приводится пример "положительное нечетное число",
# затем в конце требуется "число не является четным".
# Я выбрал реализацию с унифицированным сообщением, альтернативный код ниже:
#   if number % 2 != 0:
#       return "число не является четным"
#   sign = "положительное" if number > 0 else "отрицательное"
#   return f"{sign} четное число"


def main():
    number = input("Введите целое число: ")
    print(describe_number(number))


if __name__ == "__main__":
    main()
