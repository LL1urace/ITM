# Практика:

# 10. Найти все простые числа от 2 до 50.
from math import sqrt
from typing import List


def find_simple_nums_range2_50() -> List[int]:
    """Возвращает все простые числа от 2 до 50."""
    simple_nums = []
    for n in range(2, 51):
        is_simple = True
        for num in range(2, int(sqrt(n)) + 1):
            if n % num == 0:
                is_simple = False
                break
        if is_simple:
            simple_nums.append(n)
    return simple_nums



if __name__ == "__main__":
    simple_nums_list = find_simple_nums_range2_50()
    print(simple_nums_list)