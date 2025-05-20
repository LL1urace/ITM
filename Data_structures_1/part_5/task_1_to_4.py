# Практика
# Часть 5. Словари
from typing import Union

# 1. Создайте словарь содержащий данные о человеке.
# В качестве строковых ключей используйте его имя, возраст, пол, рост, вес, размер ноги.
person = dict(
        name = "Даниил",
        age="22",
        sex="Мужской",
        height="200 см",
        weight="110 кг",
        foot_size="50")

# 2. Выведите на экран все данные о человеке по ключам.
def get_person_data(*keys) -> list[str]:
    existing_keys = [key for key in keys if key in person]
    return existing_keys

# 3. Добавьте в словарь ключ и значение размера ноги
def set_person_value(key: str, value: Union[str, int]) -> None:
    person[key] = value

# 4. Удалите из словаря возраст.
def del_person_value() -> None:
    person.pop("age", None) # С None удаление безопасное (нет ошибки если отсутствует ключ)



if __name__ == "__main__":
    pass