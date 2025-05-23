import pytest
from For_and_While_cycles_3.task_7 import output_range



def test_output_range():
    digits = list(range(3, 101, 3))
    result = output_range()
    assert result == digits