# Практика
# Часть 1. Все входные и выходные данные в заданиях этой группы являются вещественными числами.

# 3. Даны стороны прямоугольника a и b. Найти его площадь S = a·b и периметр P = 2·(a + b)
a = input("Введите стороны прямоугольника: a = ")
b = input("Введите стороны прямоугольника: b = ")
try:
    a = float(a)
    b = float(b)
    S = a * b
    P = 2 * (a + b)
    print(f"Площадь и периметр равны: S = {S},P = {P}")
except ValueError:
    print("Ошибка: Введенные значения не являются вещественными числами!")