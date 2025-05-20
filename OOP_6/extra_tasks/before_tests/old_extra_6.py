# Практика
#
# 1. Посмотрите первые 21 видео про ООП на python (21/21)
# 1.6. Повторить код из видео 18
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = list(marks)

    def __getitem__(self, item):
        if 0 <= item <= len(self.marks):
            return self.marks[item]
        else:
            raise IndexError("Неверный индекс!")

    def __setitem__(self, key, value):
        if not isinstance(key, int) or key < 0:
            raise TypeError("Индекс должен быть целым положительным числом!")

        if key >= len(self.marks):
            off = key + 1 - len(self.marks)
            self.marks.extend(off*[None])

        self.marks[key] = value

    def __delitem__(self, key):
        if not isinstance(key, int):
            raise TypeError("Индекс должен быть целым положительным числом!")

        del self.marks[key]





s1 = Student("Сергей", [1, 2, 3, 4, 5,])
print(s1[2])
s1[10] = 4
print(s1.marks)
del s1[2]
print(s1.marks)