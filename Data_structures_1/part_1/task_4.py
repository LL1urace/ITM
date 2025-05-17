# Практика
# Часть 1. Все входные и выходные данные в заданиях этой группы являются вещественными числами.

# 4. Дан диаметр окружности d. Найти ее длину{{L = π·d, π = 3.14}}
from math import pi

def get_circle_length(diameter: float) -> float:
    try:
        d = float(diameter)
    except TypeError:
        raise TypeError("Значение не является вещественным числом!")
    except ValueError:
        raise ValueError("Значение не может быть преобразовано в число (значение)!")
    if d <= 0:
        raise ValueError("Значение не может быть отрицательным числом или нулем!")
    l = pi * d
    return l


if __name__ == "__main__":
    pass
    #get_circle_length(True)