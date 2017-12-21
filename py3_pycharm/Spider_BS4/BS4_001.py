from urllib.request import urlopen
from bs4 import BeautifulSoup
import gzip

url = "http://qzone.qq.com"
html = urlopen(url)
ziped = (html.info().get("Content-Encoding")) == ("gzip")
if ziped == True:
    print("启用了压缩")
    html = gzip.decompress(html.read())
else:
    print("没有启用压缩")
    html = html.read()
bs4 = BeautifulSoup(html,"html.parser")
# html.close()
print(bs4.title)

"""
.decode('utf-8')
.read()
,from_encoding='gb2312'
"""