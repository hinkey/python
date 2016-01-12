__author__ = 'hinkey'
#coding=utf8
import memcache

mcache= memcache.Client(['t.10000bee.com:12660'])
print mcache.set('say','hello,memcache') #display - True
value = mcache.get('say')
print value #display - hello,memcache