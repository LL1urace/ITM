# 2. Условие: Функция sum_even_numbers(nums: list[int]) ->
# int возвращает сумму всех чётных чисел в списке.
#
# Пример:
# sum_even_numbers([1, 2, 3, 4, 5]) → 6

def sum_even_numbers(nums_list):
    sum = 0
    for num in nums_list:
        if num % 2 == 0:
            sum += num
    return sum

if __name__ == "__main__":
    list_Values = [1, 2, 3, 4, 5, 6]
    count = sum_even_numbers(list_Values)
    print(count)