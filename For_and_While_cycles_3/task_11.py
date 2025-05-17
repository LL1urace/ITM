# Практика:

# 11. Посчитать сумму квадратов чисел от 1 до 10.
def output_sum_squares_ten_range() -> None:
    """Считает сумму квадратов чисел от 1 до 10."""
    sum_squares_ten_range = 0
    for num in range(1, 11):
        sum_squares_ten_range += num ** 2
    print(f"Сумма всех квадратов чисел от 1 до 10: {sum_squares_ten_range}")



output_sum_squares_ten_range()