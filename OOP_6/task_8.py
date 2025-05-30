# Практика

# 8. В классе Car добавьте переменную класса car_drive = 4 и реализуйте classmethod,
# который выводит на экран переменную car_drive

#from task_4 import MeansOfTransport
class MeansOfTransport:
    """Класс для определения цвета и марки машины."""

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show_color(self) -> None: #  напечатать цвет ТС
        """Выводит на экран цвет транспортного средства."""
        print(f"Цвет ТС: {self.color}")

    def show_brand(self) -> None: #  напечатать марку ТС
        """Выводит на экран марку транспортного средства."""
        print(f"Марка ТС: {self.brand}")


    # Сеттеры и геттеры
    def set_attrs(self, brand, color) -> None:
        """Устанавливает значения для марки и цвета ТС."""
        self.brand = brand
        self.color = color

    def get_attrs(self) -> tuple[str, str]:
        """Возвращает значения для марки и цвета ТС."""
        return self.brand, self.color


class Car(MeansOfTransport):
    """Класс, представляющий автомобиль с указанием марки, цвета и количества колёс."""
    car_drive = 4

    @classmethod
    def return_car_drive(cls) -> None:
        return f"Car_drive = {cls.car_drive}"

    def __init__(self, brand: str, color: str, wheel_count: int) -> None:
        super().__init__(brand, color)
        self.wheel_count = wheel_count

    def show_wheel_count(self):
        print(f"Количество колёс автомобиля: {self.wheel_count}")



if __name__ == "__main__":
    car = Car("Maserati", "White", 4)
    Car.show_car_drive()