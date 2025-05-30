import pytest
from OOP_6.task_14 import People



def test_init():
    p = People(["Аня", "Борис"])
    assert p.people_list == ["Аня", "Борис"]


def test_add_people_str():
    p = People([])
    p.add_people("Вася")
    assert p.people_list == ["Вася"]


def test_add_people_list():
    p = People([])
    p.add_people(["Петя", "Маша"])
    assert p.people_list == ["Петя", "Маша"]


def test_add_people_empty_list():
    p = People([])
    with pytest.raises(TypeError):
        p.add_people([])  # пустой список — ошибка


def test_add_people_invalid_type():
    p = People([])
    with pytest.raises(TypeError):
        p.add_people([123])  # не строка в списке — ошибка
    with pytest.raises(TypeError):
        p.add_people(123)  # не строка и не список — ошибка


def test_iteration():
    names = ["Аня", "Борис", "Вася"]
    p = People(names)
    result = [person for person in p]
    assert result == names


def test_str():
    p = People(["Аня", "Борис"])
    assert str(p) == "People: Аня,Борис.\n"