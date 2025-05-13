# Практика

# 13. Реализуйте класс Dog. Придумайте, какие переменные будет принимать данный класс
# и какие методы будут реализованы. Реализуйте в этом классе паттерн Singleton
# Пример: https://pythonpip.ru/osnovy/shablon-proektirovaniya-singleton-v-python
from random import randint

class Dog:
    """Класс, представляющий собаку."""
    __instance = None
    COMMON_BREEDS = ["Лабрадор", "Овчарка", "Бульдог", "Пудель",
                     "Доберман", "Бигль", "Хаски", "Дворняжка"] # Возможные значения породы
    COLORS = ["Чёрный", "Белый", "Коричневый", "Рыжий",
              "Серый", "Пятнистый", "Трёхцветный"] # Возможные значения цвета
    MOODS = ["Счастливое", "Игривое", "Спокойное",
              "Уставшее", "Нервное", "Агрессивное"] # Возможные значения настроения
    LOCATIONS = ["Дом", "Улица", "Вет. клиника", "Парк"] # Возможные значения местоположения
    health_limit = 100.0 # Предел здоровья собаки
    energy_limit = 100.0 # Предел энергии собаки
    average_life_old = randint(8, 12) # Случайное число (сколько проживет собака)
    is_alive = True

    # Реализация паттерна проектирования Singletone
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance


    def __del__(self):
        Dog.__instance = None


    def __init__(self, nickname: str, breed: str, color: str, age: int,
                sex: str, weight: float = 15, is_hungry: bool = False,
                 health_level: float = 100.0, energy_level: float = 100.0,
                 location: str = LOCATIONS[0], mood: str = MOODS[2],) -> None:
        if hasattr(self, '_initialized') and self._initialized:
            print("Нельзя создать второй экземпляр класса Dog.")
            return  # Если объект уже был инициализирован, пропускаем

        self.nickname = nickname # Кличка
        self.breed = breed # Порода
        self.color = color # Раскраска
        self.age = age # Возраст
        self.sex = sex # Пол
        self.weight = weight # Вес
        self.is_hungry = is_hungry # Состояние голода (голодна или нет)
        self.health_level = health_level  # Уровень здоровья
        self.energy_level = energy_level # Уровень энергии
        self.location = location  # Местоположение
        self.mood = mood  # Настроение

        self._initialized = True

    @classmethod
    def get_instance(cls, *args, **kwargs) -> "Dog":
        """Возвращает экземпляр класса, если он существует и создает в обратном случае."""
        if cls.__instance is None:
            cls.__instance = cls(*args, **kwargs)
        return cls.__instance

    # Методы, которые можно реализовать:
    def bark(self) -> None:
        """Выводит звук лая собаки."""
        print(f"{self.nickname}: Гав-гав!")


    def eat(self, food: str, energy_value: (int, float)) -> None:
        """Принимает еду и её энергетическую ценность, уменьшает голод и увеличивает энергию."""
        if not isinstance(food, str) or not food.strip():
            raise ValueError("Еда должна быть непустой строкой!")

        if not isinstance(energy_value, (int, float)):
            raise TypeError("Энергетическая ценность еды выражается в числах!")

        if energy_value <= 0:
            raise ValueError("Энергетическая ценность еды не может быть 0 или меньше 0!")

        self.is_hungry = False
        self.energy_level += energy_value
        self.energy_level = min(self.energy_limit, self.energy_level)

        print(f"\"{self.nickname}\" съел(a) \"{food}\" и теперь имеет \"{self.energy_level}\"% уровень энергии!")
        self.update_mood()  # Корректировка настроения


    def update_mood(self) -> None:
        """Корректирует настроение в соответствии с уровнями энергии и здоровья."""
        health_percent = self.health_level / self.health_limit # Пересчитываем процент учитывая лимиты
        energy_percent = self.energy_level / self.energy_limit
        old_mood = self.mood# Сейвим старый mood

        match (health_percent, energy_percent):
            case (h, e) if h <= 0.3 or e <= 0.3:
                self.mood = self.MOODS[4]  # Нервное
            case (h, e) if h <= 0.4 and e <= 0.4:
                self.mood = self.MOODS[3]  # Уставшее
            case (h, e) if h >= 0.8 and e >= 0.8:
                self.mood = self.MOODS[0]  # Счастливое
            case (h, e) if h >= 0.6 and e >= 0.6:
                self.mood = self.MOODS[1]  # Игривое
            case (h, e) if h > 0.4 and e > 0.4:
                self.mood = self.MOODS[2]  # Спокойное
            case _:
                self.mood = self.MOODS[5]  # Агрессивное

        if old_mood != self.mood:
            print(f"\"{self.nickname}\" теперь имеет \"{self.mood}\" настроение!")


    def sleep(self, sleep_hours: int) -> None:
        """Принимает количество часов сна, увеличивает энергию."""
        if not isinstance(sleep_hours, int):
            raise TypeError("Количество часов сна должно быть целым числом")
        if sleep_hours <= 0:
            raise ValueError("Количество сна не может быть 0 или меньше 0")

        energy_gain = sleep_hours * 10
        self.energy_level += energy_gain
        self.energy_level = min(self.energy_limit, self.energy_level)

        print(f"\"{self.nickname}\" поспал(a) \"{sleep_hours}\" ч. и теперь имеет \"{self.energy_level}\"% уровень энергии!")
        self.update_mood()  # Корректировка настроения


    def play(self) -> None:
        """Уменьшает энергию, но улучшает настроение."""
        if self.energy_level <= 0:
            print(f"\"{self.nickname}\" не может играть, у него нет энергии!")
            return

        self.energy_level -= 15
        self.energy_level = max(0.0, self.energy_level)

        print(f"\"{self.nickname}\" поиграл(а), теперь его/её энергия составляет \"{self.energy_level}\"%.")
        self.update_mood()


    def show_describe(self) -> None:
        """Выводит описание собаки(имя, возраст, породу и т.д.)."""
        print(f"Описание собаки {self.nickname}:\n---------------")
        print(f"Кличка: {self.nickname}")
        print(f"Порода: {self.breed}")
        print(f"Окрас: {self.color}")
        print(f"Возраст: {self.age} лет")
        print(f"Пол: {self.sex}")
        print(f"Вес: {self.weight} кг")
        print(f"Голоден: {'Да' if self.is_hungry else 'Нет'}")
        print(f"Энергия: {self.energy_level}/{self.energy_limit}")
        print(f"Здоровье: {self.health_level}/{self.health_limit}")
        print(f"Настроение: {self.mood}\n---------------")


    def get_older(self, add_age: int) -> None:
        """Увеличивает возраст на 1 и уменьшает предел энергии и здоровья."""
        if not isinstance(add_age, int):
            raise TypeError("Возраст должен быть целым числом!")
        if add_age <= 0:
            raise ValueError("Возраст не может быть 0 или меньше 0!")

        self.age += add_age
        print(f"\"{self.nickname}\" уже прожил(а) \"{self.age}\" лет!")
        self.health_limit = max(10.0, self.health_limit - add_age * 2)
        self.energy_limit = max(10.0, self.energy_limit - add_age * 2)

        if self.age >= self.average_life_old:
            print(f"\"{self.nickname}\" достиг(ла) предела своей жизни, прожив прекрасную жизнь! (x_x)")
            self.is_alive = False
        else:
            self.update_mood()


    def change_location(self, location: str) -> None:
        """Изменяет текущее местоположение собаки."""
        if not isinstance(location, str) or not location.strip():
            raise TypeError("Местоположение должно быть непустой строкой!")

        if not location in self.LOCATIONS:
            raise ValueError("Собака не может переместиться в указанное место.")
        self.location = location

        print(f"\"{self.nickname}\" теперь находится в \"{self.location}\"")

    def __str__(self):
        """Возвращает строковое представление класса Dog."""
        return (f"Собака: {self.nickname} ({self.breed}),\nпол: {self.sex}\nвозраст: {self.age},\n"
                f"здоровье:{self.health_level}/{self.health_limit}")




if __name__ == "__main__":
    dog = Dog("Шарик", "Дворняжка", "Пятнистый", 1,"Самец")

    # Реализация синглтона чек
    # dog2 = Dog("Лаки", "Хаски", "Белый", 1, "Самец")
    # print(dog, end='\n\n')
    # print(dog2, end='\n\n')
    # print(dog is dog2, end='\n\n')


    # Работа методов чек
    # dog.bark() # Звук
    # dog.show_describe() # Описание
    # print(dog) # Строковое представление

    # dog.update_mood() # Обновление настроения
    # dog.eat("Корм", 10) # Собака ест
    # dog.sleep(1) # Собака спит
    # dog.change_location("Дом")  # Собака перемещается в другое место
    dog.play()  # Собака перемещается в другое место
    dog.sleep(1)