def get_age_word(age: int) -> str:
    """Принимает число возраста и возращает соответствующее склонение слова год."""
    if age % 10 == 1 and age % 100 != 11:
        return "год"

    if age % 10 in (2, 3, 4) and age % 100 not in (12, 13, 14):
        return "года"

    return "лет"


def main():
    pet_type = input("Введите вид питомца: ")
    pet_age = input("Введите возраст питомца: ")
    pet_name = input("Введите кличку питомца: ")

    print(
        f'Это {pet_type} по кличке "{pet_name}". Возраст: {pet_age} {get_age_word(int(pet_age))}.'
    )


if __name__ == "__main__":
    main()
