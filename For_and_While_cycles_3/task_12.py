# Практика:

# 12. Вывести значения функции y=x^2 от 1 до 10 с шагом 0.5.
from typing import List

def output_func() -> List[str]:
    """Возвращает значения функции y=x^2 от 1 до 10 с шагом 0.5."""
    func_values = []
    x = 1
    while x <= 10:
        func_values.append(f"Значение функции y=x^2 при x = {x} равно: {x ** 2}")
        x += 0.5
    return func_values


if __name__ == "__main__":
    vals = output_func()
    for v in vals:
        print(v)