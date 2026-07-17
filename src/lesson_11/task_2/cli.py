from .pet_registry import PetRegistry


class PetRegistryCLI:
    """Консольный интерфейс для работы с реестром питомцев."""

    def __init__(self, registry: PetRegistry) -> None:
        self._registry = registry
        self._commands = {
            "create": self._create,
            "read": self._read,
            "read all": self._read_all,
            "update": self._update,
            "delete": self._delete,
            "help": self._help,
            "stop": self._stop,
        }
        self._running = True

    def run(self) -> None:
        """Запустить цикл обработки команд."""
        print("Введите команду (help - список команд).")

        while self._running:
            command = input("> ").strip().lower()

            handler = self._commands.get(command)

            if handler is None:
                print("Неизвестная команда. Введите help.")
                continue

            try:
                handler()
            except Exception as error:
                print(error)

    def _create(self) -> None:
        """Создать питомца."""
        name = input("Введите кличку питомца: ").strip()
        pet_type = input("Введите вид питомца: ").strip()

        while True:
            try:
                age = int(input("Введите возраст питомца: "))
                break
            except ValueError:
                print("Возраст должен быть целым числом.")

        owner_name = input("Введите имя владельца: ").strip()

        pet = self._registry.create(
            name=name,
            pet_type=pet_type,
            age=age,
            owner_name=owner_name,
        )
        pet_id = next(iter(pet))

        print("Питомец успешно создан:")
        print(self._registry.get_pet_info(pet[pet_id]))

    def _read(self) -> None:
        """Получить информацию о питомце."""
        while True:
            try:
                pet_id = int(input("Введите id питомца: "))
                break
            except ValueError:
                print("ID должен быть целым числом.")

        pet = self._registry.read(pet_id)
        print(self._registry.get_pet_info(pet))

    def _read_all(self) -> None:
        """Получить информацию обо всех питомцах."""

        pet_type = input("Введите вид питомца (Enter - без фильтра): ").strip() or None

        age_input = input("Введите возраст (Enter - без фильтра): ").strip()

        if age_input == "":
            age = None
        else:
            try:
                age = int(age_input)
            except ValueError:
                print("Возраст должен быть целым числом.")
                return

        owner_name = input("Введите имя владельца (Enter - без фильтра): ").strip() or None

        pets = self._registry.read_all(
            pet_type=pet_type,
            age=age,
            owner_name=owner_name,
        )

        if not pets:
            print("Питомцы не найдены.")
            return

        for pet in pets.values():
            print(self._registry.get_pet_info(pet))

    def _update(self) -> None:
        """Обновить информацию о питомце."""

        while True:
            try:
                pet_id = int(input("Введите id питомца: "))
                break
            except ValueError:
                print("ID должен быть целым числом.")

        name = input("Введите новую кличку (Enter - оставить без изменений): ").strip() or None

        pet_type = (
            input("Введите новый вид питомца (Enter - оставить без изменений): ").strip() or None
        )

        age_input = input("Введите новый возраст (Enter - оставить без изменений): ").strip()

        if age_input == "":
            age = None
        else:
            try:
                age = int(age_input)
            except ValueError:
                print("Возраст должен быть целым числом.")
                return

        owner_name = (
            input("Введите новое имя владельца (Enter - оставить без изменений): ").strip() or None
        )

        self._registry.update(
            pet_id=pet_id,
            name=name,
            pet_type=pet_type,
            age=age,
            owner_name=owner_name,
        )

        pet = self._registry.read(pet_id)

        print("Информация о питомце обновлена.")
        print(self._registry.get_pet_info(pet))

    def _delete(self) -> None:
        """Удалить питомца."""

        while True:
            try:
                pet_id = int(input("Введите id питомца: "))
                break
            except ValueError:
                print("ID должен быть целым числом.")

        self._registry.delete(pet_id)

        print(f"Питомец с id={pet_id} успешно удален.")

    def _help(self) -> None:
        """Вывести список доступных команд."""
        print(
            "Доступные команды:\n  create\n  read\n  read all\n  update\n  delete\n  help\n  stop"
        )

    def _stop(self) -> None:
        """Завершить работу программы."""
        self._running = False
        print("Работа завершена.")
