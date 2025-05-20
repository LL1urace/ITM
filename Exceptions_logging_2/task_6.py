# Практика:

# 6. Написать программу для генерации случайных чисел в заданном диапазоне.
# Если пользователь ввел недопустимые границы диапазона (например, меньше нуля),
# программа должна вывести ошибку и попросить ввести диапазон заново.
# Информация об ошибках должна быть записана в лог.
import logging
import random
from typing import Union


# Настройка логирования
logging.basicConfig(level=logging.INFO,
                    filename="task-6_py_log.log",
                    filemode="w",
                    encoding="utf-8",
                    format="%(asctime)s %(levelname)s %(message)s")

# Ввод диапазона
def input_range(start: Union[float, str], end: Union[float, str]) -> Union[float, None]:
    if start.lower() == 'exit' or end.lower() == 'exit':
        return None
    try:
        start = float(start)
        end = float(end)
    except ValueError:
        logging.error(f"Ошибка-ввода: введены некорректные значения start = {start}, end = {end}")
        return None
    if start < 0 or end < 0:
        logging.error(f"Ошибка: отрицательные значения в диапазоне: start = {start}, end = {end}")
        return None
    if start > end:
        logging.error(f"Ошибка: диапазон задан не неверными числами, start = {start}, что больше чем end = {end}")
        return None
    else:
        return start, end


if __name__ == "__main__":
    pass
    # logging.info("Запуск программы генерации случайных чисел в заданном диапазоне")
    # start_range, end_range = input_range(1, 5)
    # if start_range is None or end_range is None:
    #     print("Завершение работы программы...")
    # rand_num = random.uniform(start_range, end_range)
    # logging.info(f"Сгенерировано значение: {rand_num}")
    # print(rand_num)