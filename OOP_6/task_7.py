# Практика

# 7. Попробуйте инициализировать несколько любых переменных в классе Car и сделайте одну переменную
# приватной, одну защищенной. Попробуйте получить к ним доступ. Какой результат?
from task_4 import MeansOfTransport

class Car(MeansOfTransport):
    """Класс, представляющий автомобиль с указанием марки, цвета и количества колёс."""


    def __init__(self, brand: str, color: str, wheel_count: int, year: int, fuel_type: str) -> None:
        super().__init__(brand, color)
        self.wheel_count = wheel_count
        self._year = year
        self.__fuel_type = fuel_type

    def show_wheel_count(self):
        print(f"Количество колёс автомобиля: {self.wheel_count}")



car = Car("Maserati", "White", 4, 2025, "gasoline")

car_year = car._year # Предупреждение, что так лучше не делать
print(car_year)

car__fuel_type = car.__fuel_type # Ошибка, так как Python использует name mangling на _Car__fuel_type
print(car__fuel_type)