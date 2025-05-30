# Практика
# Часть 2. Все входные и выходные данные в заданиях этой группы являются целыми числами.
# Все числа, для которых указано количество цифр (двузначное число, трехзначное число и т. д.), считаются положительными.

# 5. Даны целые положительные числа A и B (A > B).
# На отрезке длины A размещено максимально возможное количество отрезков длины B (без наложений).
# Используя операцию взятия остатка от деления нацело, найти длину незанятой части отрезка A.
A = input("Введите два положительных числа (A > B): A = ")
B = input("Введите два положительных числа (A > B): B = ")
try:
    A = int(A)
    B = int(B)

    if A < B:
        print("Ошибка: A меньше чем B")

    segment_remainder = A % B
    print(f"Длина незанятой части отрезка A: segment_remainder = {segment_remainder}")
except ValueError:
    print("Ошибка: Введенные значения не являются целыми числами!")