import pytest
from For_and_While_cycles_3.task_5 import output_multiplication_table



def test_output_multiplication_table():
    table = output_multiplication_table()
    assert table[0] == "0 * 1 = 0"
    assert table[9] == "0 * 10 = 0"
    assert table[10] == " "  # пустая строка после 0-го множителя
    assert table[11] == "1 * 1 = 1"
    assert table[-2] == "9 * 10 = 90"