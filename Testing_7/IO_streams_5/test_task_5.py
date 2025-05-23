import os
import pytest
import asyncio
from IO_streams_5.task_5 import (
    demo_open_many_files_without_closing,
    demo_open_many_files_with_closing,
    demo_write_with_context_manager,
    demo_many_opens_with_context_manager,
    demo_write_after_context_error,
    demo_write_closed_file_error,
    demo_with_non_context_object,
    list_current_directory_files,
    demo_threading_lock_with_context,
    fetch_python_org,
)


@pytest.fixture
def test_file_path(tmp_path):
    # Путь для временного файла, чтобы не писать в реальные папки
    return tmp_path / "passwords.txt"


def test_demo_open_many_files_without_closing(test_file_path):
    # Эта функция вызовет ошибку при большом количестве открытий,
    # но для теста можно вызвать с меньшим циклом (если можно модифицировать функцию)
    # Иначе проверяем, что при вызове она бросает ошибку.
    with pytest.raises(OSError):
        demo_open_many_files_without_closing()


def test_demo_open_many_files_with_closing(test_file_path):
    result = demo_open_many_files_with_closing()
    assert result == "OK"


def test_demo_write_with_context_manager(test_file_path):
    # Перехватим путь внутри функции, если там хардкод
    test_file = test_file_path / "passwords.txt"
    result = demo_write_with_context_manager(str(test_file))
    assert result == "Written successfully"
    content = test_file.read_text(encoding="utf-8")
    assert "hello" in content


def test_demo_many_opens_with_context_manager():
    result = demo_many_opens_with_context_manager()
    assert result == "OK"


def test_demo_write_after_context_error():
    result = demo_write_after_context_error()
    assert result.startswith("Error:")


def test_demo_write_closed_file_error():
    result = demo_write_closed_file_error()
    assert result.startswith("Error:")


def test_demo_with_non_context_object():
    result = demo_with_non_context_object()
    assert result.startswith("Error:")


def test_list_current_directory_files():
    result = list_current_directory_files()
    assert isinstance(result, list)
    assert all(isinstance(t, tuple) and len(t) == 2 for t in result)


def test_demo_threading_lock_with_context():
    result = demo_threading_lock_with_context()
    assert result == "Lock acquired and released"


@pytest.mark.asyncio
async def test_fetch_python_org():
    status, content_type, html_preview = await fetch_python_org()
    assert status == 200
    assert "text/html" in content_type
    assert isinstance(html_preview, str)
    assert len(html_preview) > 0