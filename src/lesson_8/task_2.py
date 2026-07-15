def shift_numbers(numbers: list[int]) -> list[int]:
    if not numbers:
        return []

    shifted_numbers = [numbers[-1]]

    for index in range(len(numbers) - 1):
        shifted_numbers.append(numbers[index])

    return shifted_numbers


def main():
    numbers_count = int(input("Введите количество чисел: "))

    numbers = [int(number) for number in input("Введите числа через пробел: ").split()]

    if numbers_count != len(numbers):
        raise ValueError("Количество чисел не соответствует заявленному.")

    print(*shift_numbers(numbers))


if __name__ == "__main__":
    main()
