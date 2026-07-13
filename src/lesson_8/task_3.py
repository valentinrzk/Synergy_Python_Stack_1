def get_boats_count(max_weight: int, weights: list[int]) -> int:
    weights = sorted(weights)

    left = 0
    right = len(weights) - 1
    boats_count = 0

    while left <= right:
        if left == right:
            boats_count += 1
            break

        if weights[left] + weights[right] <= max_weight:
            left += 1

        right -= 1
        boats_count += 1

    return boats_count


def main():
    max_weight = int(input("Введите максимальную грузоподъемность лодки: "))
    fishermen_count = int(input("Введите количество рыбаков: "))

    weights = []

    for _ in range(fishermen_count):
        weights.append(int(input("Введите вес рыбака: ")))

    print(get_boats_count(max_weight, weights))


if __name__ == "__main__":
    main()
