# Практика:

# 6. Создайте список с разными значениями, пройдитесь по нему в цикле и выведите на экран.
# (Сделайте то же самое со словарем и выведите ключ и значение)
def output_list_dict() -> None:
    """Выводит значения массива и словаря."""
    list_items = ["item1", "item2", "item3", "item4", "item5"]
    dict_items = {1: "item1", 2: "item2", 3: "item3", 4: "item4", 5: "item5"}
    for items in list_items:
        print("LIST:", items)
    for key, value in dict_items.items():
        print("DICT:", key, value)


if __name__ == "__main__":
    output_list_dict()