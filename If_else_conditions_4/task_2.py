# Практика:
# Примечание: Во всех задачах данные должны вводится пользователем,
# это можно реализовать с помощью функции input.
# Например, начинаем выполнять первую задачу из блока If Else:
# first_number = int(input(«Введите первое число»))
# second_number = int(input(«Введите второе число»))
# third_number = int(input(«Введите третье число»))

# If Else
# 2. Даны два числа. Вывести большее из них.
from typing import Union, Optional


def max_num(fn: Union[int, float], sn: Union[int, float]) -> Optional[int]:
    """Поиск большего из двух чисел"""
    try:
        fn = int(fn)
        sn = int(sn)
    except ValueError:
        raise ValueError("Не все значения являются целыми числами!")

    if fn > sn:
        return fn
    elif fn < sn:
        return sn
    else:
        return None



if __name__ == "__main__":
    print(max_num(1, 2))