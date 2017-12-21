'''
R——READY版本，为全局程序提供某些功能准备
可以直接get()，此方法放弃

'''

import urllib.request
import re
import gzip,zlib

url = "http://www.baidu.com"


def get_coding():
    charset = page_content_byte.info().get("Content-Type")
    print(charset)
    return charset

def unzip():
    encoding = page_content_byte.info().get('Content-Encoding')
    if encoding == 'gzip':
        content = gzip(page_content_byte.read())
    elif encoding == 'deflate':
        content = deflate(page_content_byte.read())
    return content

def gzip(data):
    buf = StringIO(data)
    f = gzip.GzipFile(fileobj=buf)
    return f.read()

def deflate(data):
    try:
        return zlib.decompress(data, -zlib.MAX_WBITS)
    except zlib.error:
        return zlib.decompress(data)

"""<class 'tuple'>: ('Content-Type', 'text/html; charset=utf-8')
"""


def get_title(code1):
    lstr = 0
    rstr = 0
    if code1 != None:
        code = code1
    else:
        code = "utf-8"
    title_file = open("./files/title.txt",'w',encoding=code)
    page_content = page_content_byte.read().decode(code)
    # print(page_content)
    search = re.search("<title>",page_content)
    if search != None :
        search = search.span()
        # print(search)
    else:
        print("没有<title>字段")
        return None
    lstr = search[1]
    # print(lstr)
    search = re.search('</title>',page_content)
    if search != None :
        search = search.span()
        # print(search)
    else:
        print("没有</title>字段")
        return None
    rstr = search[0]
    # print(rstr)
    page_content = page_content[lstr:rstr]
    print(page_content)
    title_file.write(page_content)
    title_file.close()

page_content_byte = urllib.request.urlopen(url)     #Unicode网页内容

get_coding()
# print(get_coding())
# get_title(get_coding())


page_content_byte.close
