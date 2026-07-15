def get_age_word(age: int) -> str:
    """Принимает возраст и возвращает корректное склонение слова 'год'."""
    if age % 10 == 1 and age % 100 != 11:
        return "год"

    if age % 10 in (2, 3, 4) and age % 100 not in (12, 13, 14):
        return "года"

    return "лет"


def format_pet_info(pet_name: str, pet: dict[str, str | int]) -> str:
    return (
        f'Это {pet["Вид питомца"]} по кличке "{pet_name}". '
        f"Возраст питомца: {pet['Возраст питомца']} {get_age_word(int(pet['Возраст питомца']))}. "
        f"Имя владельца: {pet['Имя владельца']}."
    )


def main():
    pets = {}

    pet_name = input("Введите кличку питомца: ")
    pet_type = input("Введите вид питомца: ")
    pet_age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца: ")

    pets[pet_name] = {
        "Вид питомца": pet_type,
        "Возраст питомца": pet_age,
        "Имя владельца": owner_name,
    }

    print(format_pet_info(pet_name, pets[pet_name]))


if __name__ == "__main__":
    main()
