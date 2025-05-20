# Практика
# Часть 4. Списки

# 4. В предыдущей задаче должен был получиться список из букв.
# Используя методы списков: удалите из него последний элемент, сделайте реверсию списка.
from Data_structures_1.part_4.task_3 import divide_list_on_num_letters

def del_last_and_reverse_list(digits: list[int]) -> list[int]:
    if not all(isinstance(i, int) for i in digits):
        raise ValueError("Список должен содержать только целые числа (int).")

    if not digits:
        return []

    digits.pop()
    digits.reverse()
    return digits



if __name__ == "__main__":
    L = ["a", "s", "1", "a", "32", "23"]
    # L = [1, 32, 23, 356, 123, 22, 99]
    letters, digits = divide_list_on_num_letters(L)
    print(digits)
    digits = del_last_and_reverse_list(digits)
    print(digits)
    # L = [None, "s", "1", "a", "32", "23"]
    # L = [None, 1.5, "abc123", True, False, [], {}, "", "   "]