# Практика:
# Примечание: Во всех задачах данные должны вводится пользователем,
# это можно реализовать с помощью функции input.
# Например, начинаем выполнять первую задачу из блока If Else:
# first_number = int(input(«Введите первое число»))
# second_number = int(input(«Введите второе число»))
# third_number = int(input(«Введите третье число»))

# If Else
# 5. Даны координаты точки, не лежащей на координатных осях OX и OY.
# Определить номер координатной четверти, в которой находится данная точка.
# Координаты задаются пользователем, например (10, 15).
from typing import List

def get_point_quadrant(coords: List[int|float]) -> int:
    """Возвращает номер координатной четверти в которой находится точка."""
    try:
        x = float(coords[0])
        y = float(coords[1])
    except ValueError:
        raise ValueError("Не все значения являются целыми числами")
    # Проверка на оси
    if x == 0 or y == 0:
        raise ValueError("Точка лежит на осях OX или OY.")
    # Определение четверти
    if x > 0 and y > 0:
        return 1
    elif x < 0 < y:
        return 2
    elif x < 0 and y < 0:
        return 3
    elif x > 0 > y:
        return 4
    else:
        raise ValueError("Не удалось найти номер четверти.")


if __name__ == "__main__":
    print(get_point_quadrant([0, 0]))