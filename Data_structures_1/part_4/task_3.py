# Практика
# Часть 4. Списки

# 3. Дан список [«a», «s», «1», «a», «32», «23»].
# Разбейте его на два списка: только с буквами и только с числами.
from typing import Union

def divide_list_on_num_letters(l: list[Union[str, int]]) -> tuple[list[str], list[int]]:
    letters = []
    digits = []
    for item in l:
        if isinstance(item, str):
            if item.isalpha():
                if len(item) > 1:
                    letters.extend(list(item))
                else:
                    letters.append(item)
            elif item.isdigit():
                digits.append(int(item))
        elif isinstance(item, int):
            digits.append(item)
    return letters, digits


if __name__ == "__main__":
    #L = ["a", "s", "1", "a", "32", "23"]
    # L = [None, "s", "1", "a", "32", "23"]
    L = [None, 1.5, "abc123", True, False, [], {}, "", "   "]
    letters, digits = divide_list_on_num_letters(L)
    print(letters)
    print(digits)