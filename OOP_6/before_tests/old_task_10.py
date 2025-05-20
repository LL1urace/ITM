# Практика

# 10. Реализуйте класс Calculator, в котором будет один метод, для вычисления суммы двух чисел.
# Реализуйте еще один класс, который будет наследоваться от класса Calculator и перегрузите метод для вычисления
# суммы двух чисел, чтобы он делал конкатенацию двух строк.
class Calculator:
    """Класс для вычисления суммы двух чисел."""

    def addition(self, num1: float, num2: float) -> float:
        """Складывает два числа."""
        return num1 + num2


class StrCalculator(Calculator):
    """Класс для конкатенации строк (наследуется от Calculator)."""

    def addition(self, str1: str, str2: str) -> str:
        """Соединяет две строки."""
        return str1 + str2


# Пример использования:
calc = Calculator()
print(calc.addition(5, 3))  # 8

str_calc = StrCalculator()
print(str_calc.addition("Hello, ", "world!"))  # "Hello, world!"