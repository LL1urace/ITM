# Практика

# 9. Реализуйте все возможные магические методы в классе Car.
import copy
from typing import Union

class Car:
    def __init__(self, make: str, model: str, year: int,
                 color: str, fuel_type: str, tank_capacity: float,
                 current_fuel_level: float, number_of_doors: int,
                 mileage: float, max_speed: float, owner: str, price: float):
        """Создает экземпляр класса Car."""
        self.__make = make # Марка
        self.__model = model # Модель
        self.__year = year # Год
        self.__color = color # Цвет
        self.__fuel_type = fuel_type # Тип топлива
        self.__tank_capacity = tank_capacity #
        self.__current_fuel_level = current_fuel_level # Уровень топлива сейчас
        self.__number_of_doors = number_of_doors # Количество дверей
        self.__mileage = mileage # Пробег
        self.__max_speed = max_speed # Макс. скорость
        self.__owner = owner # Владелец
        self.__price = price # Цена

    @staticmethod
    def get_attr_map() -> dict:
        return {
            "make": "_Car__make",
            "model": "_Car__model",
            "year": "_Car__year",
            "color": "_Car__color",
            "fuel_type": "_Car__fuel_type",
            "tank_capacity": "_Car__tank_capacity",
            "current_fuel_level": "_Car__current_fuel_level",
            "number_of_doors": "_Car__number_of_doors",
            "mileage": "_Car__mileage",
            "max_speed": "_Car__max_speed",
            "owner": "_Car__owner",
            "price": "_Car__price"
        }

    # Итерации по экземпляру класса (__iter__, __next__)
    def __iter__(self):
        self.iter_index = 0
        self.iter_values = [
            self.__make, self.__model, self.__year, self.__color,
            self.__fuel_type, self.__tank_capacity, self.__current_fuel_level,
            self.__number_of_doors, self.__mileage, self.__max_speed,
            self.__owner, self.__price
        ]
        return self


    def __next__(self):
        if self.iter_index < len(self.iter_values):
            value = self.iter_values[self.iter_index]
            self.iter_index += 1
            return value
        else:
            raise StopIteration


    # Работа как с массивом (__getitem__, __setitem__ __delitem__)
    def __getitem__(self, key) -> any:
        attr_map = self.get_attr_map()
        if key in attr_map:
            return getattr(self, attr_map[key])
        else:
            raise KeyError(f"Не существует атрибута с ключом '{key}'")


    def __setitem__(self, key, value) -> None:
        attr_map = self.get_attr_map()
        if key in attr_map:
            setattr(self, attr_map[key], value)
        else:
            raise KeyError(f"Невозможно установить значение: нет атрибута с ключом '{key}'")


    def __delitem__(self, key) -> None:
        attr_map = self.get_attr_map()
        if key in attr_map:
            delattr(self, attr_map[key])
        else:
            raise KeyError(f"Невозможно удалить: нет атрибута с ключом '{key}'")


    # Работа с контекстным менеджером (__enter__, __exit__)
    def __enter__(self) -> 'Car':
        self._start_mileage = self.__mileage
        print(f"[INFO] Начало работы с автомобилем: {self.__make} {self.__model} в методе __enter__!")
        return self


    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        distance = self.__mileage - self._start_mileage
        print(f"[INFO] Автомобиль проехал {distance} км.!")
        print(f"[INFO] Завершение работы с автомобилем: {self.__make} {self.__model} в методе __exit__!")


    # Работа как с функцией (__call__)
    def __call__(self, **kwargs):
        attr_map = self.get_attr_map()
        for key, value in kwargs.items():
            if key in attr_map:
                setattr(self, attr_map[key], value)
            else:
                raise KeyError(f"Невозможно установить: нет поля '{key}'")


    # Длина (кол-во дверей) (__len__)
    def __len__(self):
        return self.__number_of_doors


    # Булево значение (пока хз) (__bool__)
    def __bool__(self) -> bool:
        return bool(self.__owner)

    # Арифметические операции (c ценами) (__add__(+), __iadd__(+=), __sub__(-), __isub__(-=)
    # __mul__(*), __imul__(*=), __truediv__(/), __itruediv__(/=), __floordiv__(//), __mod__(%), __pow__(**))
    def __add__(self, other: Union[float, 'Car']) -> 'Car':
        if not isinstance(other, (float, Car)):
            raise ArithmeticError("Арифметические операции можно выполнять только с вещественными числами или экземплярами одного класса!")
        add_value = other
        if isinstance(other, Car):
            add_value = other.__price
        new_car = copy.copy(self)
        new_car.__price = new_car.__price + add_value
        return new_car


    def __radd__(self, other):
        return self + other


    def __iadd__(self, other):
        if not isinstance(other, (float, Car)):
            raise ArithmeticError("Арифметические операции можно выполнять только с вещественными числами или экземплярами одного класса!")
        add_value = other
        if isinstance(other, Car):
            add_value = other.__price
        self.__price = self.__price + add_value
        return self


    def __sub__(self, other: Union[float, 'Car']) -> 'Car':
        if not isinstance(other, (float, Car)):
            raise ArithmeticError("Арифметические операции можно выполнять только с вещественными числами или экземплярами одного класса!")
        sub_value = other
        if isinstance(other, Car):
            sub_value = other.__price
        new_car = copy.copy(self)
        new_car.__price -= sub_value
        return new_car


    def __rsub__(self, other):
        return -self + other


    def __isub__(self, other):
        if not isinstance(other, (float, Car)):
            raise ArithmeticError("Арифметические операции можно выполнять только с вещественными числами или экземплярами одного класса!")
        add_value = other
        if isinstance(other, Car):
            add_value = other.__price
        self.__price = self.__price - add_value
        return self


    def __mul__(self, other: Union[float, 'Car']) -> 'Car':
        if not isinstance(other, (float, Car)):
            raise ArithmeticError("Арифметические операции можно выполнять только с вещественными числами или экземплярами одного класса!")
        mul_value = other
        if isinstance(other, Car):
            mul_value = other.__price
        new_car = copy.copy(self)
        new_car.__price *= mul_value
        return new_car


    def __rmul__(self, other):
        return self * other


    def __imul__(self, other):
        if not isinstance(other, (float, Car)):
            raise ArithmeticError("Арифметические операции можно выполнять только с вещественными числами или экземплярами одного класса!")
        add_value = other
        if isinstance(other, Car):
            add_value = other.__price
        self.__price = self.__price * add_value
        return self


    def __truediv__(self, other: Union[float, 'Car']) -> 'Car':
        if not isinstance(other, (float, Car)):
            raise ArithmeticError("Арифметические операции можно выполнять только с вещественными числами или экземплярами одного класса!")
        div_value = other
        if isinstance(other, Car):
            div_value = other.__price
        new_car = copy.copy(self)
        new_car.__price /= div_value
        return new_car

    def __rtruediv__(self, other):
        return NotImplemented


    def __floordiv__(self, other: Union[float, 'Car']) -> 'Car':
        if not isinstance(other, (float, Car)):
            raise ArithmeticError("Арифметические операции можно выполнять только с вещественными числами или экземплярами одного класса!")
        floor_div_value = other
        if isinstance(other, Car):
            floor_div_value = other.__price
        new_car = copy.copy(self)
        new_car.__price //= floor_div_value
        return new_car

    def __rfloordiv__(self, other):
        return NotImplemented  # Перегрузка целочисленного деления


    def __mod__(self, other: Union[float, 'Car']) -> 'Car':
        if not isinstance(other, (float, Car)):
            raise ArithmeticError("Арифметические операции можно выполнять только с вещественными числами или экземплярами одного класса!")
        mod_value = other
        if isinstance(other, Car):
            mod_value = other.__price
        new_car = copy.copy(self)
        new_car.__price %= mod_value
        return new_car


    def __rmod__(self, other):
        return NotImplemented  # Перегрузка операции остатка


    def __pow__(self, other: Union[float, 'Car'], modulo=None) -> 'Car':
        if not isinstance(other, (float, Car)):
            raise ArithmeticError("Арифметические операции можно выполнять только с вещественными числами или экземплярами одного класса!")
        pow_value = other
        if isinstance(other, Car):
            pow_value = other.__price
        new_car = copy.copy(self)
        new_car.__price **= pow_value
        return new_car


    def __rpow__(self, other):
        return NotImplemented  # Перегрузка для работы с другим типом


    # Операции сравнения (по ценам и году) (__eq__(==), __ne__(!=), __lt__(<),
    # __gt__(>), __le__(<=), __ge__(>=))
    def __eq__(self, other: 'Car') -> bool:
        if not isinstance(other, Car):
            return NotImplemented
        return self.__price == other.__price and self.__year == other.__year


    def __ne__(self, other: 'Car') -> bool: # Необязательный метод
        if not isinstance(other, Car):
            return NotImplemented
        return self.__price != other.__price and self.__year != other.__year


    def __lt__(self, other: 'Car') -> bool:
        if not isinstance(other, Car):
            return NotImplemented
        return self.__price < other.__price and self.__year < other.__year


    def __gt__(self, other: 'Car') -> bool: # Необязательный метод
        if not isinstance(other, Car):
            return NotImplemented
        return self.__price > other.__price and self.__year > other.__year


    def __le__(self, other: 'Car') -> bool:
        if not isinstance(other, Car):
            return NotImplemented
        return self.__price <= other.__price and self.__year <= other.__year


    def __ge__(self, other: 'Car') -> bool: # Необязательный метод
        if not isinstance(other, Car):
            return NotImplemented
        return self.__price >= other.__price and self.__year >= other.__year


    # Строки и вывод (__str__, __repr__, __format__)
    def __str__(self) -> str:
        """Строковое представление объекта для вывода пользователю."""
        return f"{self.__make}, {self.__model}, {self.__year}, {self.__color}, {self.__owner}, {self.__price}"


    def __repr__(self) -> str:
        """Строковое представление объекта для вывода разработчику."""
        return (f"__make = {self.__make},\n__model = {self.__model},\n"
                f"__year = {self.__year},\n__color = {self.__color},\n"
                f"__fuel_type = {self.__fuel_type},\n__tank_capacity = {self.__tank_capacity},\n"
                f"__current_fuel_level = {self.__current_fuel_level},\n__number_of_doors = {self.__number_of_doors},\n"
                f"__mileage = {self.__mileage},\n__max_speed = {self.__max_speed},\n"
                f"__owner{self.__owner},\n__price = {self.__price}")


    def __format__(self, format_spec) -> str:
        """Кастомное форматирование вывода информации о машине."""
        if format_spec == "short_info":
            return f"{self.__make}, {self.__model}"
        elif format_spec == "long_info":
            return f"{self.__make}, {self.__model}, {self.__year}, {self.__color}"
        elif format_spec == "sell_info":
            return f"{self.__make}, {self.__model}, {self.__owner}, {self.__price}"
        else:
            return self.__str__()





