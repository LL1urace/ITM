import pytest
from IO_streams_5.task_2 import file_read
import io



def test_file_read(monkeypatch):
    fake_content = "тестовый текст"
    fake_file = io.StringIO(fake_content)
    monkeypatch.setattr("builtins.open", lambda *args, **kwargs: fake_file)
    content = file_read()
    assert content == fake_content



def test_file_read():
    expected_content = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum\n"
    content = file_read()
    assert content == expected_content