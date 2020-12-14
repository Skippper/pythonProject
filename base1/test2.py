#文件操作

#file_Obj.read() 读取文件所有内容

#file_Obj.seek(3)
# file_Obj.read(2) #从当前光标所在的位置向后读取两个字符

#data = file_Obj.readline() #按行读取

#读取大文件
# for line in file_Obj:
#     print(line.strip())

#读取文件
# file_Obj = open("D:\study\data.png",mode="wb")
#
# # file_w = open("test.png",mode="w",encoding="utf-8")
# print(file_Obj.read())
#
# file_Obj.close()

#爬取
# import requests
# response = requests.get("http://www2.autoimg.cn/cardfs/product/g25/M02/ED/90/744x0_1_autohomecar__ChcCr13g73mATbNbAAnEFfP33QI725.jpg")
# data = response.content
#
# file_obj = open("test.jpg",mode="wb")
#
# file_obj.write(data)
#
# file_obj.close()

import requests
from bs4 import BeautifulSoup
response = requests.get("http://www.autohome.com.cn/news/202012/1082171.html#pvareaid=102624")
data = response.content #二进制

val = data.decode("gb2312") #gb2312

def func():
    return 1






