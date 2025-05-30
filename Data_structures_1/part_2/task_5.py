# Практика
# Часть 2. Все входные и выходные данные в заданиях этой группы являются целыми числами.
# Все числа, для которых указано количество цифр (двузначное число, трехзначное число и т. д.), считаются положительными.

# 5. Даны целые положительные числа A и B (A > B).
# На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений).
# Используя операцию взятия остатка от деления нацело, найти длину незанятой части отрезка A.
def get_unused_segment_length(a: int, b: int) -> int:
    try:
        a = int(a)
        b = int(b)
    except TypeError:
        raise TypeError("Значения не являются целыми числами!")
    except ValueError:
        raise ValueError("Значения (или одно из) не могут быть преобразованы в числа (значения)!")
    if a <= 0 or b <= 0:
        raise ValueError("Значения не могут быть отрицательными числами или нулями!")
    if a < b:
        raise ValueError("Первый аргумент должен быть больше второго!")
    segment_remainder = a % b
    return segment_remainder



if __name__ == "__main__":
    pass