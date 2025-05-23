import pytest
from For_and_While_cycles_3.task_6 import output_list_dict



def test_output_list_dict():
    l_out, d_out = output_list_dict()
    assert l_out == [
        "LIST: item1",
        "LIST: item2",
        "LIST: item3",
        "LIST: item4",
        "LIST: item5",
    ]
    assert d_out == [
        "DICT: 1 item1",
        "DICT: 2 item2",
        "DICT: 3 item3",
        "DICT: 4 item4",
        "DICT: 5 item5",
    ]