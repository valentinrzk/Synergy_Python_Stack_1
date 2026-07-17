def get_factorial(number: int) -> int:
    factorial = 1

    for current_number in range(2, number + 1):
        factorial *= current_number

    return factorial


def get_factorial_sequence(number: int) -> list[int]:
    factorial = get_factorial(number)

    factorials = []

    for current_number in range(factorial, 0, -1):
        factorials.append(get_factorial(current_number))

    return factorials


def main():
    number = int(input("Введите натуральное число: "))

    print(get_factorial_sequence(number))


if __name__ == "__main__":
    main()
