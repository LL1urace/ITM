# Практика
# Часть 1. Все входные и выходные данные в заданиях этой группы являются вещественными числами.

# 3. Даны стороны прямоугольника a и b. Найти его площадь S = a·b и периметр P = 2·(a + b)
def get_rectangle_area_perimeter(height: float, width: float) -> tuple[float, float]:
    try:
        a = float(height)
        b = float(width)
    except TypeError:
        raise TypeError("Значения не являются вещественными числами!")
    except ValueError:
        raise ValueError("Значения (или одно из) не могут быть преобразованы в числа (значения)!")
    if a <= 0 or b <= 0:
        raise ValueError("Значение не может быть отрицательным числом или нулем!")
    s = a * b
    p = 2 * (a + b)
    return s, p


if __name__ == "__main__":
    # get_rectangle_area_perimeter(3, "3")
    # get_rectangle_area_perimeter(-1, 2)
    #get_rectangle_area_perimeter(-1)
    get_rectangle_area_perimeter(True, False)