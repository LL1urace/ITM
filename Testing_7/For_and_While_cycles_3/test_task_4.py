import pytest
from For_and_While_cycles_3.task_4 import output_range



def test_output_range():
    result = list(range(101))
    assert output_range() == result