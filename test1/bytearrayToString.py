__author__ = 'hinkey'
# -*- coding: utf-8 -*-
import urllib
import struct
class csdn:
    def __init__(self):
        print ('Hello,this is a init')
    def getContent(self,url):
        self.url = url
        result = urllib.urlopen(self.url).read()#这里返回一个byte数组
        #print(type(result))
        saveFile = open('1.txt','w')
        try:
            saveFile.write(result)
        finally:
            saveFile.close()

test = csdn()
test.getContent('http://www.baidu.com')