def reverse_numbers(numbers: list[int]) -> list[int]:
    reversed_numbers = []

    for index in range(len(numbers) - 1, -1, -1):
        reversed_numbers.append(numbers[index])

    return reversed_numbers


def main():
    numbers_count = int(input("Введите количество чисел: "))

    numbers = []

    for _ in range(numbers_count):
        numbers.append(int(input("Введите число: ")))

    print(*reverse_numbers(numbers))


if __name__ == "__main__":
    main()
