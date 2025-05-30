# Практика

# 4. Работаем с классом из 3 пункта. Реализуйте сеттеры и геттеры для цвета и марки транспортного средства.
class MeansOfTransport:
    """Класс для определения цвета и марки машины."""

    def __init__(self, brand, color):
        self.__brand = brand
        self.__color = color

    def show_color(self) -> None: #  напечатать цвет ТС
        """Выводит на экран цвет транспортного средства."""
        print(f"Цвет ТС: {self.color}")

    def show_brand(self) -> None: #  напечатать марку ТС
        """Выводит на экран марку транспортного средства."""
        print(f"Марка ТС: {self.brand}")

    # Сеттеры и геттеры
    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color):
        self.__color = color

    @property
    def brand(self):
        return self.__brand

    @brand.setter
    def brand(self, brand):
        self.__brand = brand



if __name__ == "__main__":
    car = MeansOfTransport("Ferrari", "Red")
    car.brand = "Maserati"
    car.color = "White"
    print(car.brand, car.color)