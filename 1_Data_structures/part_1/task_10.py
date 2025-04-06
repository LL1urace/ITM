# Практика
# Часть 1. Все входные и выходные данные в заданиях этой группы являются вещественными числами.

# 10. Даны два ненулевых числа. Найти сумму, разность, произведение и частное их квадратов.
a = input("Введите два ненулевых числа: a = ")
b = input("Введите два ненулевых числа: b = ")

try:
    a = float(a)
    b = float(b)

    if a == 0 or b == 0:
        print("Ошибка: В введенных значения есть нулевые числа!")
        exit()

    sum = a + b
    diff = a - b
    prod = a * b
    quot_squares = (a ** 2) / (b ** 2)

    print()
    print(f"Сумма чисел равна: sum = {sum}")
    print(f"Разность чисел равна: diff = {diff}")
    print(f"Произведение чисел равно: prod = {prod}")
    print(f"Частное квадратов чисел равно: quot_squares = {quot_squares}")
except ValueError:
    print("Ошибка: Введенные значения не являются вещественным числами!")