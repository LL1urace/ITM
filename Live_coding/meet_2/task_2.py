# Функция merge_unique(list1: list[int], list2: list[int]) -> list[int]
# объединяет два списка в один без повторяющихся элементов.
#
# Пример:
# merge_unique([1, 2, 3], [3, 4, 5]) → [1, 2, 3, 4, 5]
def merge_unique(list1: list[int], list2: list[int]) -> list[int]:
    for item in list2:
        list1.append(item)
    return list(set(list1))


if __name__ == "__main__":
    print(merge_unique([1, 2, 3], [3, 4, 5]))