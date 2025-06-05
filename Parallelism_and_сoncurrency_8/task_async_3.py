# Практика:
#
# 3. Реализуйте асинхронный метод, который будет отправлять запросы в http://google.com по http
# с ограничением не более 10 запросов в единицу времени.
import aiohttp
import asyncio
import aiolimiter
import time


async def limited_fetch(url: str,
                        session: aiohttp.ClientSession,
                        limit: aiolimiter.AsyncLimiter) -> None:
    async with limit:
        async with session.get(url) as response:
            text = await response.text()
            print(f"[{time.strftime('%X')}] {url} - {response.status} - {len(text)} bytes")


async def main():
    time_start = time.perf_counter()
    url = "http://google.com"
    limit = aiolimiter.AsyncLimiter(10, 1)
    async with aiohttp.ClientSession() as session:
        coros = [limited_fetch(url, session, limit) for _ in range(10)]
        await asyncio.gather(*coros)
    time_end = time.perf_counter()
    print(f"Time: {time_end - time_start:.6f} seconds")



if __name__ == "__main__":
    asyncio.run(main())