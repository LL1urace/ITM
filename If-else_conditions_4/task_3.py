# Практика:
# Примечание: Во всех задачах данные должны вводится пользователем,
# это можно реализовать с помощью функции input.
# Например, начинаем выполнять первую задачу из блока If Else:
# first_number = int(input(«Введите первое число»))
# second_number = int(input(«Введите второе число»))
# third_number = int(input(«Введите третье число»))

# If Else
# 3. Даны два числа. Вывести вначале большее, а затем меньшее из них.
def print_maxmin_nums() -> None:
    """Поиск большего из двух чисел и вывод их в порядке убывания"""
    print("Поиск большего из двух чисел и вывод их в порядке убывания:")
    first_num = input("Введите первое число: ")
    second_num = input("Введите второе число: ")
    try:
        first_num = int(first_num)
        second_num = int(second_num)
    except ValueError:
        print("Ошибка-ввода: Не все значения являются целыми числами")
        return

    if first_num > second_num:
        print(f"Большее из чисел: {first_num}\nМеньшее из чисел: {second_num}")
    elif first_num < second_num:
        print(f"Большее из чисел: {second_num}\nМеньшее из чисел: {first_num}")
    else:
        print(f"Чиcла {first_num} и {second_num} равны")


print_maxmin_nums()