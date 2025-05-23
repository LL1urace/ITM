# Практика:
# Примечание: Во всех задачах данные должны вводится пользователем,
# это можно реализовать с помощью функции input.
# Например, начинаем выполнять первую задачу из блока If Else:
# first_number = int(input(«Введите первое число»))
# second_number = int(input(«Введите второе число»))
# third_number = int(input(«Введите третье число»))

# If Else
# 1. Даны три целых числа. Найти количество положительных чисел в исходном наборе.
def find_positive_nums_count(fn, sn, tn) -> int:
    """Поиск кол-ва положительных чисел в наборе из 3-х целых чисел"""
    try:
        fn = int(fn)
        sn = int(sn)
        tn = int(tn)
    except ValueError:
        raise ValueError("Не все значения являются целыми числами!")
    count = 0  # счётчик положительных чисел
    if fn > 0:
        count += 1
    if sn > 0:
        count += 1
    if tn > 0:
        count += 1
    return count



if __name__ == "__main__":
    print(find_positive_nums_count(1, 2, 3))