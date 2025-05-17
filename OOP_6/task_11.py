# Практика

# 11. Реализуйте абстрактный класс Animals, создайте класс Cat, который будет
# наследоваться от класса Animals и реализуйте метод voice.
from abc import ABC, abstractmethod

class Animals(ABC):
    """Абстрактный класс, представляющий сущность животного."""

    @abstractmethod
    def voice(self) -> None:
        """Абстрактный метод, который должен возвращать звук животного."""
        pass

class Cat(Animals):
    """Класс-наследник Animals, представляющий кота."""

    def __init__(self):
        super().__init__()

    def voice(self) -> None:
        """Переопределение абстрактного метода, для возвращения звука кота."""
        print("Мяу!")



cat = Cat()
cat.voice()