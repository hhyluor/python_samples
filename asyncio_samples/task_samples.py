# -*- coding: utf-8 -*-
# @Time : 2023/3/23 15:36
# @Author : hehaiyang
# @File : task_samples.py
# @Project : python_samples
# @Function :
import asyncio


def demo1():
    async def func():
        print(1)
        await asyncio.sleep(2)
        print(2)
        return "返回值"

    async def main():
        print("main开始")

        # 创建Task对象，将当前执行func函数任务添加到事件循环。
        task1 = asyncio.create_task(func())

        # 创建Task对象，将当前执行func函数任务添加到事件循环。
        task2 = asyncio.create_task(func())

        print("main结束")

        # 当执行某协程遇到IO操作时，会自动化切换执行其他任务。
        # 此处的await是等待相对应的协程全都执行完毕并获取结果`
        ret1 = await task1
        ret2 = await task2
        print(ret1, ret2)

    asyncio.run(main())


def demo2():
    import asyncio

    async def func():
        print(1)
        await asyncio.sleep(2)
        print(2)
        return "返回值"

    async def main():
        print("main开始")

        task_list = [
            asyncio.create_task(func(), name='n1'),
            asyncio.create_task(func(), name='n2')
        ]

        print("main结束")

        done, pending = await asyncio.wait(task_list, timeout=None)
        print(done)

    asyncio.run(main())


def demo3():
    import asyncio

    async def func():
        print(1)
        await asyncio.sleep(2)
        print(2)
        return "返回值"

    task_list = [
        func(),
        func(),
    ]

    done, pending = asyncio.run(asyncio.wait(task_list))
    print(done)


if __name__ == '__main__':
    demo3()
