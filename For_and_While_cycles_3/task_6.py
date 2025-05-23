# Практика:

# 6. Создайте список с разными значениями, пройдитесь по нему в цикле и выведите на экран.
# (Сделайте то же самое со словарем и выведите ключ и значение)
from typing import List, Tuple

def output_list_dict() -> Tuple[List[str], List[str]]:
    """Возвращает значения массива и словаря в виде списков строк."""
    list_items = ["item1", "item2", "item3", "item4", "item5"]
    dict_items = {1: "item1", 2: "item2", 3: "item3", 4: "item4", 5: "item5"}

    list_output = [f"LIST: {item}" for item in list_items]
    dict_output = [f"DICT: {key} {value}" for key, value in dict_items.items()]

    return list_output, dict_output


if __name__ == "__main__":
    l, d = output_list_dict()
    for item in l:
        print(item)

    for item in d:
        print(item)