# Практика:

# 7. Написать программу для нахождения среднего арифметического списка чисел.
# Если при вводе списка чисел была допущена ошибка (например, был передан не список, а строка),
# программа должна корректно обработать эту ошибку и выдать соответствующее сообщение.
# Информация об ошибках должна быть записана в лог.
import logging

logging.basicConfig(level=logging.INFO,
                    filename="task-7_py_log.log",
                    filemode="w",
                    encoding="utf-8",
                    format="%(asctime)s %(levelname)s %(message)s")

logging.info("Запуск программы для нахождения среднего арифметического.")
print("Запуск программы для нахождения среднего арифметического из списка чисел!")
raw_input  = input("Введите список чисел через пробел: ").split()
num_list = []
try:
    if not raw_input:
        raise ZeroDivisionError("Список пустой.")

    for item in raw_input :
        num_list.append(float(item))

    average_num = sum(num_list) / len(num_list)
    print(f"Среднее арифметическое списка чисел равно: {average_num}.")
    logging.info(f"Успешно найдено среднее арифметическое списка чисел: {average_num} у списка {num_list}.")
except ValueError:
    print("Ошибка-ввода: в списке есть элементы не являющиеся числами!")
    logging.error(f"Ошибка-ввода: некорректный состав списка list = {raw_input}.")
except ZeroDivisionError:
    print("Ошибка: список чисел пуст.")
    logging.error("Попытка деления на ноль: пустой список")