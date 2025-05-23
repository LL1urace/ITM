# Практика:

# 5. Напишите программу для вывода таблицы умножения от 0 до 9.
# Используйте вложенный цикл for, print и range
# Пример:
# 0*1 = 0
# 0 *2 = 0
# …..
# 9*1 = 9
# 9*2=18
from typing import List

def output_multiplication_table() -> List[str]:
    """Возвращает таблицу умножения от 0 до 9 с множителями от 1 до 10 в виде списка строк."""
    result = []
    for multiplicand in range(0, 10):
        for multiplier in range(1, 11):
            result.append(f"{multiplicand} * {multiplier} = {multiplicand * multiplier}")
        result.append(" ")  # пустая строка для разделения блоков
    return result


if __name__ == "__main__":
    result = output_multiplication_table()
    for row in result:
        print(row)