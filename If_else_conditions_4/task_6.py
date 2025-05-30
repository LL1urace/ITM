# Практика:
# Примечание: Во всех задачах данные должны вводится пользователем,
# это можно реализовать с помощью функции input.
# Например, начинаем выполнять первую задачу из блока If Else:
# first_number = int(input(«Введите первое число»))
# second_number = int(input(«Введите второе число»))
# third_number = int(input(«Введите третье число»))
#
# Switch Case
# 1. Дано целое число K. Вывести строку-описание оценки, соответствующей числу
# K (1 — «плохо», 2 — «неудовлетворительно», 3 — «удовлетворительно», 4 — «хорошо», 5 — «отлично»).
# Если K не лежит в диапазоне 1–5, то вывести строку «ошибка».
def define_score() -> None:
    """Определение оценки в диапазоне от 1 до 5"""
    k = input("Введите целое число K: ")
    try:
        k = int(k)
    except ValueError:
        print("Ошибка-ввода: K не является целым числом")
        return
    match k:
        case 1:
            print("Ваша оценка: «плохо»")
        case 2:
            print("Ваша оценка: «неудовлетворительно»")
        case 3:
            print("Ваша оценка: «удовлетворительно»")
        case 4:
            print("Ваша оценка: «хорошо»")
        case 5:
            print("Ваша оценка: «отлично»")
        case _:
            print("Ошибка-ввода: K не находится в диапазоне 1-5")



if __name__ == "__main__":
    define_score()