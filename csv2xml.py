#!/usr/bin/env python
# -*- coding:utf-8 -*-
import csv
from pypinyin import lazy_pinyin, Style, load_phrases_dict

## 常量
INPUT_FILE = 'blacklist.csv' # 输入
OUTPUT_FILE = 'blacklist.xml' # 输出

WORD_LIST = 0 # 屏蔽词所在列
REGEX_COLUMN = 1 # 自制表达式所在列
DISENABLED_COLUMN = 2 # 默认禁用列

## 多音字
load_phrases_dict({'重云': [['chong3'], ['yun2']]})

## 写入屏蔽词
def GenerateXml(text):
    with open(OUTPUT_FILE, 'a', encoding='utf-8') as output:
        # 正则表达式 == 否，禁用 == 否
        if i[REGEX_COLUMN] == '' and i[DISENABLED_COLUMN] == '':
            output.write('\t<item enabled="true">t=' + i[WORD_LIST] + '</item>\n')
        # 正则表达式 == 否，禁用 == 是
        elif i[REGEX_COLUMN] == '' and i[DISENABLED_COLUMN] == 'TRUE':
            output.write('\t<item enabled="false">t=' + i[WORD_LIST] + '</item>\n')
        # 正则表达式 == 是，禁用 == 否
        elif i[REGEX_COLUMN] == 'TRUE' and i[DISENABLED_COLUMN] == '':
            output.write('\t<item enabled="true">r=' + i[WORD_LIST] + '</item>\n')
        # 正则表达式 == 是，禁用 == 是
        elif i[REGEX_COLUMN] == 'TRUE' and i[DISENABLED_COLUMN] == 'TRUE':
            output.write('\t<item enabled="false">r=' + i[WORD_LIST] + '</item>\n')
        # 其他情况
        else:
            pass # 跳过

## 写入屏蔽列表起始行
with open(OUTPUT_FILE, 'w', encoding='utf-8') as output:
    output.write("<filters>\n")

## 读取 csv 文件
with open(INPUT_FILE, newline='', encoding='utf-8-sig') as input:
    spamreader = list(csv.reader(input, delimiter=',')) # 转换成列表
    spamreader.pop(0) # 删除表格标题
    # TODO: 按照以下顺序进行排序 0-9 a-z 汉语拼音a-z
    spamreader.sort(key=lambda x:lazy_pinyin(x,style=Style.TONE3,strict=False)[WORD_LIST]) # 按照汉语拼音升序排序
    #print(spamreader)
    for i in spamreader:
        GenerateXml(i[WORD_LIST])

## 写入屏蔽列表结束行
with open(OUTPUT_FILE, 'a', encoding='utf-8') as output:
    output.write('</filters>\n')
    output.close() # 关闭文件
