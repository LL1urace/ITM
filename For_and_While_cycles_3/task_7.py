# Практика:

# 7. Вывести все числа от 1 до 100, которые делятся на 3 без остатка.
from typing import List

def output_range() -> List[int]:
    """Возвращает числа от 1 до 100 которые делятся на 3 без остатка."""
    digits_range = []
    for num in range(3, 101, 3):
        digits_range.append(num)
    return digits_range


if __name__ == "__main__":
    digits = output_range()
    print(digits)