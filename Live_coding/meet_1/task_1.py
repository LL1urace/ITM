# 1. Список строк, цифра число инт, вернуть список больше
def func(row_list, count_rows):
    max_list = []
    for item in row_list:
        if len(str(item)) > count_rows:
            max_list.append(item)
    return max_list

if __name__ == "__main__":
    list_Values = ["Строка1", "313", 312, "Антончик", "hi"]
    count = func(list_Values, 3)
    print(count)

