# Практика:
# Примечание: Во всех задачах данные должны вводится пользователем,
# это можно реализовать с помощью функции input.
# Например, начинаем выполнять первую задачу из блока If Else:
# first_number = int(input(«Введите первое число»))
# second_number = int(input(«Введите второе число»))
# third_number = int(input(«Введите третье число»))

# If Else
# 2. Даны два числа. Вывести большее из них.
def max_num() -> None:
    """Поиск большего из двух чисел"""
    print("Поиск большего из двух чисел:")
    first_num = input("Введите первое число: ")
    second_num = input("Введите второе число: ")
    try:
        first_num = int(first_num)
        second_num = int(second_num)
    except ValueError:
        print("Ошибка-ввода: Не все значения являются целыми числами")
        return

    if first_num > second_num:
        print(f"Большее из двух чисел: {first_num}")
    elif first_num < second_num:
        print(f"Большее из двух чисел: {second_num}")
    else:
        print(f"Чиcла {first_num} и {second_num} равны")



if __name__ == "__main__":
    max_num()