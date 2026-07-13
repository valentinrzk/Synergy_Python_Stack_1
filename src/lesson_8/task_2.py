def shift_numbers(
    numbers: list[int],
    numbers_count: int | None = None,
) -> list[int]:
    if not validate_numbers_count(numbers, numbers_count):
        raise ValueError("Количество чисел не соответствует заявленному.")

    if not numbers:
        return []

    shifted_numbers = [numbers[-1]]

    for index in range(len(numbers) - 1):
        shifted_numbers.append(numbers[index])

    return shifted_numbers


def validate_numbers_count(numbers: list[int], numbers_count: int | None) -> bool:
    if numbers_count is None:
        return True

    return numbers_count == len(numbers)


def main():
    numbers_count = int(input("Введите количество чисел: "))

    numbers = [int(number) for number in input("Введите числа через пробел: ").split()]

    print(*shift_numbers(numbers, numbers_count))


if __name__ == "__main__":
    main()
