import urllib
wangzhi = "http://www.baidu.com"
wangye = urllib.urlopen(wangzhi);
print wangye.readline();