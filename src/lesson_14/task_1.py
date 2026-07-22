MY_LIST = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]


def print_list_recursively(items: list[int], index: int = 0) -> None:
    """Рекурсивно выводит элементы списка и сообщение о завершении."""
    if index == len(items):
        print("Конец списка")
        return

    print(items[index])
    print_list_recursively(items, index + 1)


def main() -> None:
    print_list_recursively(MY_LIST)


if __name__ == "__main__":
    main()
