from .pet import Pet


class PetRegistry:
    """Хранилище данных о питомцах."""

    def __init__(self):
        self._pets: dict[int, Pet] = {}
        self._next_id = 1

    def create(
        self,
        name: str,
        pet_type: str,
        age: int,
        owner_name: str,
    ) -> dict[int, dict[str, str | int]]:
        """Создать нового питомца."""
        pet = Pet(name=name, pet_type=pet_type, age=age, owner_name=owner_name)
        pet_id = self._next_id
        self._pets[pet_id] = pet
        self._next_id += 1

        return {pet_id: pet.to_dict()}

    def read(
        self,
        pet_id: int,
    ) -> dict[str, str | int]:
        """Получить информацию о питомце по его id."""
        pet = self._pets.get(pet_id)

        if pet is None:
            raise ValueError(f"Питомец с id={pet_id} не найден.")

        return pet.to_dict()

    def read_all(
        self,
        pet_type: str | None = None,
        age: int | None = None,
        owner_name: str | None = None,
    ) -> dict[int, dict[str, str | int]]:
        """Получить информацию обо всех питомцах с возможностью фильтрации по виду, возрасту и имени владельца."""
        result = {}

        for pet_id, pet in self._pets.items():
            if pet_type is not None and pet.pet_type != pet_type:
                continue

            if age is not None and pet.age != age:
                continue

            if owner_name is not None and pet.owner_name != owner_name:
                continue

            result[pet_id] = pet.to_dict()

        return result

    def update(
        self,
        pet_id: int,
        *,
        name: str | None = None,
        pet_type: str | None = None,
        age: int | None = None,
        owner_name: str | None = None,
    ) -> None:
        """Редактировать информацию о питомце"""
        pet = self._pets.get(pet_id)

        if pet is None:
            raise ValueError(f"Питомец с id={pet_id} не найден.")

        if name is not None:
            pet.name = name

        if pet_type is not None:
            pet.pet_type = pet_type

        if age is not None:
            pet.age = age

        if owner_name is not None:
            pet.owner_name = owner_name

    def delete(
        self,
        pet_id: int,
    ) -> None:
        """Удалить питомца"""
        if pet_id not in self._pets:
            raise ValueError(f"Питомец с id={pet_id} не найден.")

        del self._pets[pet_id]

    @staticmethod
    def get_suffix(age: int) -> str:
        """Принимает число возраста и возращает соответствующее склонение слова год."""
        if age % 10 == 1 and age % 100 != 11:
            return "год"
        if age % 10 in (2, 3, 4) and age % 100 not in (12, 13, 14):
            return "года"
        return "лет"

    @staticmethod
    def get_pet_info(pet: dict[str, str | int]) -> str:
        """
        Получить информацию о питомце в виде строки формата:
        "Это <вид питомца> по кличке "<кличка>".
        Возраст питомца: <возраст> <суффикс возраста>.
        Имя владельца: <имя владельца>."
        """
        suffix = PetRegistry.get_suffix(int(pet["Возраст питомца"]))
        return (
            f"Это {pet['Вид питомца']} по кличке {pet['Кличка питомца']}. "
            f"Возраст питомца: {pet['Возраст питомца']} {suffix}. "
            f"Имя владельца: {pet['Имя владельца']}."
        )
