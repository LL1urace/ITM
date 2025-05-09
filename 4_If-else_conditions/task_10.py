# Практика:
# Примечание: Во всех задачах данные должны вводится пользователем,
# это можно реализовать с помощью функции input.
# Например, начинаем выполнять первую задачу из блока If Else:
# first_number = int(input(«Введите первое число»))
# second_number = int(input(«Введите второе число»))
# third_number = int(input(«Введите третье число»))
#
# Switch Case
# 5. Дано целое число в диапазоне 100–999. Вывести строку-описание данного числа,
# например: 256 — «двести пятьдесят шесть», 814 — «восемьсот четырнадцать».
def num_description() -> None:
    """Вывод строки-описания для трехзначного числа"""
    print("Вывод строки-описания для трехзначного числа: ")
    num = input("Введите трехзначное число (100-999): ")
    try:
        num = int(num)
    except ValueError:
        print("Ошибка-ввода: некорректные данные числовых значений")
        return

    hundreds_dict = {1: "сто", 2: "двести", 3: "триста", 4: "четыреста", 5: "пятьсот",
                6: "шестьсот", 7: "семьсот", 8:"восемьсот", 9: "девятьсот"}
    tens_dict = {1: "десять", 2: "двадцать", 3: "тридцать", 4: "сорок", 5: "пятьдесят",
            6: "шестьдесят", 7: "семьдесят", 8: "восемьдесят", 9: "девяносто"}
    teens_dict = {11: "одиннадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать",
             15: "пятнадцать", 16: "шестнадцать", 17: "семнадцать", 18: "восемнадцать", 19: "девятнадцать"}
    ones_dict = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять",
            6: "шесть", 7: "семь", 8: "восемь", 9: "девять"}

    hundreds = num // 100
    teens = (num % 100)
    tens = teens // 10
    ones = teens % 10

    match teens, tens, ones:
        case (teens, _, _) if teens in teens_dict:
            print(f"Введенное число: {hundreds_dict[hundreds]} {teens_dict[teens]}")
        case (_, 0, 0):
            print(f"Введенное число: {hundreds_dict[hundreds]}")
        case (_, tens, 0):
            print(f"Введенное число: {hundreds_dict[hundreds]} {tens_dict[tens]}")
        case (_, 0, ones):
            print(f"Введенное число: {hundreds_dict[hundreds]} {ones_dict[ones]}")
        case (_, tens, ones):
            print(f"Введенное число: {hundreds_dict[hundreds]} {tens_dict[tens]} {ones_dict[ones]}")




num_description()