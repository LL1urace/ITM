import pytest
from For_and_While_cycles_3.task_8 import output_sum_hundred_range



def test_output_sum_hundred_range():
    assert output_sum_hundred_range() == 5050
    assert output_sum_hundred_range() == sum(list(range(1,101)))