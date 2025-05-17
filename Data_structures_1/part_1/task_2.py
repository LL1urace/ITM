# Практика
# Часть 1. Все входные и выходные данные в заданиях этой группы являются вещественными числами.

# 2. Дана сторона квадрата a. Найти его площадь{{S = a2}}
def get_square_area(side: float) -> float:
    try:
        a = float(side)
    except TypeError:
        raise TypeError("Значение не является вещественным числом!")
    except ValueError:
        raise ValueError("Значение не может быть преобразовано в число (значение)!")
    if a <= 0:
        raise ValueError("Значение не может быть отрицательным числом или нулем!")
    S = a ** 2
    return S



if __name__ == "__main__":
    get_square_area(4)
    get_square_area(7)
    #get_square_area("Антончик")
    # get_square_area(-39.37)
