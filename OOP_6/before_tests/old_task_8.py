# Практика

# 8. В классе Car добавьте переменную класса car_drive = 4 и реализуйте classmethod,
# который выводит на экран переменную car_drive
from old_task_4 import MeansOfTransport

class Car(MeansOfTransport):
    """Класс, представляющий автомобиль с указанием марки, цвета и количества колёс."""
    car_drive = 4

    @classmethod
    def show_car_drive(cls) -> None:
        print(f"Car_drive = {cls.car_drive}")

    def __init__(self, brand: str, color: str, wheel_count: int) -> None:
        super().__init__(brand, color)
        self.wheel_count = wheel_count

    def show_wheel_count(self):
        print(f"Количество колёс автомобиля: {self.wheel_count}")

car = Car("Maserati", "White", 4)
Car.show_car_drive()