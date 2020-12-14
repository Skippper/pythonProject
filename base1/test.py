v1=[1,2]
v2=[2,3]
v3=[11,22,v1,v2,v1]

user={"name":"qwe","age":"123"}
# print(type(user) is dict)

#深浅拷贝
import copy
v4 =copy.deepcopy(v3)
print(v4)



