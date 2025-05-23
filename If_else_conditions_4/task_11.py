# Практика:
# Примечание: Во всех задачах данные должны вводится пользователем,
# это можно реализовать с помощью функции input.
# Например, начинаем выполнять первую задачу из блока If Else:
# first_number = int(input(«Введите первое число»))
# second_number = int(input(«Введите второе число»))
# third_number = int(input(«Введите третье число»))
#
# Switch Case
# 6. *** Реализуйте программу калькулятор. На вход подается три значения:
# первое число, второе число и операция (*, /, + или -).
# На выходе должны получить число, после выполнения операции.
def calculator(f_num: str, s_num: str, operation: str) -> str | None:
    """Производит операции (*, /, + или -) на двух числах"""
    try:
        f_num = float(f_num)
        s_num = float(s_num)
        if operation not in ["*", "/", "+", "-"] or len(operation) != 1:
            return "Ошибка-ввода: некорректные данные операции"
    except ValueError:
        return "Ошибка-ввода: некорректные данные числовых значений"

    match operation:
        case "*":
            return f"Результат операции: {f_num * s_num}"
        case "/":
            try:
                return f"Результат операции: {f_num / s_num}"
            except ZeroDivisionError:
                return "Ошибка-операции: ошибка деления на ноль"
        case "+":
            return f"Результат операции: {f_num + s_num}"
        case "-":
            return f"Результат операции: {f_num - s_num}"
    return None


if __name__ == "__main__":
    print(calculator("1", "2", "*"))