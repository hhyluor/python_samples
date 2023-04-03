from io import StringIO

import openai
import pandas as pd

# 配置OpenAI API密钥
from OpenAI_samples.settings import hy_api_key

openai.api_key = hy_api_key  # 替换为您的API密钥，如果不使用环境变量


def combine_columns(row):
    return "|".join(str(cell) for cell in row)


def generate_content(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "你是一个AI机器人助手。"},
                  {"role": "user", "content": prompt}],
    )
    return response.choices[0].message.content


if __name__ == "__main__":
    # 读取两个Excel表
    keywords_df = pd.read_excel("关键词.xlsx")
    labels_df = pd.read_excel("标签.xlsx", header=None)
    labels = labels_df.apply(combine_columns, axis=1).str.cat(sep='\n')
    keywords = keywords_df.apply(combine_columns, axis=1).str.cat(sep='\n')
    prompt = "我先给你下面这些标签四元组" + "\n" + labels + "\n\n" + "然后再给你关键词,标签编码,标签,对外显示标签编码,对外显示标签,五元组" + "\n" + keywords + "\n" + \
             "关键词和标签四元组是否代表同一个临床意义,加上第6列代表是否,如果不一致,就在我给的标签四元组中找出最合适的,放在7,8,9,10列中,以表格形式给我,谢谢"

    markdown_text = generate_content(prompt)
    # 从字符串创建 DataFrame
    data_str = markdown_text.replace('|', '').strip()
    data_df = pd.read_csv(StringIO(data_str), sep='\s\s+', engine='python')

    # 保存 DataFrame 为 Excel 文件
    data_df.to_excel('output2.xlsx', index=False)
