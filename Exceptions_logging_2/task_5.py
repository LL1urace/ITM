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

import logging
from math import sqrt
from typing import Union, Tuple

# Настройка логирования
logging.basicConfig(level=logging.INFO,
                    filename="task-5_py_log.log",
                    filemode="w",
                    encoding="utf-8",
                    format="%(asctime)s %(levelname)s %(message)s")


def validate_coefficient(name: str, value: Union[str, float]) -> float:
    """Проверка коэффициента и преобразование в float."""
    logging.info(f"Валидация коэффициента {name} со значением {value}")

    try:
        val = float(value)
        if name == 'a' and val == 0:
            msg = "Коэффициент 'a' не может быть равен 0"
            logging.error(msg)
            raise ValueError(msg)
        return val
    except ValueError:
        msg = f"Некорректное значение для коэффициента {name}: {value}"
        logging.error(msg)
        raise ValueError(msg)


def solve_quadratic(a: float, b: float, c: float) -> Tuple[float, float]:
    """Решение квадратного уравнения. Возвращает кортеж из корней."""
    logging.info(f"Попытка решения уравнения с коэффициентами a={a}, b={b}, c={c}")

    d = b ** 2 - 4 * a * c
    if d < 0:
        msg = f"Дискриминант отрицательный: D = {d}. Нет действительных корней."
        logging.error(msg)
        raise ValueError(msg)
    elif d == 0:
        x = -b / (2 * a)
        logging.info(f"Один корень: x = {x}, дискриминант D = 0")
        return x, x
    else:
        sqrt_d = sqrt(d)
        x1 = (-b + sqrt_d) / (2 * a)
        x2 = (-b - sqrt_d) / (2 * a)
        logging.info(f"Два корня: x1 = {x1}, x2 = {x2}, дискриминант D = {d}")
        return x1, x2



def main():
    print("Решение квадратного уравнения вида ax^2 + bx + c = 0")
    print("Введите коэффициенты (или 'exit' для выхода)")

    while True:
        try:
            a_input = input("a = ").strip()
            if a_input.lower() == "exit":
                break
            a = validate_coefficient("a", a_input)

            b_input = input("b = ").strip()
            if b_input.lower() == "exit":
                break
            b = validate_coefficient("b", b_input)

            c_input = input("c = ").strip()
            if c_input.lower() == "exit":
                break
            c = validate_coefficient("c", c_input)

            x1, x2 = solve_quadratic(a, b, c)
            print(f"\nКорни уравнения: x1 = {x1}, x2 = {x2}\n")

        except ValueError as err:
            print(f"Ошибка: {err}")
            print("Попробуйте снова.\n")

    print("Программа завершена.")


if __name__ == "__main__":
    main()