# Условие:
# Функция sum_of_squares(nums: list[int]) -> int возвращает сумму квадратов всех элементов списка.
#
# Пример:
# sum_of_squares([1, 2, 3]) → 14
from math import pow

def sum_of_squares(nums: list[int]) -> int:
    sum_sq = 0
    for num in nums:
        sum_sq += pow(num, 2)
    return sum_sq


if __name__ == "__main__":
    print(sum_of_squares([1, 2, 3]))