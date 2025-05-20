import pytest
from faker import Faker
from Data_structures_1.part_1.task_6 import get_parallelepiped_volume_area



faker: Faker = Faker()

# Тест на случайные правильные значения
def test_get_parallelepiped_volume_area_valid_input():
    l = faker.pyfloat(positive=True)
    w = faker.pyfloat(positive=True)
    h = faker.pyfloat(positive=True)
    volume, area = get_parallelepiped_volume_area(l, w, h) # == (l * w * h, 2 * (l * w + w * h + l * h))
    assert volume == pytest.approx(l * w * h, rel=1e-6)
    assert area == pytest.approx(2 * (l * w + w * h + l * h), rel=1e-6)

# # Тест на случайные неправильные значения
@pytest.mark.parametrize(
                        ("l", "w", "h"),
                        [
                            (faker.pyfloat(positive=False), faker.pyfloat(positive=False), faker.pyfloat(positive=False)),
                            (faker.word(), faker.word(), faker.word()),
                            (None, None, None),
                            ([], [], []),
                            ("", "", ""),
                            ({}, {}, {}),
                            ((), (), ()),
                            # float(True), считает что 1 и норм проходит
                            (float(False), float(False), float(False)),
                            (0, 0, 0),
                            # Разные аргументы
                            (faker.word(), faker.pyfloat(positive=True), None),
                            (faker.pyfloat(positive=True), faker.pyfloat(positive=True), None),
                            (faker.pyfloat(positive=True), None, faker.pyfloat(positive=True)),
                        ])
def test_get_parallelepiped_volume_area_invalid_input(l, w, h):
    with pytest.raises((TypeError, ValueError)):
        get_parallelepiped_volume_area(l, w, h)