# py中的·for循环比较特殊要和in连用

# range内置的用来生成指定区间的整数序列
# in后面必须是一个可迭代的对象
for i in range(0,10):
    print(i)

#计算1-100的和

z = 0
for j in range(1,101):
    z += j
    print(z)