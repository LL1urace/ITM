# Практика:
#
# 5. Выполните профилирование для определения точек потребления памяти и просадок по времени.
import aiohttp
import asyncio
import aiolimiter
import time
import cProfile
import pstats
import tracemalloc


# Task №3
async def limited_fetch(url: str,
                        session: aiohttp.ClientSession,
                        limit: aiolimiter.AsyncLimiter) -> str:
    async with limit:
        async with session.get(url) as response:
            text = await response.text()
            print(f"[{time.strftime('%X')}] {url} - {response.status} - {len(text)} bytes")
            return f"[{time.strftime('%X')}] {url} - {response.status} - {len(text)} bytes"


async def main():
    time_start = time.perf_counter()
    url = "http://google.com"
    limit = aiolimiter.AsyncLimiter(10, 1)
    async with aiohttp.ClientSession() as session:
        coros = [limited_fetch(url, session, limit) for _ in range(10)]
        await asyncio.gather(*coros)
    time_end = time.perf_counter()
    print(f"Time: {time_end - time_start:.6f} seconds")


def run_profile():
    tracemalloc.start()
    profiler = cProfile.Profile()
    profiler.enable()

    asyncio.run(main())

    snapshot = tracemalloc.take_snapshot()
    top_stats = snapshot.statistics('lineno')

    print("[ Top 10 memory-consuming lines ]")
    for stat in top_stats[:10]:
        print(stat)

    profiler.disable()
    stats = pstats.Stats(profiler)
    stats.strip_dirs()
    stats.sort_stats('cumtime')
    stats.print_stats(10)




if __name__ == "__main__":
    run_profile()