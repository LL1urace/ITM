# Практика
# Часть 2. Все входные и выходные данные в заданиях этой группы являются целыми числами.
# Все числа, для которых указано количество цифр (двузначное число, трехзначное число и т. д.), считаются положительными.

# 8. Дано двузначное число. Вывести число, полученное при перестановке цифр исходного числа.
def reverse_two_digits_number(num: int) -> int:
    try:
        a = int(num)
    except TypeError:
        raise TypeError("Значение не является целым числом!")
    except ValueError:
        raise ValueError("Значение не может быть преобразовано в число (значение)!")
    if not 10 <= abs(a) <= 99:
        raise ValueError("Значение не является двузначным числом!")
    sign = -1 if a < 0 else 1  # сохраняем знак
    units = abs(a) % 10
    tens = abs(a) // 10
    swapped_digit = sign * (units * 10 + tens)
    return swapped_digit



if __name__ == "__main__":
    pass