import pytest
from For_and_While_cycles_3.task_3 import average_nums_of_list



def test_average_with_zero_in_middle():
    assert average_nums_of_list([1, 2, 0, 4, 5]) == pytest.approx(1.5)

def test_average_with_zero_at_start():
    assert average_nums_of_list([0, 1, 2]) is None

def test_average_with_no_zero():
    assert average_nums_of_list([1, 2, 3]) == pytest.approx(2.0)

def test_average_with_strings():
    assert average_nums_of_list(['3', '5', '0', '7']) == pytest.approx(4.0)

def test_empty_list():
    assert average_nums_of_list([]) is None

def test_invalid_string_raises_value_error():
    with pytest.raises(ValueError):
        average_nums_of_list(['a', 'b'])

def test_invalid_type_raises_type_error():
    with pytest.raises(TypeError):
        average_nums_of_list([1, 2, None])

def test_zero_as_float():
    assert average_nums_of_list([1.0, 0.0, 3]) == pytest.approx(1.0)

def test_multiple_zeros():
    assert average_nums_of_list([1, 2, 0, 0, 5]) == pytest.approx(1.5)