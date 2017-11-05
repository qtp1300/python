#!python2
# -*- coding: utf-8 -*-
import urllib,urllib2,sys,os
def get_page_info():
    start = "http://www.baidu.com:80"
    first = urllib.urlopen(start)
    print first.info()

def get_page():
    start = "http://www.baidu.com:80"
    first = urllib.urlopen(start)
    # first1 = urllib2.request_host(start)
    page = first.read()
    first.close()
    title_file = open("./files/title.txt", 'w')
    title_file.write(page)
    print page
    title_file.close()
    title_file = open("./files/title.txt")
    print title_file.read()
    title_file.close()

get_page_info()