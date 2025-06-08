# Практика:
#
# 5. Выполните профилирование для определения точек потребления памяти и просадок по времени.
import aiohttp
import asyncio
import aiofiles
import time
import os
from scalene import scalene_profiler




file_lock = asyncio.Lock()

# Task №4
async def write_response(data: str) -> None:
    os.makedirs("files_task4", exist_ok=True)
    async with file_lock:
        async with aiofiles.open(file="files_task4/responses.txt", mode="a") as f:
            await f.write(data + '\n')


async def limited_fetch(url: str,
                      session: aiohttp.ClientSession,
                      semaphore: asyncio.Semaphore) -> None:
        async with semaphore:
            async with session.get(url) as response:
                text = f"[{time.strftime('%X')}] {url} - {response.status}"
                print(text)
                await write_response(text)


async def main(url: str = "https://example.com",
               total_requests: int = 50,
               max_concurrent: int = 10):
    time_start = time.perf_counter()
    limit = asyncio.Semaphore(max_concurrent)
    async with aiohttp.ClientSession() as session:
        coroutines = [limited_fetch(url, session, limit) for _ in range(total_requests)]
        await asyncio.gather(*coroutines)
    time_end = time.perf_counter()
    print(f"Time: {time_end - time_start:.6f} seconds")


def run_profile():
    # Опционально: HTML отчет
    os.environ["SCALENE_HTML"] = "true"
    # scalene_profiler.start()

    asyncio.run(main())

    #scalene_profiler.stop()


if __name__ == "__main__":
    run_profile()

    # scalene Parallelism_and_сoncurrency_8/profile/profile_task_async_5_4.py