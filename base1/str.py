name = input("输入姓名")
do = input("做什么")
age = int(input("年龄"))
temp = """
%s今年%d岁
在%s看书
        """%(name,age,do,)
print(temp)
'''
'''

def func():
    return 1

astr = "hello javae"
# str = str.lstrip()
# str = str.replace("hello","world",1)
# print(astr[1:6]) 大于等于1小于6(前闭后开) astr[3:] 取到最后
# print(astr[-5:])
#astr[0:-1: 2] 2代表步长 从0 开始取 第二次从2索引开始取
#print(astr[::-1]) 字符串反转
# print(astr[::2])

# for循环
# for item in astr:
#     print(item)
#     break
#     print(123)

# arr= range(0,10) #[1,2,3,4,5,6,7,8,9]
# for i in arr:
#     if i == 7 :
#         continue
#     print(i)