# Практика
#
# 1. Посмотрите первые 21 видео про ООП на python (21/21)
# 1.2. Повторить код из видео 11
class ReadIntX: # Дескриптор не данных
    def __set_name__(self, owner, name):
        self.name = "_x"

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Integer: # Дескриптор данных
    @classmethod
    def verify_coord(cls, coord):
        if not isinstance(coord, int):
            raise TypeError("Координата должна быть целым числом!")

    def __set_name__(self, owner, name):
        self.name = "_" + name

    def __get__(self, instance, owner):
        # return instance.__dict__[self.name]
        return getattr(instance, self.name)

    def __set__(self, instance, value):
        self.verify_coord(value)
        print(f"__set__: {self.name} = {value}")
        # instance.__dict__[self.name] = value
        setattr(instance, self.name, value)



class Point3D:
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


if __name__ == "__main__":
    p = Point3D(1, 2, 3)
    p.xr = 6 # Создание локального свойства экземпляра
    print(p.__dict__, p.xr) # Найдет локальное свойство, так как приоритет выше чем у non-data descriptor
    #Если бы был просто дескриптор, то нашло бы значение дескриптора потому что у него выше приоритет