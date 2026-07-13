def check_numbers(numbers: list[int]) -> list[str]:
    seen_numbers = set()
    result = []

    for number in numbers:
        if number in seen_numbers:
            result.append("YES")
        else:
            result.append("NO")
            seen_numbers.add(number)

    return result


def main():
    numbers = [int(number) for number in input("Введите числа через пробел: ").split()]

    print(*check_numbers(numbers), sep="\n")


if __name__ == "__main__":
    main()
