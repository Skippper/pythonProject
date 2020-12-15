from datetime import datetime,timedelta
import time
ctime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

v1 = datetime.now()
#把datetime转换成字符串
print(v1,type(v1))
v2 = v1.strftime("%Y-%m-%d")
print(v2)
#字符串转换成datatime
v3= datetime.strptime(v2,"%Y-%m-%d")
print(v3)
#时间的加减
v4 = v3 + timedelta(days=2,minutes=29)
v5=str(v4)
print(v5)

#时间戳转为datetime
mtime = time.time()
v6= datetime.fromtimestamp(mtime).strftime("%Y-%m-%d %H:%M:%S")
print(v6)