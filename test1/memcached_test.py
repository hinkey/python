__author__ = 'hinkey'
#coding=utf8
import memcache

mcache= memcache.Client(['192.168.110.27:12660'])
print mcache.set('say','hello,memcache') #display - True
value = mcache.get('say')
print value #display - hello,memcache