# Практика
# Часть 1. Все входные и выходные данные в заданиях этой группы являются вещественными числами.

# 8. Даны два числа a и b. Найти их среднее арифметическое: (a + b)/2
a = input("Введите два любых вещественных числа: a = ")
b = input("Введите два любых вещественных числа: b = ")
try:
    a = float(a)
    b = float(b)
    avg = (a + b) / 2
    print(f"Среднее арифметическое чисел: avg = {avg}")
except ValueError:
    print("Ошибка: Введенные значения не являются вещественным числами!")