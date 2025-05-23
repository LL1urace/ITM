# Практика:
# Примечание: Во всех задачах данные должны вводится пользователем,
# это можно реализовать с помощью функции input.
# Например, начинаем выполнять первую задачу из блока If Else:
# first_number = int(input(«Введите первое число»))
# second_number = int(input(«Введите второе число»))
# third_number = int(input(«Введите третье число»))

# If Else
# 3. Даны два числа. Вывести вначале большее, а затем меньшее из них.
from typing import Union

def print_maxmin_nums(fn: Union[int, float], sn: Union[int, float]) -> tuple[int, int]:
    """Поиск большего из двух чисел и вывод их в порядке убывания"""
    try:
        fn = int(fn)
        sn = int(sn)
    except ValueError:
        raise ValueError("Ошибка-ввода: Не все значения являются целыми числами")

    if fn > sn:
        return fn, sn
    elif fn < sn:
        return sn, fn
    else:
        return fn, sn



if __name__ == "__main__":
    print(print_maxmin_nums(1, 33))