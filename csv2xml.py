#!/usr/bin/env python
# -*- coding:utf-8 -*-
import csv

inputFile = 'blacklist.csv'
outputFile = 'blacklist.xml'

WordLine = 0
RegExLine = 1
DisenabledLine = 2


def GenerateXml(text):
    with open(outputFile, 'a', encoding='utf-8') as output:
    
        if x[RegExLine] == 'TRUE':
            RegEx = 'r'
        elif x[RegExLine] == '':
            RegEx = 't'
        
        if x[DisenabledLine] == 'TRUE':
            output.write('\t<item enabled="false">' + RegEx + '=' + x[WordLine] + '</item>\n')
        elif x[DisenabledLine] == '':
            output.write('\t<item enabled="true">' + RegEx + '=' + x[WordLine] + '</item>\n')

with open(outputFile, 'w', encoding='utf-8') as fx:
    fx.write("<filters>\n")

with open(inputFile, newline='', encoding='utf-8-sig') as input:
    spamreader = csv.reader(input, delimiter=',')
    for x in spamreader:
        GenerateXml(x[WordLine])

with open(outputFile, 'a', encoding='utf-8') as fx:
    fx.write('</filters>')
    fx.close()
    