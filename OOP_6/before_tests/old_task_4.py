# Практика

# 4. Работаем с классом из 3 пункта. Реализуйте сеттеры и геттеры для цвета и марки транспортного средства.
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


if __name__ == "__main__":
    car = MeansOfTransport("Ferrari", "Red")
    car.set_attrs("Maserati", "White")
    brand, color = car.get_attrs()
    print(brand, color)