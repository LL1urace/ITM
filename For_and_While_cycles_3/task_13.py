# Практика:

# 13. Найти факториалы чисел от 1 до 5 (включительно).
from typing import List

def find_factorial() -> List[str]:
    """Возвращает факториалы чисел от 1 до 5 (включительно)."""
    factorials = []
    for f in range(1, 6):
        factorials.append(f"Значение: {f}")
        rf = f
        for j in range(1, f):
            rf *= j
        factorials[f-1] += f" Факториал: {rf}"
    return factorials



if __name__ == "__main__":
    factorials_list = find_factorial()
    for fc in factorials_list:
        print(fc)