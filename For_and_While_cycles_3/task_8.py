# Практика:

# 8. Найти сумму всех чисел от 1 до 100.

def output_sum_hundred_range() -> int:
    """Возвращает сумму всех чисел от 1 до 100"""
    sum_hundred_range = 0
    for num in range(1, 101):
        sum_hundred_range += num
    return sum_hundred_range



if __name__ == "__main__":
    print(output_sum_hundred_range())