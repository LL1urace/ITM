# inheritance_examples.py

# === Обычное наследование с вызовом конструктора родителя напрямую ===
class Parent:
    def __init__(self):
        self.parent_attribute = "I am a parent"

    @staticmethod
    def parent_method():
        # Метод родителя, возвращающий строку
        return "Back in my day"

class ChildUsingParentInit(Parent):
    def __init__(self):
        # Вызов конструктора родителя напрямую
        Parent.__init__(self)
        self.child_attribute = "I am a child"


# === Обычное наследование, но с использованием super() ===
class ChildUsingSuper(Parent):
    def __init__(self):
        # Вызов конструктора родителя через super()
        super().__init__()
        self.child_attribute = "I am a child"


# === Множественное наследование без super(), классы B и C ===
class B:
    def b(self):
        return "b"

class C:
    def c(self):
        return "c"

class D(B, C):
    def d(self):
        return "d"


# === Порядок разрешения методов (Method Resolution Order, MRO) ===
class BX:
    def x(self):
        return "x: B"

class CX:
    def x(self):
        return "x: C"

class DX(BX, CX):
    # Наследует от BX и CX, x() будет вызываться из BX (согласно MRO)
    pass


# === Пример с проблемой алмаза и super() ===

# Первый базовый класс, разбивает текст на токены
class Tokenizer:
    def __init__(self, text):
        self.tokens = text.split()

# Подсчет количества слов (наследует Tokenizer)
class WordCounter(Tokenizer):
    def __init__(self, text):
        super().__init__(text)  # вызывает Tokenizer
        self.word_count = len(self.tokens)

# Подсчет уникальных слов (наследует Tokenizer)
class Vocabulary(Tokenizer):
    def __init__(self, text):
        super().__init__(text)  # вызывает Tokenizer
        self.vocab = set(self.tokens)

# Класс, объединяющий WordCounter и Vocabulary
class TextDescriber(WordCounter, Vocabulary):
    def __init__(self, text):
        # Вызовет только один раз Tokenizer через цепочку MRO
        super().__init__(text)

# Функция, возвращающая словарь с результатами для тестирования
def get_text_describer_data(text):
    td = TextDescriber(text)
    return {
        "tokens": td.tokens,           # Список слов
        "vocab": td.vocab,             # Уникальные слова
        "word_count": td.word_count,   # Количество слов
        "mro": TextDescriber.__mro__   # Порядок разрешения методов
    }
