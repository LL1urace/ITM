# Практика:
#
# 4. Напишите программу для вывода на экран чисел от 0 до 100
# Вам понадобиться цикл for, конструкция range и print
from typing import List

def output_range() -> List[int]:
    """Выводит числа от 0 до 100 включительно."""
    digits = []
    for digit in range(101):
        digits.append(digit)
    return digits

if __name__ == "__main__":
    print(output_range())