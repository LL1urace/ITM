# Практика:

# 3. Напишите программу для подсчета среднего числа всех введенных пользователем чисел.
# Ввод пользователя должен осуществляться с помощью input.
# Если пользователь вводит ноль, то выводиться на экран среднее значение.
# Используйте цикл while для решения данной задачи
from typing import List, Union, Optional


def average_nums_of_list(nums: List[Union[float, int]]) -> Optional[float]:
    """Вычисление среднего значения списка чисел"""
    processed_nums = []
    for n in nums:
        # Преобразуем к float, если нужно
        if isinstance(n, (int, float)):
            val = float(n)
        elif isinstance(n, str):
            try:
                val = float(n)
            except ValueError:
                raise ValueError(f"Невозможно преобразовать значение '{n}' в число")
        else:
            raise TypeError(f"Некорректное значение в списке: {n} (тип {type(n)})")
        # Если встретился ноль — прерываем цикл
        if val == 0:
            break
        processed_nums.append(val)
    if not processed_nums:
        return None
    return sum(processed_nums) / len(processed_nums)


if __name__ == "__main__":
    print(average_nums_of_list([1, 2, 3, 0]))