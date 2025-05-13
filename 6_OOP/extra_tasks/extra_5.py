# Практика
#
# 1. Посмотрите первые 21 видео про ООП на python (21/21)
# 1.5. Повторить код из видео 15 (+ добавить методы в класс Clock)
class Clock:
    __DAY = 86400 # число секунд в одном дне

    def __init__(self, seconds: int):
        if not isinstance(seconds, int):
            raise TypeError("Секунды должны быть целым числом")
        self.seconds = seconds % self.__DAY

    @classmethod
    def __verify_data(cls, other):
        if not isinstance(other, (int, Clock)):
            raise TypeError("Правый операнд должен быть типа int или Clock.")

        return other if isinstance(other, int) else other.seconds

    def __eq__(self, other):
        second_operand = self.__verify_data(other)
        return self.seconds == second_operand

    def __lt__(self, other):
        second_operand = self.__verify_data(other)
        return self.seconds < second_operand

    def __le__(self, other):
        second_operand = self.__verify_data(other)
        return self.seconds <= second_operand


c1 = Clock(1000)
c2 = Clock(2000)
print(c1 == c2)
print(c1 < c2)
print(c1 <= c2)