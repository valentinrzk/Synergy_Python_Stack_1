def count_zeros(numbers: list[int]) -> int:
    zeros_count = 0

    for number in numbers:
        if number == 0:
            zeros_count += 1

    return zeros_count


def main():
    numbers_count = int(input("Введите количество чисел: "))

    numbers = []

    for _ in range(numbers_count):
        numbers.append(int(input("Введите число: ")))

    print(count_zeros(numbers))


if __name__ == "__main__":
    main()
