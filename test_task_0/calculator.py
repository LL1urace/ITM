# Разбор строки:
def parse_input(user_string):
    try:
        parts = user_string.split()

        if len(parts) != 3:
            raise ValueError("Некорректный формат. Введите выражение в формате 'a [+, -, *, /] b'.")

        a, operator, b = parts

        try:
            a, b = int(a), int(b)  # Вложенный try-except для преобразования чисел
        except ValueError:
            raise ValueError("Ошибка: Введённые значения не являются целыми числами!")

        if not (1 <= a <= 10 and 1 <= b <= 10):
            raise ValueError("Числа должны быть в диапазоне от 1 до 10.")

        if operator not in ["+", "-", "*", "/"]:
            raise ValueError("Оператор не соответствует ни одному из списка [+, -, *, /].")

        return a, operator, b

    except Exception as e:
        print("Ошибка ввода: ", e)
        return None


# Вычисление выражения
def calculate_expression(expression):
    try:
        a, action, b = expression

        if action == "+":
            return a + b
        elif action == "-":
            return a - b
        elif action == "*":
            return a * b
        elif action == "/":
            return a // b  # Целочисленное деление
        else:
            raise ValueError("Некорректный оператор (не один из +, -, *, /)")

    except Exception as e:
        print("Ошибка вычисления: ", e)
        return None


if __name__ == "__main__":
    while True:
        user_input = input("Введите выражение (или 'exit' для выхода): ") # Чтение входных данных:

        if user_input.lower() == "exit":
            print("Завершение работы программы...")
            break

        parts_expr = parse_input(user_input)

        if parts_expr is None:
            exit("Программа завершена из-за возникновения ошибки.")

        result = calculate_expression(parts_expr)
        print("Результат вычисления: ", result)