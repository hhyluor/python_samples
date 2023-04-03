# -*- coding: utf-8 -*-
# @Time : 2023/3/23 14:54
# @Author : hehaiyang
# @File : asyncio_samples.py
# @Project : python_samples
# @Function :
"""
下载图片使用第三方模块aiohttp，请提前安装：pip3 install aiohttp
"""
import asyncio

# !/usr/bin/env python
# -*- coding:utf-8 -*-
import aiohttp


async def fetch(session, url):
    print("发送请求：", url)
    async with session.get(url, verify_ssl=False) as response:
        content = await response.content.read()
        file_name = url.rsplit('_')[-1]
        with open(file_name, mode='wb') as file_object:
            file_object.write(content)
        print('下载完成', url)


async def main():
    async with aiohttp.ClientSession() as session:
        url_list = [
            'https://www3.autoimg.cn/newsdfs/g26/M02/35/A9/120x90_0_autohomecar__ChsEe12AXQ6AOOH_AAFocMs8nzU621.jpg',
            'https://www2.autoimg.cn/newsdfs/g30/M01/3C/E2/120x90_0_autohomecar__ChcCSV2BBICAUntfAADjJFd6800429.jpg',
            'https://www3.autoimg.cn/newsdfs/g26/M0B/3C/65/120x90_0_autohomecar__ChcCP12BFCmAIO83AAGq7vK0sGY193.jpg'
        ]
        tasks = [asyncio.create_task(fetch(session, url)) for url in url_list]

        await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(main())
    # # 去生成或获取一个事件循环
    # loop = asyncio.get_event_loop()
    #
    # # 将任务放到`任务列表`
    # loop.run_until_complete(任务)
