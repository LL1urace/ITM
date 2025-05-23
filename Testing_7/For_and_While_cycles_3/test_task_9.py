import pytest
from For_and_While_cycles_3.task_9 import output_multiplication2table



def test_output_multiplication2table():
    table = output_multiplication2table()
    assert table[0] == "2 * 1 = 2"
    assert table[4] == "2 * 5 = 10"
    assert table[6] == "2 * 7 = 14"
    assert table[-1] == "2 * 10 = 20"
    assert table[-3] == "2 * 8 = 16"