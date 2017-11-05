#!python2
# -*- coding: utf-8 -*-
import urllib2,urllib
import os,sys
from sys import argv

os.chdir(os.path.dirname(sys.argv[0]))

# def jump():
#     url = "http://10.54.100.254"
#     wangye = urllib2.urlopen(url)
#     nr = wangye.read()
#     # print nr
#     nr = nr[32:]
#     # print nr
#     nr = nr[:-30]
#     # print nr
#     txtfile = open("192.168.100.254.txt", 'w')
#     txtfile.write(nr)
#     txtfile.close()

def loginpage():
    temp = open("192.168.100.254.txt", 'r')
    url2 = temp.read()
    temp.close()
    login = urllib2.urlopen(url2)
    nr2 = login.read()
    # print nr2
    temp2 = open("login_page.txt", 'w')
    temp2.write(nr2)
    temp2.close()

def post():
    user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
    headers = {'User-Agent': user_agent}
    xuehao = '150243003'
    mima = '1234561'
    values = urllib.urlencode({'operatorPwd': '','operatorUserId':'','password':mima,'queryString':'wlanuserip%3D10.55.6.184%26wlanacname%3DZZTZ_HX_N18007%26ssid%3D%26nasip%3D10.54.2.13%26snmpagentip%3D%26mac%3Dca4f43cd3f9d%26t%3Dwireless-v2-plain%26url%3Dhttp%3A%2F%2Fnewtab.firefoxchina.cn%2Ferror-tab-rec.html%26apmac%3D%26nasid%3DZZTZ_HX_N18007%26vid%3D4022%26port%3D57%26nasportid%3DAggregatePort%25201.40220000%3A4022-0','service':'','userId':xuehao,'validcode':''})


    req = urllib2.Request(open('192.168.100.254.txt','r').read(), values, headers)
    # aaa = 111
    response = urllib2.urlopen(req)
    jieguo = response.read()
    print jieguo
    temp3 = open('successful.html','w')
    temp3.write(jieguo)

# jump()
loginpage()
post()
