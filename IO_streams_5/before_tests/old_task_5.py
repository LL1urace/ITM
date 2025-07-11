# Практика:

# 5. Посмотрите видео про контекстный менеджер и повторите все действия
# из видео с файлом из пункта 2 https://www.youtube.com/watch?v=ycVlsU_c4Mg

# №1 (Ошибка - переполнения подключений к файлу)
# lst = []
# for i in range(10000):
#     lst.append(open("files_task2/task_5/passwords.txt", 'w'))


# №2 (Ошибки нет из-за закрытия файла)
# lst = []
# for i in range(10000):
#     file = open("files_task2/task_5/passwords.txt", 'w')
#     lst.append(file)
#     file.close()


# №3 Используем контекстный менеджер
# with open("files_task2/task_5/passwords.txt", 'w') as f:
#     f.write('123')
#     f.write('hello')
# print('end')


# №4 (Ошибки нет из-за закрытия файла контекстным менеджером)
# lst = []
# for i in range(10000):
#     with open("files_task2/task_5/passwords.txt", 'w') as f:
#         lst.append(f)


# №5 (Взаимодействие с файлом за границей контекста)
# with open("files_task2/task_5/passwords.txt", 'w') as f:
#     f.write('123')
#     f.write('hello')
# print(f)
# # print(f.write('123')) # Ошибка: нельзя записать в закрытый файл


# №6 (Ошибки нет из-за закрытия файла контекстным менеджером)
# with open("files_task2/task_5/passwords.txt", 'w') as f:
#     f.write('123')
#     f.write('hello')
# print(f)
# print(f.write('123')) # Ошибка: нельзя записать в закрытый файл


# №7 (Ошибка - контекстный менеджер работает только с объектами без метода __enter__)
# with print("files_task2/task_5/passwords.txt", 'w') as f:
#     f.write('123')
#     f.write('hello')
# print(f.write('123'))


# №8 (Пример использования with)
import os

with os.scandir(".") as entries:
    for entry in entries:
        print(entry.name, "->", entry.stat().st_size, "bytes")


# №9 (Пример использования with)
# import threading
#
# balance_lock = threading.Lock()
#
# # balance_lock.acquire() # вкл. блокировки
# # balance_lock.release() # выклю блокировки
#
# # c контекстным менеджером блокировка вкл. и выкл. автоматически
# with balance_lock:
#     pass


# №10 (Пример с двумя with)
import asyncio
from aiohttp import ClientSession

async def main():

    async with ClientSession() as session:
        async with session.get("https://python.org") as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")


if __name__ == "__main__":
    asyncio.run(main())