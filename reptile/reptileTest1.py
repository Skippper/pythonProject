from bs4 import *
import pandas as pd
import requests
#爬取房源 写入excel
response = requests.get("https://bj.ke.com/ershoufang/co32/")
response.encoding='utf-8'
writer = pd.ExcelWriter('/Users/saybot/SKipper_HOME/python/pythonProject/reptile/out1.xls')




b = BeautifulSoup(response.text,'lxml')
sellList = b.find(class_="sellListContent")
lis = sellList.findAll('li',class_='clear')
res_lst= []
print(lis)
for houseSrc in lis:
    print(houseSrc.find('a').get('title'))
    res_lst.append(houseSrc.find('a').get('title'))

dta_excel = pd.DataFrame(
    data={'房源': res_lst})
dta_excel.to_excel(writer, 'Sheet1',index_label='id')
writer.save()
print(res_lst)

