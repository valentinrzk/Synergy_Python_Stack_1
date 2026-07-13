def get_common_numbers_count(
    first_numbers: list[int],
    second_numbers: list[int],
) -> int:
    return len(set(first_numbers) & set(second_numbers))


def main():
    first_numbers_count = int(input("Введите количество чисел в первом списке: "))
    first_numbers = []

    for _ in range(first_numbers_count):
        first_numbers.append(int(input("Введите число: ")))

    second_numbers_count = int(input("Введите количество чисел во втором списке: "))
    second_numbers = []

    for _ in range(second_numbers_count):
        second_numbers.append(int(input("Введите число: ")))

    print(get_common_numbers_count(first_numbers, second_numbers))


if __name__ == "__main__":
    main()
