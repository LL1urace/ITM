# Практика
# Часть 2. Все входные и выходные данные в заданиях этой группы являются целыми числами.
# Все числа, для которых указано количество цифр (двузначное число, трехзначное число и т. д.), считаются положительными.

# 8. Дано двузначное число. Вывести число, полученное при перестановке цифр исходного числа.
a = input("Введите двузначное число: a = ")
try:
    a = int(a)

    if not 10 <= abs(a) <= 99:
        print("Ошибка: Число не является двузначным!")
        exit()

    sign = -1 if a < 0 else 1  # сохраняем знак

    units = abs(a) % 10
    tens = abs(a) // 10

    swapped_digit = sign * (units * 10 + tens)
    print(f"Число полученное при перестановке цифр: swapped_digit = {swapped_digit}")
except ValueError:
    print("Ошибка: Введенное значение не является целым числом!")