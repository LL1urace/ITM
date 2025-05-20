# Практика:
# Примечание: Во всех задачах данные должны вводится пользователем,
# это можно реализовать с помощью функции input.
# Например, начинаем выполнять первую задачу из блока If Else:
# first_number = int(input(«Введите первое число»))
# second_number = int(input(«Введите второе число»))
# third_number = int(input(«Введите третье число»))

# If Else
# 4. Даны три числа. Найти наименьшее из них.
def min_num() -> None:
    """Поиск наименьшего из трех чисел"""
    print("Поиск наименьшего из трех чисел:")
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

    min_val = first_num

    if second_num < first_num:
        min_val = second_num
    if third_num < min_val:
        min_val = third_num

    print(f"Наименьшее из трех чисел: {min_val}")



if __name__ == "__main__":
    min_num()