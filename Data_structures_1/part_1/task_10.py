# Практика
# Часть 1. Все входные и выходные данные в заданиях этой группы являются вещественными числами.

# 10. Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов.
def get_squares_operations(num1: float, num2: float) -> tuple[float, float, float, float]:
    try:
        a = float(num1)
        b = float(num2)
    except TypeError:
        raise TypeError("Значения не являются вещественными числами!")
    except ValueError:
        raise ValueError("Значения (или одно из) не могут быть преобразованы в числа (значения)!")
    if a == 0 or b == 0:
        raise ValueError("Значения не могут быть равны нулю!")
    sum_sq = calc_sum_sq(a, b)
    diff_sq = calc_difference_sq(a, b)
    prod_sq = calc_product_sq(a, b)
    quot_sq = calc_quotient_sq(a, b)
    return sum_sq, diff_sq, prod_sq, quot_sq


def calc_sum_sq(num1: float, num2: float) -> float:
    return num1 ** 2 + num2 ** 2

def calc_difference_sq(num1: float, num2: float) -> float:
    return num1 ** 2 - num2 ** 2

def calc_product_sq(num1: float, num2: float) -> float:
    return (num1 ** 2) * (num2 ** 2)

def calc_quotient_sq(num1: float, num2: float) -> float:
    return (num1 ** 2) / (num2 ** 2)



if __name__ == "__main__":
    pass