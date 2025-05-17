# Практика
# Часть 1. Все входные и выходные данные в заданиях этой группы являются вещественными числами.

# 9. Даны два неотрицательных числа a и b. Найти их среднее геометрическое, т. е. квадратный корень
# из их произведения: (a·b)1/2
def get_geomean_two_nums(num1: float, num2: float) -> float:
    try:
        a = float(num1)
        b = float(num2)
    except TypeError:
        raise TypeError("Значения не являются вещественными числами!")
    except ValueError:
        raise ValueError("Значения (или одно из) не могут быть преобразованы в числа (значения)!")
    if a < 0 or b < 0:
        raise ValueError("Значения не могут быть отрицательными числами!")
    geomean = (a * b) ** (1 / 2)
    return geomean



if __name__ == "__main__":
    pass