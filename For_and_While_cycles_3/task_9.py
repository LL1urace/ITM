# Практика:

# 9. Вывести таблицу умножения для числа 2 от 1 до 10.
def output_multiplication2table() -> None:
    """Выводит таблицу умножения для числа 2 от 1 до 10."""
    for multiplier  in range(1, 11):
        print(f"{2} * {multiplier} = {2 * multiplier}")



if __name__ == "__main__":
    output_multiplication2table()