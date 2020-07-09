person1 = {'name':'xiaofeng','age':18,'sex':'男'}


#第一种 直接for in 循环字典
# for x in person1:  #for in  循环 获取到的是key的值
#     print(x, '=' ,person1[x])

#第二种 直接for in 循环字典
# for x in person1.keys():  #for in  循环 获取到的是key的值
#     print(x)

#第三种 只拿到value
# for x in person1.values():  #for in  循环 获取到的是key的值
#     print(x)

#第四种 获取键值对
for k,v in person1.items():  #for in  循环 获取到的是key的值
    print(k ,'=', v)