if __name__ == "__main__":
    my_car = Car(
        make="Toyota",
        model="Camry",
        year=2020,
        color="Серебристый",
        fuel_type="Бензин",
        tank_capacity=60.0,
        current_fuel_level=30.0,
        number_of_doors=4,
        mileage=45000.0,
        max_speed=210.0,
        owner="Александр Александрович",
        price=1800000.0
    )
    # Вывод строковый
    # print(my_car)
    # print(repr(my_car))

    print(f"{my_car:short_info}")
    print(f"{my_car:long_info}")
    print(f"{my_car:sell_info}")
    print(f"{my_car:bla-bla-bla}")


    # Итерируемся по экземпляру
    # for item in my_car:
    #     print("Итерируемся по экземпляру: ", item)


    # Работа как с массивом (__getitem__, __setitem__ __delitem__)
    # print(my_car["make"])
    # print(my_car["model"])
    # my_car["owner"] = "nobody"
    # print(my_car["owner"])


    # Работа с контекстным менеджером (__enter__, __exit__)
    # with my_car as c:
    #     my_car["mileage"] += 5000.0


    # Работа как с функцией (__call__)
    # my_car(color="Розовый", owner="Кто-то")
    # print(my_car["color"])
    # print(my_car["owner"])


    # Длина (кол-во дверей) (__len__)
    # print(len(my_car))


    # Булево значение (пока хз) (__bool__)
    # print(bool(my_car))
    # my_car["owner"] = None
    # print(bool(my_car))


    # Арифметические операции (сложение цен) (__add__(+), __iadd__(+=), __sub__(-), __isub__(-=)
    # __mul__(*), __imul__(*=), __truediv__(/), __itruediv__(/=), __floordiv__(//), __mod__(%), __pow__(**))
    # my_car2 = copy.copy(my_car)
    # my_car = my_car + my_car2
    # print(my_car['price'])
    #
    # my_car = my_car2 + my_car
    # my_car = my_car2 + 9999.99
    # print(my_car['price'])
    #
    # my_car += 9999.999
    # my_car += my_car2
    # print(my_car['price'])
    #
    # my_car = my_car - my_car2
    # print(my_car['price'])
    # my_car -= my_car2
    # print(my_car['price'])
    #
    # my_car = my_car * 2.0
    # print(my_car['price'])
    #
    # my_car = my_car / 2.0
    # print(my_car['price'])
    #
    # my_car = my_car // 2.0
    # print(my_car['price'])
    #
    # my_car = my_car ** 2.0
    # print(my_car['price'])

    # Операции сравнения (сложение цен) (__eq__(==), __ne__(!=), __lt__(<),
    # __gt__(>), __le__(<=), __ge__(>=))
    # my_car2 = copy.copy(my_car)
    # my_car2['price'] = 2000
    # my_car2['year'] = 2000
    # print(my_car == my_car, "[==]")
    # print(my_car == my_car2, "[==]",end='\n\n')
    #
    # print(my_car != my_car, "[!=]")
    # print(my_car != my_car2, "[!=]",end='\n\n')
    #
    # print(my_car > my_car, "[>]")
    # print(my_car > my_car2, "[>]",end='\n\n')
    #
    # print(my_car < my_car, "[<]")
    # print(my_car < my_car2, "[<]", end='\n\n')
    #
    # print(my_car >= my_car, "[>=]")
    # print(my_car >= my_car2, "[>=]", end='\n\n')
    #
    # print(my_car <= my_car, "[<=]")
    # print(my_car <= my_car2, "[<=]", end='\n\n')