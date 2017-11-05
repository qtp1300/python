'''
python2 版本
已废弃
全面转入py3
'''
#!python2
# -*- coding: utf-8 -*-

import urllib,urllib2,sys,os

start = "http://www.baidu.com"
first = urllib.urlopen(start)
title_file = open("./files/title.txt",'w')
page = first.read()
title_file.write(page)
print page
title_file.close()
title_file = open("./files/title.txt",'r')
# print title_file.read()
title_file.close()
