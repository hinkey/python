# encoding: utf-8
import urllib2
import commands
import threading
import time
from __builtin__ import str
import os
import logging

LOG_FILENAME="log.txt"
logging.basicConfig(filename=LOG_FILENAME,level=logging.NOTSET)

def httpStatus():     
    try:        
        page=urllib2.urlopen('http://localhost:3000/api/err',timeout=2)
    except Exception,e:
            print "http err is "+str(e)
            print '服务错误，第一次检测，重新启动pm2,错误时间是：' +time.strftime('%Y-%m-%d %H:%M:%S')
            temp = os.popen('pm2 start /Users/hinkey/Documents/working/nodejs/mobileCloud/src/server.js')  
            print temp.read()
            logging.debug("http err is "+str(e))
            logging.debug('服务错误，第一次检测，重新启动pm2,错误时间是：' +time.strftime('%Y-%m-%d %H:%M:%S'))
        
    time.sleep(3)
    try:        
        page=urllib2.urlopen('http://localhost:3000/api/err',timeout=2)
    except Exception,e:
            print "http err is "+str(e)
            print '服务错误，第二次检测，重新启动pm2,错误时间是：' +time.strftime('%Y-%m-%d %H:%M:%S')
            temp = os.popen('pm2 start /Users/hinkey/Documents/working/nodejs/mobileCloud/src/server.js')  
            print temp.read()
            logging.debug("http err is "+str(e))
            logging.debug('服务错误，第二次检测，重新启动pm2,错误时间是：' +time.strftime('%Y-%m-%d %H:%M:%S'))
          
    time.sleep(3)
    try:        
        page=urllib2.urlopen('http://localhost:3000/api/err',timeout=2)
    except Exception,e:
            print "http err is "+str(e)
            print '服务错误，第三次检测，重新启动pm2,错误时间是：' +time.strftime('%Y-%m-%d %H:%M:%S')
            temp = os.popen('pm2 start /Users/hinkey/Documents/working/nodejs/mobileCloud/src/server.js')  
            print temp.read()
            logging.debug("http err is "+str(e))
            logging.debug('服务错误，第三次检测，重新启动pm2,错误时间是：' +time.strftime('%Y-%m-%d %H:%M:%S'))

#timer定时器
def checkHttp():
        print "每次间隔10分钟检测一次，检测时间是："+time.strftime('%Y-%m-%d %H:%M:%S')
        httpStatus()
        global t        #Notice: use global variable!
        t = threading.Timer(10, checkHttp)
        t.start()
checkHttp()