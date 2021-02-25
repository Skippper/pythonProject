from bs4 import *
import pandas as pd
import requests
import re
import logging
#爬取房源 写入excel
writer = pd.ExcelWriter('/Users/saybot/SKipper_HOME/python/pythonProject/reptile/房源.xls')

house_title_lst = []
houseInfo_lst = []
followInfo_lst = []
priceInfo_lst = []
positionInfo_lst = []

res_dict= {#用于存放最终数据
}
for page in range(1,101):
    if page == 1:
        url = 'https://bj.ke.com/ershoufang/co32/'
    else:
        url= 'https://bj.ke.com/ershoufang/pg{pageNum}co32/'.format(pageNum=page)
    logging.info(url)
    response = requests.get(url)
    response.encoding='utf-8'

    b = BeautifulSoup(response.text,'lxml')
    sellList = b.find(class_="sellListContent")
    lis = sellList.findAll('li',class_='clear')

    for container in lis:
        house_title = container.find('a').get('title')
        info_div = container.find('div',class_='info clear')
        positionInfo = re.sub('\\s+','',info_div.find('div', class_='positionInfo').text)
        houseInfo = re.sub('\\s+', '', ''.join(info_div.find('div', class_='houseInfo').text.split('\n')))
        followInfo = re.sub('\\s+','',''.join(info_div.find('div',class_='followInfo').text.split('\n')))
        priceInfo_arr = re.sub('\\s+', '|', info_div.find('div', class_='priceInfo').text).split('|')
        priceInfo = priceInfo_arr[1] + priceInfo_arr[2] + ',' + priceInfo_arr[3]
        #print(positionInfo)
        logging.info(positionInfo)
        positionInfo_lst.append(positionInfo)
        house_title_lst.append(house_title)
        houseInfo_lst.append(houseInfo)
        followInfo_lst.append(followInfo)
        priceInfo_lst.append(priceInfo)
    #print(lis)

res_dict['房源名']=house_title_lst
res_dict['位置']=positionInfo_lst
res_dict['房源信息']=houseInfo_lst
res_dict['关注信息'] = followInfo_lst
res_dict['价格信息'] = priceInfo_lst

dta_excel = pd.DataFrame(data=res_dict)
dta_excel.to_excel(writer,index_label='id')

writer.save()

