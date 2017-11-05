'''
qq.com 报错，检查错误原因
qq网页的charset位置不一样，不能用固定位置截取，遍历寻找
可以直接get()，此方法放弃
'''

import urllib.request
import re

url = "http://www.baidu.com"


def get_coding():
    code = "charset"                    #定义下面需要匹配的字符串
    headers = page_content_byte.info()._headers      #实际网址
    num = len(headers)
    i = 0
    while i< num:
        # print(i)
        nearcharset = headers[i]                    #定位到charset那一行
        num1 = len(nearcharset)
        i1 = 0
        while i1<num1:
            # print(i1)
            charsetline = nearcharset[i1]
            print(charsetline)
            i1+=1
            search = re.search(code,charsetline)  # 搜索匹配字符串
            if search != None:
                search = search.span()
                # print(search)
            else:
                print("没有charset字段")
        # print(nearcharset)
        i+=1;
"""    

        return None
    
    charset = nearcharset[search[1]+1:]
    # print(charset)
    return charset

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
"""
page_content_byte = urllib.request.urlopen(url)     #Unicode网页内容

# print(get_coding(
get_coding()
# get_title(get_coding())


page_content_byte.close
