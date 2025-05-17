# Практика
# Часть 1. Все входные и выходные данные в заданиях этой группы являются вещественными числами.

# 5. Дана длина ребра куба a. Найти объем куба V = a3 и площадь его поверхности S = 6·a2
def get_cube_volume_area(edge: float) -> tuple[float, float]:
    try:
        a = float(edge)
    except TypeError:
        raise TypeError("Значение не является вещественным числом!")
    except ValueError:
        raise ValueError("Значение не может быть преобразовано в число (значение)!")
    if edge <= 0:
        raise ValueError("Значение не может быть отрицательным числом или нулем!")
    v = a ** 3
    s = 6 * a ** 2
    return v, s


if __name__ == "__main__":
    pass