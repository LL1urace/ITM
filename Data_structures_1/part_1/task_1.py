# Практика
# Часть 1. Все входные и выходные данные в заданиях этой группы являются вещественными числами.

# 1. Дана сторона квадрата a. Найти его периметр P = 4·a
def get_square_perimeter(side: float) -> float:
    try:
        a = float(side)
    except TypeError:
        raise TypeError("Значение не является вещественным числом!")
    except ValueError:
        raise ValueError("Значение не может быть преобразовано в число (значение)!")
    if a <= 0:
        raise ValueError("Значение не может быть отрицательным числом или нулем!")
    perimeter = 4 * a
    return perimeter


if __name__ == "__main__":
    get_square_perimeter(-2)
    # get_square_perimeter("вфв")
    # get_square_perimeter([2313, "ывфвф"])
    # get_square_perimeter([2313, 453])