# Практика
#
# 1. Посмотрите первые 21 видео про ООП на python (21/21)
# 1.1. Повторить код из видео 10
from string import ascii_letters


class Person:
    S_RUS = "абвгдеёжзиклмнопрстуфхцчшщьыъэюя-"
    S_RUS_UPPER = S_RUS.upper()

    def __init__(self, fio: str, old: int, ps: str, weight: float) -> None:
        self.verify_fio(fio)

        self.__fio = fio.split()
        self.old = old # Проверка значений через @property.setter
        self.passport = ps
        self.weight = weight

    @classmethod
    def verify_fio(cls, fio):
        if not isinstance(fio, str):
            raise TypeError("ФИО должно быть строкой!")

        f = fio.split()
        if len(f) != 3:
            raise TypeError("Неверный формат ФИО!")

        letters = ascii_letters + cls.S_RUS + cls.S_RUS_UPPER
        for s in f:
            if len(s) < 1:
                raise TypeError("В ФИО должен быть хотя бы один символ!")
            if len(s.strip(letters)) != 0:
                raise TypeError("В ФИО можно использовать только буквенные символы и дефис!")

    @classmethod
    def verify_old(cls, old):
        if not isinstance(old, int) or not (14 < old < 120):
            raise TypeError("Возраст должен быть целым числом в диапазоне [14: 120]!")

    @classmethod
    def verify_weight(cls, weight):
        if not isinstance(weight, float) or weight < 20:
            raise TypeError("Вес должен быть вещественным числом от 20 и выше!")

    @classmethod
    def verify_ps(cls, ps):
        if not isinstance(ps, str):
            raise TypeError("Паспорт должен быть строкой!")

        p = ps.split()
        if len(p) != 2 or len(p[0]) != 4 or len(p[1]) != 6:
            raise TypeError("Неверный формат паспорта!")

        for s in p:
            if not s.isdigit():
                raise TypeError("Серия и номер паспорта должны быть числами!")

    @property
    def fio(self):
        return self.__fio

    @property
    def old(self):
        return self.__old

    @old.setter
    def old(self, old):
        self.verify_old(old)
        self.__old = old

    @property
    def passport(self):
        return self.__passport

    @passport.setter
    def passport(self, ps):
        self.verify_ps(ps)
        self.__passport = ps

    @property
    def weight(self):
        return self.__weight

    @weight.setter
    def weight(self, weight):
        self.verify_weight(weight)
        self.__weight = weight




person = Person("Рожин Александр Александрович", 22, "1234 567890", 90.0)
person.old = 50
person.passport = "0987 654321"
person.weight = 70.0
print(person.__dict__)