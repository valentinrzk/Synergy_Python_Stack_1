from math import isqrt


def count_divisors(number: int) -> int:
    divisors_count = 0

    for divisor in range(1, isqrt(number) + 1):
        if number % divisor == 0:
            divisors_count += 1

            if divisor != number // divisor:
                divisors_count += 1

    return divisors_count
    # Т.к. речь тут идет о входных данных до двух лярдов,
    # вместо простого перебора имеет смысл пробежаться от единицы до корня числа + 1.
    # Раз надо количество делителей, то если нашли один делитель,
    # то сразу нашли и парный к нему. И так до корня.
    # Чтобы корень не задвоился, проверяем его на равенство.


def main():
    number = int(input("Введите натуральное число: "))
    print(count_divisors(number))


if __name__ == "__main__":
    main()
