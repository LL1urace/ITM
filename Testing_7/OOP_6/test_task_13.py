import pytest
from OOP_6.task_13 import Dog



@pytest.fixture(autouse=True)
def reset_singleton():
    # Сбрасываем синглтон перед каждым тестом
    Dog._Dog__instance = None
    yield
    Dog._Dog__instance = None


def test_singleton_behavior():
    dog1 = Dog.get_instance("Шарик", "Дворняжка", "Пятнистый", 1, "Самец")
    dog2 = Dog.get_instance("Лаки", "Хаски", "Белый", 2, "Самка")
    assert dog1 is dog2, "Должен быть один экземпляр (Singleton)"
    # Аргументы второго вызова игнорируются, так как объект уже создан
    assert dog1.nickname == "Шарик"


def test_bark(capsys):
    dog = Dog.get_instance("Тузик", "Пудель", "Белый", 3, "Самец")
    dog.bark()
    captured = capsys.readouterr()

    assert "Тузик: Гав-гав!" in captured.out

@pytest.mark.parametrize("food,energy,expected_energy", [
    ("Корм", 10, 100),
    ("Мясо", 5.5, 100),
])
def test_eat_valid(food, energy, expected_energy, capsys):
    dog = Dog.get_instance("Барбос", "Бигль", "Коричневый", 5, "Самец", energy_level=90)
    dog.energy_level = 90  # ставим 90, чтобы проверить рост энергии
    dog.eat(food, energy)
    captured = capsys.readouterr()
    assert f"\"Барбос\" съел(a) \"{food}\"" in captured.out
    assert dog.energy_level <= dog.energy_limit
    assert not dog.is_hungry


@pytest.mark.parametrize("food,energy,exception", [
    ("", 10, ValueError),
    ("Корм", -5, ValueError),
    ("Корм", "много", TypeError),
])
def test_eat_invalid(food, energy, exception):
    dog = Dog.get_instance("Рэкс", "Доберман", "Чёрный", 4, "Самец")
    with pytest.raises(exception):
        dog.eat(food, energy)


def test_update_mood_changes(capsys):
    dog = Dog.get_instance("Шарик", "Дворняжка", "Пятнистый", 1, "Самец")
    dog.health_level = 20
    dog.energy_level = 20
    dog.update_mood()
    captured = capsys.readouterr()
    assert "теперь имеет" in captured.out


def test_sleep_increases_energy(capsys):
    dog = Dog.get_instance("Бим", "Хаски", "Серый", 3, "Самец", energy_level=50)
    dog.sleep(3)
    captured = capsys.readouterr()
    assert "поспал(a) \"3\"" in captured.out
    assert dog.energy_level > 50


def test_sleep_invalid_values():
    dog = Dog.get_instance("Лаки", "Бульдог", "Рыжий", 2, "Самец")
    with pytest.raises(TypeError):
        dog.sleep("два")
    with pytest.raises(ValueError):
        dog.sleep(0)


def test_play_decreases_energy(capsys):
    dog = Dog.get_instance("Рэкс", "Овчарка", "Чёрный", 4, "Самец", energy_level=20)
    dog.play()
    captured = capsys.readouterr()
    assert "поиграл(а)" in captured.out
    assert dog.energy_level == 5  # 20 - 15 = 5


def test_play_no_energy(capsys):
    dog = Dog.get_instance("Тузик", "Пудель", "Белый", 3, "Самец", energy_level=0)
    dog.play()
    captured = capsys.readouterr()
    assert "не может играть" in captured.out


@pytest.mark.parametrize("location", Dog.LOCATIONS)
def test_change_location_valid(location, capsys):
    dog = Dog.get_instance("Бобик", "Лабрадор", "Чёрный", 3, "Самец")
    dog.change_location(location)
    captured = capsys.readouterr()
    assert location in captured.out
    assert dog.location == location


def test_change_location_invalid():
    dog = Dog.get_instance("Бобик", "Лабрадор", "Чёрный", 3, "Самец")
    with pytest.raises(TypeError):
        dog.change_location("")
    with pytest.raises(ValueError):
        dog.change_location("Космос")


def test_get_older_updates(capsys):
    dog = Dog.get_instance("Шарик", "Дворняжка", "Пятнистый", 1, "Самец",
                           health_level=100, energy_level=100)
    old_health_limit = dog.health_limit
    old_energy_limit = dog.energy_limit
    dog.get_older(1)
    captured = capsys.readouterr()
    assert f"\"Шарик\" уже прожил(а) \"{dog.age}\" лет!" in captured.out
    assert dog.health_limit < old_health_limit
    assert dog.energy_limit < old_energy_limit


def test_get_older_invalid():
    dog = Dog.get_instance("Шарик", "Дворняжка", "Пятнистый", 1, "Самец")
    with pytest.raises(TypeError):
        dog.get_older("один")
    with pytest.raises(ValueError):
        dog.get_older(0)