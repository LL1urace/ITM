# Практика

# 3. Создайте класс MeansOfTransport (для определения цвета и марки машины),
# принимающий 2 аргумента при инициализации (марка и цвет транспортного средства).
# В этом классе реализуйте методы show_color(), выводящий на печать цвет транспортного средства
# и show_brand, для получения марки транспортного средства.
class MeansOfTransport:
    """Класс для определения цвета и марки машины."""

    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def show_color(self) -> str: #  напечатать цвет ТС
        """Выводит на экран цвет транспортного средства."""
        return f"Цвет ТС: {self.color}"

    def show_brand(self) -> str: #  напечатать марку ТС
        """Выводит на экран марку транспортного средства."""
        return f"Марка ТС: {self.brand}"


if __name__ == "__main__":
    car = MeansOfTransport("Ferrari", "Red")
    print(car.show_brand())
    print(car.show_color())