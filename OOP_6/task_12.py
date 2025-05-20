# Практика

# 12. Прочитайте статью и выполните действия, которые в ней прописаны
# https://pythonist.ru/vvedenie-v-mnozhestvennoe-nasledovanie-i-super/

# 1) // Краткий обзор наследования
# class Parent:
#     def __init__(self):
#         self.parent_attribute = "I am a parent"
#
#     @staticmethod
#     def parent_method() -> None:
#         print("Back in my day")
#
# class Child(Parent):
#     def __init__(self):
#         Parent.__init__(self)
#         self.child_attribute = "I am a child"
#


# if __name__ == "__main__":
    # child = Child()
    #
    # print(child.child_attribute)
    # print(child.parent_attribute)
    # child.parent_method()



# 2) как 1), но с ипользованием super() // Введение в super()
# class Parent:
#     def __init__(self):
#         self.parent_attribute = "I am a parent"
#
#     @staticmethod
#     def parent_method() -> None:
#         print("Back in my day")
#
# class Child(Parent):
#     def __init__(self):
#         super().__init__()
#         self.child_attribute = "I am a child"
#


# if __name__ == "__main__":
    # child = Child()
    #
    # print(child.child_attribute)
    # print(child.parent_attribute)
    # child.parent_method()



# 3) // Множественное наследование без super()
# class B:
#     def b(self):
#         print("b")
#
#
# class C:
#     def c(self):
#         print("c")
#
#
# class D(B, C):
#     def d(self):
#         print("d")
#
#
# d = D()
# d.b()
# d.c()
# d.d()



# 4) // Порядок разрешения методов
# class B:
#     def x(self):
#         print("x: B")
#
#
# class C:
#     def x(self):
#         print("x: C")
#
#
# class D(B, C):
#     pass
#



# if __name__ == "__main__":
    # d = D()
    # d.x()
    # print(D.mro()) # multiple-resolution order



# 5) // Множественное наследование, super() и проблема алмаза
class Tokenizer:
    """Tokenizer text"""
    def __init__(self, text):
        print("Start Tokenizer.__init__()")
        self.tokens = text.split()
        print("End Tokenizer.__init__()")


class WordCounter(Tokenizer):
    """Count words in text"""
    def __init__(self, text):
        print("Start WordCounter.__init__()")
        super().__init__(text)
        self.word_count = len(self.tokens)
        print("End WordCounter.__init__()")


class Vocabulary(Tokenizer):
    """Find unique words in text"""
    def __init__(self, text):
        print("Start init Vocabulary.__init__()")
        super().__init__(text)
        self.vocab = set(self.tokens)
        print("End init Vocabulary.__init__()")


class TextDescriber(WordCounter, Vocabulary):
    """Describe text with multiple metrics"""
    def __init__(self, text):
        print("Start init TextDescriber.__init__()")
        super().__init__(text)
        print("End init TextDescriber.__init__()")


if __name__ == "__main__":
    td = TextDescriber("row row row your boat")
    print("--------")
    print(td.tokens)
    print(td.vocab)
    print(td.word_count)
    print(TextDescriber.__mro__) # Смотрим порядок вызовов

# super() не обращается напрямую к родителю, а ищет следующий класс в цепочке MRO (Method Resolution Order).
# Благодаря этому каждый метод вызывается только один раз, даже если он есть в нескольких ветках.