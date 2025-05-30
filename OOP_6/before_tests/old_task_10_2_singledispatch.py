# Практика

# 10. Реализуйте класс Calculator, в котором будет один метод, для вычисления суммы двух чисел.
# Реализуйте еще один класс, который будет наследоваться от класса Calculator и перегрузите метод для вычисления
# суммы двух чисел, чтобы он делал конкатенацию двух строк.

# TO DO Переделать с singledispatсh
from functools import singledispatchmethod
from typing import Union

class Calculator:
    """Класс для вычисления суммы двух чисел."""

    @singledispatchmethod
    def addition(self, a: Union[float, str], b: Union[float, str]) -> Union[float, str]:
        """Выбрасывает исключение если ни одна другая перегрузка функции не подходит."""
        raise TypeError(f"Неподдерживаемый тип аргументов {type(a)} и {type(b)}!")

    @addition.register(int)
    @addition.register(float)
    def _(self, num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
        """Выбрасывает исключение если ни одна другая функция с таким же именем не подходит."""
        try:
            return num1 + num2
        except TypeError:
            raise TypeError(f"Неподдерживаемый тип аргументов {type(num1)} и {type(num2)}!")

    @addition.register(str)
    def _(self, str1: str, str2: str) -> str:
        """Соединяет две строки."""
        try:
            return str1 + str2
        except TypeError:
            raise TypeError(f"Неподдерживаемый тип аргументов {type(str1)} и {type(str2)}!")



# Пример использования:
calc = Calculator()
print(calc.addition(4, 3))  # 8
print(calc.addition("5", "3"))  # 53
print(calc.addition(4, "3"))  # Исключение в перегруженном методе @method_name.register
print(calc.addition([1,2,3], "3"))  # Исключение из базового @singledispatch