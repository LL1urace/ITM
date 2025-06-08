# Практика:
#
# 5. Перекройте тестами выше указанные задачи.
import asyncio
import time
import aiohttp
import aiolimiter
import pytest
from unittest.mock import AsyncMock, patch
from Parallelism_and_сoncurrency_8 import task_async_3



# Task №3 (limited_fetch, main)
# limited_fetch
@pytest.mark.asyncio
async def test_limited_fetch():
    test_url = "http://example.com"
    mock_response = AsyncMock()
    mock_response.status = 200
    mock_response.text = AsyncMock(return_value = "response_body")

    mock_session = AsyncMock(spec=aiohttp.ClientSession)
    mock_session.get.return_value.__aenter__.return_value = mock_response

    limiter = aiolimiter.AsyncLimiter(10, 1)
    result = await task_async_3.limited_fetch(test_url, mock_session, limiter)
    assert "200" in result
    assert "response_body" not in result
    assert result.endswith(f"{len(mock_response.text.return_value)} bytes")


# main
# Стандартная работа main
times_call_list = []

@pytest.mark.asyncio
async def test_main_task_3():
    times_call_list.clear()
    async def mock_limited_fetch(url: str,
                                 session: aiohttp.ClientSession,
                                 limiter: aiolimiter.AsyncLimiter) -> str:
        times_call_list.append(time.perf_counter())
        await asyncio.sleep(0.01)
        return "mock"

    with patch("Parallelism_and_сoncurrency_8.task_async_3.limited_fetch",
               side_effect=mock_limited_fetch):
        await task_async_3.main()

    assert len(times_call_list) == 10
    duration = max(times_call_list) - min(times_call_list)
    assert duration <= 0.0001
    for i, t in enumerate(times_call_list):
        count = sum(1 for x in times_call_list if t <= x < t + 1)
        assert count <= 10