# Практика:

# 5. Написать программу на Python для решения квадратного уравнения ax^2 + bx + c = 0.
# Если дискриминант отрицателен, программа должна выдать ошибку и предложить пользователю
# попробовать еще раз с другими коэффициентами. При выполнении скрипта в лог должна
# записываться информация об успехе или неудаче операции.
import logging
from math import sqrt

# Настройка логирования
logging.basicConfig(level=logging.INFO,
                    filename="task-5_py_log.log",
                    filemode="w",
                    encoding="utf-8",
                    format="%(asctime)s %(levelname)s %(message)s")

# Получаем коэффициент и проверяем его
def get_coefficient(name):
    logging.info(f"Проверка ввода коэффициента {name}")
    value = input(f"Введите коэффициенты ур-ия: {name} = ").strip()
    if value.lower()  == 'exit':
        return None
    try:
        value = float(value)
        if name == 'a' and value == 0:
            print("Ошибка-ввода: коэффициент a не может быть равным 0.")
            logging.info(f"Коэффициент {name} не может быть равным {value}.")
        else:
            return value
    except ValueError:
        print("Ошибка-ввода: введите число или 'exit' для выхода.")
        logging.error(f"Ошибка-ввода: введено некорректное значение коэффициента, {name} = {value}")
        return get_coefficient(name)


# Решаем квадратное уравнение
def calc_equation(a, b, c):
    logging.info(f"Поиск решения с коэффициентами a = {a}, b = {b} и c = {c}")
    d = b ** 2 - 4 * a * c
    if d < 0:
        print("Ошибка: D < 0, попробуйте ввести другие коэффициенты ур-ия.")
        logging.error(f"D = {d}, выход из функции расчета уравнения")
        return
    elif d == 0:
        x1 = x2 = -b/(2 * a)
        logging.info(f"Корни успешно найдены x1 = {x1}, x2 = {x2}, при D = {d}")
    else:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        logging.info(f"Корни успешно найдены x1 = {x1}, x2 = {x2}, при D = {d}")
    print(f"\nНайденные корни уравнения: x1 = {x1}, x2 = {x2}")



if __name__ == "__main__":
    while True:
        print("Решение квадратного уравнения ax^2 + bx + c = 0\n(exit - для выхода)")
        a = get_coefficient("a")
        if a is None:
            print("Завершение работы программы...")
            break

        b = get_coefficient("b")
        if b is None:
            print("Завершение работы программы...")
            break

        c = get_coefficient("c")
        if c is None:
            print("Завершение работы программы...")
            break

        calc_equation(a, b, c)
