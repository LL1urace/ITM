import pytest
from faker import Faker
from Data_structures_1.part_1.task_5 import get_cube_volume_area



faker: Faker = Faker()

# Тест на случайные правильные значения
def test_get_cube_volume_area_valid_input():
    edge = faker.pyfloat(positive=True)
    assert get_cube_volume_area(edge) == (edge ** 3, 6 * edge ** 2)


# Тест на случайные неправильные значения
@pytest.mark.parametrize("edge",
                        [
                            faker.pyfloat(positive=False),
                            faker.word(),
                            None,
                            [],
                            "",
                            {},
                            (),
                            # float(True), считает что 1 и норм проходит
                            float(False),
                            0
                        ])
def test_get_cube_volume_area_invalid_input(edge):
    with pytest.raises((TypeError, ValueError)):
        get_cube_volume_area(edge)