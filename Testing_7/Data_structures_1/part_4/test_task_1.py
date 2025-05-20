import pytest
from Data_structures_1.part_4.task_1 import get_first_item, get_third_item, get_slice_items  # Замените на актуальный путь


# --- get_first_item ---
def test_get_first_item_normal():
    assert get_first_item([10, 20, 30]) == 10

def test_get_first_item_empty_list():
    with pytest.raises(IndexError):
        get_first_item([])


# --- get_third_item ---
def test_get_third_item_normal():
    assert get_third_item([5, 6, 7, 8]) == 7

def test_get_third_item_short_list():
    with pytest.raises(IndexError):
        get_third_item([1])


# --- get_slice_items ---
def test_get_slice_items_full():
    assert get_slice_items([1, 2, 3, 4, 5], 1, 4) == [2, 3, 4]

def test_get_slice_items_default_args():
    assert get_slice_items([1, 2, 3]) == [1, 2, 3]

def test_get_slice_items_to_end():
    assert get_slice_items([1, 2, 3, 4], 2) == [3, 4]

def test_get_slice_items_empty_result():
    assert get_slice_items([1, 2, 3], 3, 3) == []

def test_get_slice_items_out_of_bounds():
    assert get_slice_items([1, 2, 3], 0, 10) == [1, 2, 3]
