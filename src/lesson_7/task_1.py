def is_palindrome(text: str) -> str:
    normalized_text = "".join(char.lower() for char in text if char.isalpha())

    return "yes" if normalized_text == normalized_text[::-1] else "no"


def main():
    text = input("Введите строку: ")
    print(is_palindrome(text))


if __name__ == "__main__":
    main()
