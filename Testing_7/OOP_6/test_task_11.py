import pytest
from OOP_6.task_11 import Cat



def test_voice(capsys):
    cat = Cat()
    cat.voice()
    check_out = capsys.readouterr()
    assert check_out.out.strip() == "Мяу!"