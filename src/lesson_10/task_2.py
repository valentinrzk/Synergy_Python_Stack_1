def get_numbers_powers(start: int, end: int) -> dict[int, float]:
    result = {}

    step = 1 if start <= end else -1

    for number in range(start, end + step, step):
        result[number] = number**number

    return result


def main():
    start = int(input("Введите начало диапазона: "))
    end = int(input("Введите конец диапазона: "))

    print(get_numbers_powers(start, end))


if __name__ == "__main__":
    main()
