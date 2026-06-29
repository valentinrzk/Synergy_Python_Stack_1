def get_even_numbers(start: int, end: int) -> list[int]:
    if start % 2 != 0:
        start += 1

    even_numbers = []

    for number in range(start, end + 1, 2):
        even_numbers.append(number)

    return even_numbers
    # Идея в том, что вместо простого прохода с делениями сразу определить четное число и двигаться +2.


def main():
    start = int(input("Введите начало отрезка: "))
    end = int(input("Введите конец отрезка: "))

    print(get_even_numbers(start, end))


if __name__ == "__main__":
    main()
