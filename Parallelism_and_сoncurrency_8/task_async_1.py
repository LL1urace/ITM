# Практика:
#
# 1. Дано число в диапазоне от 1_000_000 до 20_000_000.
# Получите список целочисленных делителей этого числа.
from multiprocessing import Pool, cpu_count
from random import randint
from typing import List
from math import sqrt
from time import perf_counter



# Ищем делители в заданном диапазоне
def get_divisors_in_range(args: tuple[int, int, int]) -> List[int]:
    number, start, end = args
    divisors_list = []

    for div in range(start, end): # Перебираем возможные делители
        if number % div == 0:
            divisors_list.append(div)
            if div != number // div:
                divisors_list.append(number // div)

    return divisors_list

# Разбиваем на диапазоны
# Собираем делители, сортируем и удаляем повторы
def get_collection_divisors(number: int) -> List[int]:
    limit = int(sqrt(number)) + 1
    n_processes = cpu_count()
    step = limit // n_processes
    args_ranges = []

    for i in range(n_processes):
        set_start = i * step + 1
        if i == n_processes - 1:
            set_end = limit
        else:
            set_end = (i + 1) * step + 1
        args_ranges.append((number, set_start, set_end))

    with Pool(n_processes) as pool:
        result = pool.map(get_divisors_in_range, args_ranges)

    flat_list = [item for sublist in result for item in sublist]
    unique_sorted = sorted(set(flat_list))
    return unique_sorted

def main(number: int, verbose: bool = False) -> List[int]:
    start = perf_counter()
    result = get_collection_divisors(number)
    end = perf_counter()
    if verbose:
        print(result)
        print(len(result))
        print(f"Time: {end - start:.6f} seconds")
    return result


if __name__ == "__main__":
    num = randint(1_000_000, 20_000_000)
    main(number=4, verbose=True)