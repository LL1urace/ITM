# Практика:

# 9. Вывести таблицу умножения для числа 2 от 1 до 10.
from typing import List

def output_multiplication2table() -> List[int]:
    """Возвращает таблицу умножения для числа 2 от 1 до 10."""
    table2 = []
    for multiplier in range(1, 11):
        table2.append(f"{2} * {multiplier} = {2 * multiplier}")
    return table2



if __name__ == "__main__":
    table = output_multiplication2table()
    print(table[6])