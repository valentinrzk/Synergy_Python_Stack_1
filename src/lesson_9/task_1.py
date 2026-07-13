def get_unique_numbers_count(numbers: list[int]) -> int:
    return len(set(numbers))


def main():
    numbers_count = int(input("Введите количество чисел: "))

    numbers = [int(number) for number in input("Введите числа через пробел: ").split()]

    if numbers_count != len(numbers):
        raise ValueError("Количество чисел не соответствует заявленному.")

    print(get_unique_numbers_count(numbers))


if __name__ == "__main__":
    main()
