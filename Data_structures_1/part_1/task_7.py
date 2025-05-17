# Практика
# Часть 1. Все входные и выходные данные в заданиях этой группы являются вещественными числами.

# 7. Найти длину окружности L и площадь круга S заданного радиуса R: L = 2·π·R, S = π·R2, π=3.14
from math import pi

def get_circle_length_area(radius: float) -> tuple[float, float]:
    try:
        r = float(radius)
    except TypeError:
        raise TypeError("Значения не являются вещественными числами!")
    except ValueError:
        raise ValueError("Значение не может быть преобразовано в число (значение)!")
    if r <= 0:
        raise ValueError("Значение не может быть отрицательным числом или нулем!")
    l = 2 * pi * r
    s = pi * r ** 2
    return l, s



if __name__ == "__main__":
    pass