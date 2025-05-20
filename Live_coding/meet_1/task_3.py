# 3.
# Условие:
# Функция get_stats(nums: list[int]) -> dict[str, float] возвращает словарь с ключами min, max, avg (среднее значение).
#
# Пример:
# get_stats([1, 2, 3, 4, 5]) → {'min': 1, 'max': 5, 'avg': 3.0}

def get_stats(nums: list[int]) -> dict[str, float]:
    d = {}
    min_nums = nums[0]
    max_nums = nums[0]
    sum_nums = 0
    avg_nums = None

    for item in nums:
        if min_nums > item:
            min_nums = item
        if max_nums < item:
            max_nums = item
        sum_nums += item

    avg_nums = sum_nums / len(nums)
    d["min"] = min_nums
    d["max"] = max_nums
    d["avg"] = avg_nums

    return d



if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    d = get_stats(my_list)
    print(d)