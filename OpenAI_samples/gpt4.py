# -*- coding: utf-8 -*-
# @Time : 2023/3/18 12:02
# @Author : hehaiyang
# @File : openai_api_try.py
# @Project : python_samples
# @Function :
# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import openai

# 用您的API密钥替换此处的YOUR_API_KEY
from OpenAI_samples.settings import hy_api_key

openai.api_key = hy_api_key


def generate_markdown(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "你是一个AI机器人助手。"},
                  {"role": "user", "content": "哪个对将获得2023年NBA总冠军？"}],
        # max_tokens=4000,
        # n=1,
        # stop=None,
        # temperature=0.5,
    )

    return response.choices[0].text.strip()


if __name__ == "__main__":
    prompt = "Write a short story about a dragon and a princess."
    markdown_text = generate_markdown(prompt)

    with open("gpt4.md", "w") as md_file:
        md_file.write(markdown_text)

    print("Markdown文档已生成并保存为gpt4.md")
