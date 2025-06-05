# Практика:
#
# 1. Дано число в диапазоне от 1_000_000 до 20_000_000.
# Получите список целочисленных делителей этого числа.
from random import randint
from typing import List
from math import sqrt
from time import perf_counter



def get_divisors(number: int) -> List[int]:
    divisors_list = [] # Список для хранения делителей

    for div in range(1, int(sqrt(number)) + 1): # Перебираем возможные делители
        if number % div == 0:
            divisors_list.append(div)
            if div != number // div:
                divisors_list.append(number // div)

    return sorted(divisors_list)


if __name__ == "__main__":
    rand = randint(1_000_000, 20_000_000)
    not_rand = 3600
    start = perf_counter() # Запоминаем время перед вызовом функции
    print(get_divisors(not_rand))
    end = perf_counter()
    print(f"Time: {end - start:.6f} seconds")