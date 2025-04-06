# Практика
# Часть 1. Все входные и выходные данные в заданиях этой группы являются вещественными числами.

# 7. Найти длину окружности L и площадь круга S заданного радиуса R: L = 2·π·R, S = π·R2, π=3.14
pi = 3.14
R = input("Введите длину радиуса: R = ")
try:
    R = float(R)
    L = 2 * pi * R
    S = pi * R ** 2
    print(f"Длина окружности и площадь круга равны: L = {L}, S = {S}")
except ValueError:
    print("Ошибка: Введенное значение не является вещественным числом!")