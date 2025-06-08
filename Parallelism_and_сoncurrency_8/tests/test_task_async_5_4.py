# Практика:
#
# 5. Перекройте тестами выше указанные задачи.
import asyncio

import pytest
import aiofiles
import aiohttp
from unittest.mock import AsyncMock, patch
from Parallelism_and_сoncurrency_8 import task_async_4



# Task №4 (write_response, limited_fetch, main)
# write_response
@pytest.mark.asyncio
@pytest.mark.parametrize("data", ["stroka1", "stroka2", "file"])
async def test_write_response(data, tmp_path):
    tmp_folder = tmp_path / "files_task4"
    tmp_folder.mkdir()
    await task_async_4.write_response(data, str(tmp_folder))
    expected_file = tmp_folder / "responses.txt"
    assert expected_file.exists()

    async with aiofiles.open(expected_file, encoding='utf-8') as f:
        text = await f.read()
        assert text == str(data + '\n')


# limited_fetch
@pytest.mark.asyncio
async def test_limited_fetch():
    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.__aenter__.return_value = mock_response

    mock_session = AsyncMock(spec=aiohttp.ClientSession)
    mock_session.get.return_value = mock_response

    with patch("Parallelism_and_сoncurrency_8.task_async_4.write_response",
               new_callable=AsyncMock) as mock_write_response:
        test_url = "https://example.com"
        semaphore = asyncio.Semaphore(1)
        await task_async_4.limited_fetch(test_url, mock_session, semaphore)

        mock_session.get.assert_called_once_with(test_url)
        args, _ = mock_write_response.call_args
        assert test_url in args[0]
        assert "200" in args[0]



# main
# Стандартная работа main
async def test_main_task_4():
    pass