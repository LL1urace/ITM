# Практика
#
# 1. Посмотрите первые 21 видео про ООП на python (21/21)
# 1.3. Повторить код из видео 12
# class Counter:
#     def __init__(self):
#         self.__counter = 0
#
#     # Классы, которые можно вызывать как функции - Функторы
#     def __call__(self, step=1, *args, **kwargs):
#         print("__call__")
#         self.__counter += step
#         return self.__counter
#
#
# c = Counter()
# c2 = Counter()
# c() # Нельзя вызывать класс как функцию если не определен __call__
# c(2)
# res = c(10)
# res2 = c2(-5)
# print(res, res2)


# class StripChars:
#     def __init__(self, chars):
#         self.__counter = 0
#         self.__chars = chars
#
#     def __call__(self, *args, **kwargs):
#         if not isinstance(args[0], str):
#             raise TypeError("Аргумент должен быть строкой!")
#
#         return args[0].strip(self.__chars)
#
#
# s1 = StripChars("?:.; ")
# s2 = StripChars("!")
# res = s1(" Hello World! !")
# res2 = s2(" Hello World! !")
# print(res, res2, sep='\n')


import math


class Derivate:
    def __init__(self, func):
        self.__fn = func

    def __call__(self, x, dx=0.0001, *args, **kwargs):
        return (self.__fn(x + dx) - self.__fn(x)) / dx

@Derivate # Стандартный декоратор
def df_sin(x):
    return math.sin(x)


# df_sin = Derivate(df_sin) Прямой способ задать декоратор
print(df_sin(math.pi/3))