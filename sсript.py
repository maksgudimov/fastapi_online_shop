import asyncio
import time
import aiohttp


# async def print_some1():
#     print('Запуск1 ...')
#     await asyncio.sleep(1)
#     print('... Готово1')
#
#
# async def print_some2():
#     print('Запуск2 ...')
#     await asyncio.sleep(3)
#     print('... Готово2')
#
#
#
# async def main():
#     await print_some1()
#     await print_some2()
#
#
# if __name__ == "__main__":
#     asyncio.run(main())







# async def print_some1():
#     print('Запуск1 ...')
#     await asyncio.sleep(2)
#     print('... Готово1')
#
#
# async def print_some2():
#     print('Запуск2 ...')
#     await asyncio.sleep(1)
#     print('... Готово2')
#
#
# async def print_some3():
#     print('Запуск3 ...')
#     await asyncio.sleep(3)
#     print('... Готово3')
#
#
# async def main():
#     await asyncio.gather(print_some1(), print_some2(), print_some3())
#
#
# if __name__ == "__main__":
#     asyncio.run(main())


async def print_some1():
    print('Запуск1 ...')
    await asyncio.sleep(2)
    print('... Готово1')


async def print_some2():
    print('Запуск2 ...')
    await asyncio.sleep(1)
    print('... Готово2')


async def print_some3():
    print('Запуск3 ...')
    await asyncio.sleep(3)
    print('... Готово3')


async def main():
    # Запуск задач в фоновом режиме
    task1 = asyncio.create_task(print_some1())
    task2 = asyncio.create_task(print_some2())
    task3 = asyncio.create_task(print_some3())

    # Основная программа продолжает свою работу
    print('Основная программа продолжает свою работу')

    # Ожидание завершения всех фоновых задач
    await asyncio.gather(task1, task2, task3)
    print('Все фоновые задачи завершены')


if __name__ == "__main__":
    asyncio.run(main())




# async def do_request(session, url):
#     try:
#         start_time = time.time()
#         async with session.get(url) as response:
#             if response.status == 200:
#                 end_time = time.time()
#                 ping_time = end_time - start_time
#                 print(f"Ping to {url} successful: {ping_time:.4f} seconds")
#             else:
#                 print(f"Ping to {url} failed with status code {response.status}")
#     except Exception as exp:
#         print(f"Ping to {url} failed with error: {exp}")
#
#
#
#
# async def main():
#     url_list = [
#         "https://www.python.org/",
#         "https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0",
#         "https://nonexistssitehere/",
#         "https://docs.python.org/3/library/asyncio.html",
#         "https://docs.aiohttp.org/en/stable/",
#
#     ]
#     async with aiohttp.ClientSession() as session:
#         tasks = [do_request(session, url) for url in url_list]
#
#         await asyncio.gather(*tasks)
#
#
#
# if __name__ == "__main__":
#     asyncio.run(main())







# import time
# from collections import deque
#
# def coroutine(func):
#     def wrapper(*args, **kwargs):
#         gen = func(*args, **kwargs)
#         gen.send(None)  # prime the coroutine
#         return gen
#     return wrapper
#
# @coroutine
# def print_some1():
#     print('Запуск1 ...')
#     yield time.sleep(2)
#     print('... Готово1')
#
# @coroutine
# def print_some2():
#     print('Запуск2 ...')
#     yield time.sleep(1)
#     print('... Готово2')
#
# @coroutine
# def print_some3():
#     print('Запуск3 ...')
#     yield time.sleep(3)
#     print('... Готово3')
#
# def main():
#     tasks = deque([
#         print_some1(),
#         print_some2(),
#         print_some3()
#     ])
#
#     while tasks:
#         task = tasks.popleft()
#         try:
#             next(task)
#             tasks.append(task)  # re-add the task to the deque if not finished
#         except StopIteration:
#             pass
#
# if __name__ == "__main__":
#     main()
