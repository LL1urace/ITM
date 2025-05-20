# Практика:

# 10. Найти все простые числа от 2 до 50.
from math import sqrt

def find_simple_nums_range2_50() -> None:
    """Находит все простые числа от 2 до 50."""
    print("Поиск всех простых чисел от 2 до 50.")
    for n in range(2, 51):
        is_simple = True
        for num in range(2, int(sqrt(n)) + 1):
            if n % num == 0:
                is_simple = False
                break
        if is_simple:
            print(n)



if __name__ == "__main__":
    find_simple_nums_range2_50()