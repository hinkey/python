# encoding: utf-8
import memcache
import logging
import threading
import time

LOG_FILENAME = "memcachedClearLog.txt"
logging.basicConfig(filename=LOG_FILENAME, level=logging.NOTSET)
mcache = memcache.Client(['192.168.110.27:12660'])


def clearFunction():
    Users = mcache.get('Users-')
    if Users != None:
        mcache.delete('Users-')
        print("memcached clear: Users-")
        logging.debug("memcached clear: Users-")
        logging.debug('memcached数据有空值,删除时间是:' +time.strftime('%Y-%m-%d %H:%M:%S'))

    Groups = mcache.get('Groups-')
    if Groups != None:
        mcache.delete('Groups-')
        print("memcached clear: Groups-")
        logging.debug("memcached clear: Groups-")
        logging.debug('memcached数据有空值,删除时间是:' +time.strftime('%Y-%m-%d %H:%M:%S'))

    GroupUserMaps = mcache.get('GroupUserMaps-')
    if GroupUserMaps != None:
        mcache.delete('GroupUserMaps-')
        print("memcached clear: GroupUserMaps-")
        logging.debug("memcached clear: GroupUserMaps-")
        logging.debug('memcached数据有空值,删除时间是:' +time.strftime('%Y-%m-%d %H:%M:%S'))

    AttributeDef = mcache.get('AttributeDef-')
    if AttributeDef != None:
        mcache.delete('AttributeDef-')
        print("memcached clear: AttributeDef-")
        logging.debug("memcached clear: AttributeDef-")
        logging.debug('memcached数据有空值,删除时间是:' +time.strftime('%Y-%m-%d %H:%M:%S'))

    AttributeDataTypeDef = mcache.get('AttributeDataTypeDef-')
    if AttributeDataTypeDef != None:
        mcache.delete('AttributeDataTypeDef-')
        print("memcached clear: AttributeDataTypeDef-")
        logging.debug("memcached clear: AttributeDataTypeDef-")
        logging.debug('memcached数据有空值,删除时间是:' +time.strftime('%Y-%m-%d %H:%M:%S'))

    DevType = mcache.get('DevType-')
    if DevType != None:
        mcache.delete('DevType-')
        print("memcached clear: DevType-")
        logging.debug("memcached clear: DevType-")
        logging.debug('memcached数据有空值,删除时间是:' +time.strftime('%Y-%m-%d %H:%M:%S'))

    DevTypeAttributesMaps = mcache.get('DevTypeAttributesMaps-')
    if DevTypeAttributesMaps != None:
        mcache.delete('DevTypeAttributesMaps-')
        print("memcached clear: DevTypeAttributesMaps-")
        logging.debug("memcached clear: DevTypeAttributesMaps-")
        logging.debug('memcached数据有空值,删除时间是:' +time.strftime('%Y-%m-%d %H:%M:%S'))

    DevDataType = mcache.get('DevDataType-')
    if DevDataType != None:
        mcache.delete('DevDataType-')
        print("memcached clear: DevDataType-")
        logging.debug("memcached clear: DevDataType-")
        logging.debug('memcached数据有空值,删除时间是:' +time.strftime('%Y-%m-%d %H:%M:%S'))

def checkHttp():
    print "每次间隔10秒钟检测一次，检测时间是：" + time.strftime('%Y-%m-%d %H:%M:%S')
    clearFunction()
    global t  # Notice: use global variable!
    t = threading.Timer(10, checkHttp)
    t.start()

checkHttp()
