def normalize_spaces(text: str) -> str:
    result = []
    previous_char = ""

    for char in text:
        if char == " " and previous_char == " ":
            continue

        result.append(char)
        previous_char = char

    return "".join(result)


def main():
    text = input("Введите строку: ")
    print(normalize_spaces(text))


if __name__ == "__main__":
    main()
