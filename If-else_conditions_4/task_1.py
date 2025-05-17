# Практика:
# Примечание: Во всех задачах данные должны вводится пользователем,
# это можно реализовать с помощью функции input.
# Например, начинаем выполнять первую задачу из блока If Else:
# first_number = int(input(«Введите первое число»))
# second_number = int(input(«Введите второе число»))
# third_number = int(input(«Введите третье число»))

# If Else
# 1. Даны три целых числа. Найти количество положительных чисел в исходном наборе.
def find_positive_nums_count() -> None:
    """Поиск кол-ва положительных чисел в наборе из 3-х целых чисел"""
    print("Поиск кол-ва положительных чисел в наборе из 3-х целых чисел:")
    first_num = input("Введите первое число: ")
    second_num = input("Введите второе число: ")
    third_num = input("Введите третье число: ")
    try:
        first_num = int(first_num)
        second_num = int(second_num)
        third_num = int(third_num)
    except ValueError:
        print("Ошибка-ввода: Не все значения являются целыми числами")
        return

    count = 0  # счётчик положительных чисел

    if first_num > 0:
        count += 1
    if second_num > 0:
        count += 1
    if third_num > 0:
        count += 1

    print(f"Количество положительных чисел: {count}")


find_positive_nums_count()