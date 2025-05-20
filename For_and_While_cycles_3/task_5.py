# Практика:

# 5. Напишите программу для вывода таблицы умножения от 0 до 9.
# Используйте вложенный цикл for, print и range
# Пример:
# 0*1 = 0
# 0 *2 = 0
# …..
# 9*1 = 9
# 9*2=18
def output_multiplication_table() -> None:
    """Выводит таблицу умножения от 0 до 9 с множителями от 1 до 10."""
    for multiplicand  in range(0, 10):
        for multiplier  in range(1, 11):
            print(f"{multiplicand} * {multiplier} = {multiplicand * multiplier}")
        print()


if __name__ == "__main__":
    output_multiplication_table()