# Практика

# 10. Реализуйте класс Calculator, в котором будет один метод, для вычисления суммы двух чисел.
# Реализуйте еще один класс, который будет наследоваться от класса Calculator и перегрузите метод для вычисления
# суммы двух чисел, чтобы он делал конкатенацию двух строк.

# TO DO Переделать с multipledispatch
from multipledispatch import dispatch
from typing import Union

# multipledispatch сам обрабатывает диспетчеризацию (выбор подходящей версии метода по типам аргументов).
# Если он не находит подходящую сигнатуру, то:
# не вызывает ни одну из функций, и
# выбрасывает NotImplementedError — потому что подходящего варианта метода не реализовано для данных типов.

class Calculator:
    """Класс для вычисления суммы двух чисел."""

    @dispatch(int, int)
    def addition(self, num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
        """Выбрасывает исключение если ни одна другая функция с таким же именем не подходит."""
        return num1 + num2

    @dispatch(float, float)
    def addition(self, num1: Union[int, float], num2: Union[int, float]) -> Union[int, float]:
        """Выбрасывает исключение если ни одна другая функция с таким же именем не подходит."""
        return num1 + num2

    @dispatch(str, str)
    def addition(self, str1: str, str2: str) -> str:
        """Соединяет две строки."""
        return str1 + str2



# Пример использования:
if __name__ == "__main__":
    calc = Calculator()
    print(calc.addition(4, 3))  # 8
    print(calc.addition("5", "3"))  # 53
    # print(calc.addition(4, "3"))  # Исключение в перегруженном методе @method_name.register