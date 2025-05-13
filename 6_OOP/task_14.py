# Практика

# 14. Напишите класс, который принимает список людей с интерфейсом добавления
# новых и при итерации возвращал имена людей
class People:
    """Класс, представляющий людей."""

    def __init__(self, people_list: list[str]) -> None:
        """Конструктор класса People, принимает список людей"""
        self.people_list = people_list
        self.__index = 0

    def add_people(self, people_list: str | list[str]) -> None:
        """Добавляет людей в список"""
        if isinstance(people_list, list) and len(people_list) != 0:
            for person in people_list:
                if isinstance(person, str):
                    self.people_list.append(person)
                else:
                    raise TypeError("Среди значений списка, есть не строковые значения!")
        elif isinstance(people_list, str):
            self.people_list.append(people_list)
        else:
            raise TypeError("Список людей должен быть строкой или списком строк!")

    def __iter__(self) -> 'People':
        """Возвращает итератор (сам объект), подготавливает к началу итерации."""
        self.__index = 0
        return self

    def __next__(self) -> str:
        """Возвращает следующее имя из списка при итерации."""
        if self.__index >= len(self.people_list):
            raise StopIteration
        person = self.people_list[self.__index]
        self.__index += 1
        return person

    def __str__(self) -> str:
        """Возвращает строковое представление списка людей."""
        return f"People: {",".join(self.people_list)}" + ".\n"

friends = People(["Чел1", "Чел2"])
print(friends)

friends.add_people("Чел3")
print(friends)

friends.add_people(["Чел4", "Чел5"])

print("Список людей через итерации:")
for person in friends:
    print(person)

# friends.add_people([])