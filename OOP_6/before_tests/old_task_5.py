# Практика

# 5. Реализуйте два класса Car и Moped, которые будут наследоваться от класса MeansOfTransport.
# При инициализации они должны принимать новый аргументы(количество колес).
from old_task_4 import MeansOfTransport

class Car(MeansOfTransport):
    """Класс, представляющий автомобиль с указанием марки, цвета и количества колёс."""

    def __init__(self, brand: str, color: str, wheel_count: int) -> None:
        super().__init__(brand, color)
        self.wheel_count = wheel_count

    def show_wheel_count(self):
        print(f"Количество колёс автомобиля: {self.wheel_count}")


class Moped(MeansOfTransport):
    """Класс, представляющий мопед с указанием марки, цвета и количества колёс."""

    def __init__(self, brand: str, color: str, wheel_count: int) -> None:
        super().__init__(brand, color)
        self.wheel_count = wheel_count

    def show_wheel_count(self):
        print(f"Количество колёс мопеда: {self.wheel_count}")



car = Car("Maserati", "White", 4)
moped = Moped("ALPHA RX 11", "Red", 2)
car.show_wheel_count()
moped.show_wheel_count()