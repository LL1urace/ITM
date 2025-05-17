# Практика
#
# 1. Посмотрите первые 21 видео про ООП на python (21/21)
# 1.4. Повторить код из видео 14 (+ добавить недоделанные методы в класс Clock)
from typing import Union
class Clock:
    __DAY = 86400 # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds  # % self.__DAY

    def get_time(self):
        s = self.seconds % 60 # Текущее кол-во секунд
        m = (self.seconds // 60) % 60 # Минуты в текущем часе
        h = (self.seconds // 3600) % 24 # Кол-во часов в дне
        return f"{self.__get_formatted(h)}:{self.__get_formatted(m)}:{self.__get_formatted(s)}"

    @classmethod
    def __get_formatted(cls, x):
        return str(x).rjust(2, "0")

    def __add__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть целым числом или экземпляром класса (int/Clock)!")

        second_operand = other
        if isinstance(other, Clock):
            second_operand = other.seconds

        return Clock(self.seconds + second_operand)

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        if not isinstance(other, (int, Clock)):
            raise ArithmeticError("Правый операнд должен быть целым числом или экземпляром класса (int/Clock)!")

        second_operand = other
        if isinstance(other, Clock):
            second_operand = other.seconds

        self.seconds += second_operand
        return self



c1 = Clock(1000)
c2 = Clock(86405)
print(c2.get_time())
c1 += 85669 # переопределение метода __add__ <=> с1.__add__(100)
# c1 = 100 + c1 # переопределение метода __radd__ <=> с1.__add__(100)
# c3 = c1 + c2
# c3 += c1
print(c1.get_time())
# print(c3.get_time())
c = Clock(86000)
c += 1000  # -> self.seconds = 87000 (без %)
# print(c.get_time())