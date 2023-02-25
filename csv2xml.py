#!/usr/bin/env python
# -*- coding:utf-8 -*-
import csv

INPUT_FILE = 'blacklist.csv'
OUTPUT_FILE = 'blacklist.xml'

WORD_LIST = 0
REGEX_COLUMN = 1
DISENABLED_COLUMN = 2


def GenerateXml(text):
    with open(OUTPUT_FILE, 'a', encoding='utf-8') as output:

        if x[REGEX_COLUMN] == 'TRUE' and x[DISENABLED_COLUMN] == 'TRUE':
            output.write('\t<item enabled="false">r=' + x[WORD_LIST] +
                         '</item>\n')
        elif x[REGEX_COLUMN] == '' and x[DISENABLED_COLUMN] == 'TRUE':
            output.write('\t<item enabled="false">t=' + x[WORD_LIST] +
                         '</item>\n')
        elif x[REGEX_COLUMN] == 'TRUE' and x[DISENABLED_COLUMN] == '':
            output.write('\t<item enabled="true">r=' + x[WORD_LIST] +
                         '</item>\n')
        elif x[REGEX_COLUMN] == '' and x[DISENABLED_COLUMN] == '':
            output.write('\t<item enabled="true">t=' + x[WORD_LIST] +
                         '</item>\n')
        else:
            pass


with open(OUTPUT_FILE, 'w', encoding='utf-8') as fx:
    fx.write("<filters>\n")

with open(INPUT_FILE, newline='', encoding='utf-8-sig') as input:
    spamreader = csv.reader(input, delimiter=',')
    for x in spamreader:
        GenerateXml(x[WORD_LIST])

with open(OUTPUT_FILE, 'a', encoding='utf-8') as fx:
    fx.write('</filters>\n')
    fx.close()
