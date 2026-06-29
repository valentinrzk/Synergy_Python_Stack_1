def analyze_word(word: str) -> str:
    """Анализирует слово на количество согласных и на количество определенных гласных"""
    vowels = {
        "a": 0,
        "e": 0,
        "i": 0,
        "o": 0,
        "u": 0,
    }
    consonants = 0

    for char in word.lower():
        if char in vowels:
            vowels[char] += 1
        else:
            # Условие задачи гарантирует, что дано слово из маленьких латинских букв,
            # поэтому я считаю согласным любой символ, не являющийся гласным.
            consonants += 1

    result: list[str] = [
        f"Количество согласных: {consonants}",
        f"Количество гласных: {len(word) - consonants}",
    ]

    for letter, count in vowels.items():
        result.append(f"{letter}: {count if count else False}")

    return "\n".join(result)


def main():
    word = input("Введите слово: ")
    print(analyze_word(word))


if __name__ == "__main__":
    main()
