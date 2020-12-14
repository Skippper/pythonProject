#三元运算符
# data = input("请输入:")
# val = int(data) if data.isdecimal() else None

word = "ase123qweasdw234eqas324dwqe213asd12"
temp=""
nums=[]
index = 0
while (index != len(word)):
    target = word[index:index+1]
    if (target.isdigit()):
        temp += target
        if (index == len(word) - 1):
            nums.append(temp)
        elif (not word[index + 1 : index + 2].isdigit()):
            nums.append(temp)
            temp=""
    index +=1

a = 1

def parseDta():
    res1 = []
    res2 = []
    res3 = []
    with open("../base1/log.txt",mode="r",encoding="utf-8") as file:
        for item in file:
           lineArr = item.strip().split("|")
           res1.append(item.strip())
           res2.append(lineArr)
           lineDict={}
           lineDict["name"] = lineArr[0]
           lineDict["age"] = lineArr[2]
           lineDict["pwd"] = lineArr[1]
           res3.append(lineDict)
    print(res1)
    print(res2)
    print(res3)
    global a
    a=2
    file.close()


#函数高级
#分页
# numList = range(1,345)
# max_page_num,a = divmod(len(numList),10)
# page = int(input("输入"))
# for item in numList[(page - 1) * 10:page * 10]:
#     print(item)

def func(args):
    print(args)

func_list = {func,func,func}

info = {
    "f1":func,
    "f2":func
}


def show():
    return func

#密码不显示
# import getpass
# pwd = getpass.getpass("输入密码")
# print(pwd)

#import hashlib #加密

#装饰器
def func(arg):
    def inner():
        print("inner before")
        v = arg()
        print("inner after")
        return v
    return inner

 #执行func函数 并且将发f1作为参数传入func函数 func(f1) f1 ==func(f1)
@func
def f1():
    print(123)
    return 666

v = f1()



def deco(func):
    def inner():
        v1 = func()
        return v1
    return inner


#sys 模块
import sys
import time
# for i in range(1,101):
#     print("%s%%"%i)
#     time.sleep(0.05)

with open("../base1/log.txt",mode="r",encoding="utf-8") as f1:
    for index in f1:
        print(index)

import os

print(os.path.dirname(os.path.abspath("base1.py")))
print(os.path.basename("base1.py"))
abpath= os.path.abspath("base1.py")
dirname = os.path.dirname(abpath)
print(os.path.join(dirname, "a.py"))


res = os.walk("D:\codespace\project\pythonProject")
# for baseDir,innerDir,c in res:
#     # print(os.path.join(baseDir,c))
#     for item in c:
#         print(os.path.join(baseDir,item))

print(os.listdir("D:\codespace\project\pythonProject"))

































