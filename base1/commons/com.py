from datetime import datetime, date, timedelta
from os import path
from bs4 import BeautifulSoup
import requests
import pandas
mydt = {"name": "as", "add": "beij"}
for key, val in mydt.items():
    print(key + ":" + val)


class Person():
    def __init__(self,name, age, com):
        self.name = name
        self.age = age
        self.com = com

class Chinese(Person):
    def __init__(self, name, age, com,dtl):
        super().__init__(name, age, com)
        self.dtl = dtl

ming = Chinese("sd",15,"alo7","hello")


requests.get()

mydict = {
    "name":"skipper",
    "gneder":"male",
    "company":"alo7",
    "detail":{
        "address":"上海",
        "home":"蚌埠"
    },
}
print("======================")
from datetime import *
import time

targetDate=datetime.fromtimestamp(1613801092).strftime('%Y-%m-%d')
print(targetDate)

nm = dict()
print(nm)
