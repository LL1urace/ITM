import pytest
from For_and_While_cycles_3.task_13 import find_factorial



def test_find_factorial():
    f_vals = find_factorial()
    assert f_vals[0] == "Значение: 1 Факториал: 1"
    assert f_vals[1] == "Значение: 2 Факториал: 2"
    assert f_vals[2] == "Значение: 3 Факториал: 6"
    assert f_vals[3] == "Значение: 4 Факториал: 24"
    assert f_vals[4] == "Значение: 5 Факториал: 120"