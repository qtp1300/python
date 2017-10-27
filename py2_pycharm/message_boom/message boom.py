import urllib2
# from sys import argv
# url = "http://www.baidu.com"
# wangye = urllib2.urlopen(url)
txtfile = open("temp.txt",'r')
neirong = txtfile.read()
print (neirong)
txtfile.close()
txtfile = open("temp.txt",'w')
strr = "3333"
# txtfile.writable()
txtfile.write(strr)
txtfile.close()
# print(wangye.read())