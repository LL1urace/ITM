import pytest
from OOP_6.task_6 import Moped, MeansOfTransport



@pytest.fixture
def init_class():
    return Moped("ALPHA RX 11", "Red", 2)


def test_calc_time_valid_data(init_class):
    moped = init_class
    time = moped.calc_time(100, 10)
    assert time == (100 / 10)
    time = moped.calc_time("1200", 5)
    assert time == (1200 / 5)
    time = moped.calc_time(16530.26, "70")
    assert time == (float("16530.26") / 70)


def test_calc_time_invalid_data(init_class):
    moped = init_class
    with pytest.raises((TypeError, ValueError, ZeroDivisionError)):
        assert moped.calc_time("Очень много км.", 10)
        assert moped.calc_time("Очень много км.", "Очень быстро.")
        assert moped.calc_time(None, None)
        assert moped.calc_time(15, 0)
        assert moped.calc_time(0, 0)
