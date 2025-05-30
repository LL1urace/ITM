# Практика

# 6. В классе {{Moped}} напишите статическую функцию, которая на вход будет принимать расстояние и
# максимальную скорость, а на выходе получать время, за которое проедет мопед это расстояние.


#from task_4 import MeansOfTransport
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


class Moped(MeansOfTransport):
    """Класс, представляющий мопед с указанием марки, цвета и количества колёс."""

    def __init__(self, brand: str, color: str, wheel_count: int) -> None:
        super().__init__(brand, color)
        self.wheel_count = wheel_count

    def show_wheel_count(self):
        print(f"Количество колёс мопеда: {self.wheel_count}")

    @staticmethod
    def calc_time(destination: float, max_speed: float) -> float: # Optional[float] - либо float, либо None
        try:
            time = float(destination) / float(max_speed)
            return time
        except TypeError as e:
            raise TypeError("Ошибка типизации аргументов функции", e)
        except ZeroDivisionError as e:
            raise ValueError("Ошибка деления на ноль:", e)



if __name__ == "__main__":
    moped = Moped("ALPHA RX 11", "Red", 2)
    moped.show_wheel_count()
    moped_time = moped.calc_time(100, 10)
    print(f"Время за которое мопед проедет {moped_time}:" )