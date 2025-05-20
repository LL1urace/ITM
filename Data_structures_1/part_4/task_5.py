# Практика
# Часть 4. Списки

# 5. Преобразуйте список [«a», «s», «1», «a», «32», «23»] в set и выведите на экран. Что изменилось?
from typing import Union

def get_set_of_list(list: list[Union[str, int]]) -> set[Union[str, int]]:
    return set(list)



if __name__ == "__main__":
    L = ["a", "s", "1", "a", "32", "23"]
    # L = [1, 32, 23, 356, 123, 22, 99]
    my_set = get_set_of_list(L)
    print(my_set)