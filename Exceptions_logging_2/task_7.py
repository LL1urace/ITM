# Практика:

# 7. Написать программу для нахождения среднего арифметического списка чисел.
# Если при вводе списка чисел была допущена ошибка (например, был передан не список, а строка),
# программа должна корректно обработать эту ошибку и выдать соответствующее сообщение.
# Информация об ошибках должна быть записана в лог.
import logging
from typing import Union


def get_avg_of_list(num_list: list[Union[int, float]]) -> Union[float, None]:
    logging.info("Запуск программы для нахождения среднего арифметического.")
    new_nums = []
    if not num_list:
        raise ValueError("Список пустой.")

    try:
        for item in num_list :
            new_nums.append(float(item))
    except ValueError:
        logging.error(f"Ошибка-ввода: некорректный состав списка list = {num_list}.")
        return None
    except ZeroDivisionError:
        logging.error("Попытка деления на ноль: пустой список")
        return None
    average_num = sum(new_nums) / len(new_nums)
    logging.info(f"Успешно найдено среднее арифметическое списка чисел: {average_num} у списка {num_list}.")
    return average_num


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        filename="task-7_py_log.log",
                        filemode="w",
                        encoding="utf-8",
                        format="%(asctime)s %(levelname)s %(message)s")

    get_avg_of_list(["1", "2", "abc"])
