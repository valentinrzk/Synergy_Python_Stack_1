from pydantic import BaseModel


class Pet(BaseModel):
    name: str
    pet_type: str
    age: int
    owner_name: str

    def to_dict(self) -> dict[str, str | int]:
        return {
            "Кличка питомца": self.name,
            "Вид питомца": self.pet_type,
            "Возраст питомца": self.age,
            "Имя владельца": self.owner_name,
        }
