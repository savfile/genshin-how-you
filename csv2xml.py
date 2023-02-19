#!/usr/bin/env python
# -*- coding:utf-8 -*-
from re import search

textFile = 'blacklist.csv'
generateFile = 'blacklist.xml'
#generateMinFile = 'blacklist.min.xml'

def generateXml(text):
    with open(generateFile, 'a', encoding='utf-8') as fx:
        if search(r'\\|\^|\||\$|\*|\+|\?|\{|\}|\.|\(|\)|\[|\]|\\s', text) != None:
            if search(r'\(\?\<?\!', text) == None:
                fx.write('\t<item enabled="true">r=' + text.strip('\n') + '</item>\n')
            elif search(r'\(\?\<?\!', text) != None:
                pass
        #elif search(r'\\|\^|\||\$|\*|\+|\?|\{|\}|\.|\(|\)|\[|\]|\\s', text) == None:
        else:
            fx.write('\t<item enabled="true">t=' + text.strip('\n') + '</item>\n')

#def generateMinXml(text):
    #with open(generateMinFile, 'a', encoding='utf-8') as fx:
        #if search(r'\\|\^|\||\$|\*|\+|\?|\{|\}|\.|\(|\)|\[|\]|\\s', text) != None:
            #if search(r'\(\?\<?\!', text) == None:
                #fx.write('<item enabled="true">r=' + text.strip('\n') + '</item>')
            #elif search(r'\(\?\<?\!', text) != None:
                #pass
        #else:
            #fx.write('<item enabled="true">t=' + text.strip('\n') + '</item>')

with open(generateFile, 'w', encoding='utf-8') as fx:
    fx.write("<filters>\n")

#with open(generateMinFile, 'w', encoding='utf-8') as fx:
    #fx.write("<filters>")

with open(textFile, 'r', encoding='utf-8-sig') as fp:
    for line in fp:
        generateXml(line)
        #generateMinXml(line)
    fp.close()

with open(generateFile, 'a', encoding='utf-8') as fx:
    fx.write('</filters>')
    fx.close()

#with open(generateMinFile, 'a', encoding='utf-8') as fx:
    #fx.write('</filters>')
    #fx.close()

print('ok')