# Практика
# Часть 1. Все входные и выходные данные в заданиях этой группы являются вещественными числами.

# 8. Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2
def get_avg_two_nums(num1: float, num2: float) -> float:
    try:
        a = float(num1)
        b = float(num2)
    except TypeError:
        raise TypeError("Значения не являются вещественными числами!")
    except ValueError:
        raise ValueError("Значения (или одно из) не могут быть преобразованы в числа (значения)!")
    avg = (num1 + num2) / 2
    return avg

if __name__ == "__main__":
    pass
    # get_avg_two_nums(False, False)