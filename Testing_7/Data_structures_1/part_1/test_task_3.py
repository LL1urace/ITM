import pytest
from faker import Faker
from Data_structures_1.part_1.task_3 import get_rectangle_area_perimeter



faker: Faker = Faker()

# Тест на случайные правильные значения
def test_get_rectangle_area_perimeter_valid_input():
    height = faker.pyfloat(positive=True)
    width = faker.pyfloat(positive=True)
    assert get_rectangle_area_perimeter(height, width) == (height * width, 2 * (height + width))


# Тест на неправильные значения
@pytest.mark.parametrize(
                        ("height", "width"),
                        [
                            (faker.pyfloat(positive=False), faker.pyfloat(positive=False)),
                            (faker.pyfloat(positive=False), faker.word()),
                            (faker.word(), faker.pyfloat(positive=False)),
                            (faker.word(), faker.word()),
                            (faker.word(), None),
                            (None, faker.word()),
                            (None, None),
                            ([], []),
                            ([], ""),
                            ("", []),
                        ])
def test_get_rectangle_area_perimeter_invalid_input(height, width):
    with pytest.raises((TypeError, ValueError)):
        get_rectangle_area_perimeter(height, width)