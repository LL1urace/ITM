# Практика
# Часть 4. Списки

# 1. Используя операции индексирования и среза выведите на экран первый и третий элементы списка
# [1, 2, 3, 4, 5], а также срез списка из первых трех элементов.
def get_first_item(l: list) -> int:
    return l[0]

def get_third_item(l: list) -> int:
    return l[2]

def get_slice_items(l: list, start: int = 0, end: int = None) -> list:
    return l[start:end]



if __name__ == "__main__":
    L = [1, 2, 3 ,4 ,5]
    print(get_first_item(L))
    print(get_third_item(L))
    print(get_slice_items(L, 0, 4))