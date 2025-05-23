# Практика:
# Примечание: Во всех задачах данные должны вводится пользователем,
# это можно реализовать с помощью функции input.
# Например, начинаем выполнять первую задачу из блока If Else:
# first_number = int(input(«Введите первое число»))
# second_number = int(input(«Введите второе число»))
# third_number = int(input(«Введите третье число»))

# If Else
# 4. Даны три числа. Найти наименьшее из них.
from typing import Union

def min_num(fn: Union[int, float], sn: Union[int, float], tn: Union[int, float]) -> int:
    """Возвращает наименьшее из трех целых чисел."""
    try:
        fn = int(fn)
        sn = int(sn)
        tn = int(tn)
    except ValueError:
        raise ValueError("Не все значения являются целыми числами")

    min_val = fn
    if sn < min_val:
        min_val = sn
    if tn < min_val:
        min_val = tn

    return min_val



if __name__ == "__main__":
    min_num()