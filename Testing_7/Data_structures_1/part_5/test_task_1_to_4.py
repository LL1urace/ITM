import pytest
from Data_structures_1.part_5.task_1_to_4 import (
    get_person_data,
    set_person_value,
    del_person_value,
    person
)

@pytest.fixture(autouse=True)
def reset_person():
    person.clear()
    person.update({
        "name": "Даниил",
        "age": 22,
        "sex": "M",
        "height": 200,
        "weight": 110,
        "foot_size": 50
    })

def test_get_person_data_existing():
    assert get_person_data("name", "sex") == ["name", "sex"]

def test_get_person_data_with_missing():
    assert get_person_data("name", "hobby", "weight") == ["name", "weight"]

def test_set_person_value():
    set_person_value("foot_size", 42)
    assert person["foot_size"] == 42

def test_del_person_value():
    del_person_value()
    assert "age" not in person

