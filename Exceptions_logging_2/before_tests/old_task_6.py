# Практика:

# 6. Написать программу для генерации случайных чисел в заданном диапазоне.
# Если пользователь ввел недопустимые границы диапазона (например, меньше нуля),
# программа должна вывести ошибку и попросить ввести диапазон заново.
# Информация об ошибках должна быть записана в лог.
import logging
import random

# Настройка логирования
logging.basicConfig(level=logging.INFO,
                    filename="task-6_py_log.log",
                    filemode="w",
                    encoding="utf-8",
                    format="%(asctime)s %(levelname)s %(message)s")

# Ввод диапазона
def input_range():
    start = input("Введите начало диапазона: start = ")
    end = input("Введите конец диапазона: end = ")
    if start.lower() == 'exit' or end.lower() == 'exit':
        return None, None
    try:
        start = float(start)
        end = float(end)
    except ValueError:
        print("Ошибка-ввода: числа не являются вещественными! Попробуй еще раз.")
        logging.error(f"Ошибка-ввода: введены некорректные значения start = {start}, end = {end}")
        return input_range()
    if start < 0 or end < 0:
        print("Ошибка: границы диапазона не могут быть отрицательными!")
        logging.error(f"Ошибка: отрицательные значения в диапазоне: start = {start}, end = {end}")
        return input_range()
    if start > end:
        print("Ошибка-ввода: начало диапазона не может быть больше конца, попробуйте заново")
        logging.error(f"Ошибка: диапазон задан не вещественными числами, start = {start}, что больше чем end = {end}")
        return input_range()
    else:
        return start, end



logging.info("Запуск программы генерации случайных чисел в заданном диапазоне")
while True:
    print("Генерация случайных чисел в заданном диапазоне\n(exit - для выхода)")
    start_range, end_range = input_range()

    if start_range is None or end_range is None:
        print("Завершение работы программы...")
        break

    while True:
        rand_num = random.uniform(start_range, end_range)
        logging.info(f"Сгенерировано значение: {rand_num}")
        print(rand_num)

        stop = input("Продолжить генерацию? (stop - для выхода)")

        if stop.lower() == "stop":
            print("Завершение работы программы...")
            break