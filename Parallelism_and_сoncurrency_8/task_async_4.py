# Практика:
#
# 4. Написать асинхронный код, который делает 50 get запросов к https://example.com.
# Записать все статусы ответов в файл и убедиться, что количество запросов соответствует заданному количеству.
# Необходимо учесть, чтобы одновременно выполнялось не больше 10 запросов.
# Для выполнения запросов использовать библиотеку aiohttp.
# Все значения, количество запросов, лимит одновременно выполняемых запросов и url должны передаваться как параметры.
import aiohttp
import asyncio
import aiofiles
import time



async def write_response(data: str) -> None:
    async with asyncio.Lock():
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


async def main():
    time_start = time.perf_counter()
    url = "https://example.com"
    limit = asyncio.Semaphore(10)
    async with aiohttp.ClientSession() as session:
        coroutines = [limited_fetch(url, session, limit) for _ in range(50)]
        await asyncio.gather(*coroutines)
    time_end = time.perf_counter()
    print(f"Time: {time_end - time_start:.6f} seconds")



if __name__ == "__main__":
    asyncio.run(main())