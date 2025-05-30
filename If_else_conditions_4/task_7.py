# Практика:
# Примечание: Во всех задачах данные должны вводится пользователем,
# это можно реализовать с помощью функции input.
# Например, начинаем выполнять первую задачу из блока If Else:
# first_number = int(input(«Введите первое число»))
# second_number = int(input(«Введите второе число»))
# third_number = int(input(«Введите третье число»))
#
# Switch Case
# 2. Дан номер месяца — целое число в диапазоне 1–12 (1 — январь, 2 — февраль и т. д.).
# Определить количество дней в этом месяце для невисокосного года.
def get_days_in_month(month_number: int) -> str:
    """Определение кол-ва дней в этом месяце для невисокосного года"""
    try:
        m = int(month_number)
    except TypeError:
        raise TypeError("Ошибка-ввода: номер месяца должен быть целым числом")
    except ValueError:
        raise ValueError("Ошибка-ввода: номер месяца должен быть целым числом")

    match m:
        case 1:
            return "Кол-во дней в январе: 31"
        case 2:
            return "Кол-во дней в феврале: 28"
        case 3:
            return "Кол-во дней в марте: 31"
        case 4:
            return "Кол-во дней в апреле: 30"
        case 5:
            return "Кол-во дней в мае: 31"
        case 6:
            return "Кол-во дней в июне: 30"
        case 7:
            return "Кол-во дней в июле: 31"
        case 8:
            return "Кол-во дней в августе: 31"
        case 9:
            return "Кол-во дней в сентябре: 30"
        case 10:
            return "Кол-во дней в октябре: 31"
        case 11:
            return "Кол-во дней в ноябре: 30"
        case 12:
            return "Кол-во дней в декабре: 31"
        case _:
            return "Ошибка-ввода: номер месяце не находится в диапазоне 1-12"



if __name__ == "__main__":
    print(get_days_in_month("1"))