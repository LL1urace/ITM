# Практика:
#
# 4. Напишите программу для вывода на экран чисел от 0 до 100
# Вам понадобиться цикл for, конструкция range и print
def output_range() -> None:
    """Выводит числа от 0 до 100 включительно."""
    for digit in range(101):
        print(digit)


if __name__ == "__main__":
    output_range()