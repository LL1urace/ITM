# Практика
# Часть 1. Все входные и выходные данные в заданиях этой группы являются вещественными числами.

# 6. Даны длины ребер a, b, c прямоугольного параллелепипеда.
# Найти его объем V = a·b·c и площадь поверхности S = 2·(a·b + b·c + a·c)
def get_parallelepiped_volume_area(length: float, width: float, height: float) -> tuple[float, float]:
    try:
        a = float(length)
        b = float(width)
        c = float(height)
    except TypeError:
        raise TypeError("Значения не являются вещественными числами!")
    except ValueError:
        raise ValueError("Значения (или одно из) не могут быть преобразованы в числа (значения)!")
    if a <= 0 or b <= 0 or c <= 0:
        raise ValueError("Значения (или одно) не могут быть отрицательными числами или нулями!")
    v = a * b * c
    s = 2 * (a * b + b * c + a * c)
    return v, s


if __name__ == "__main__":
    pass