
#元祖和列表很类似 （）包裹的，区别在于列表是可变的，元祖是不可变得
arr = ['hello', '','xiaofeng','lulu','']
nums = (2,3,4,5,6,6,8,7,7,7,7,7,7)

print(nums.index(4))  #查询数据第一次出现的位置
print(nums.count(7))  #查询某个元素出现的次数
print(type(nums))

#特殊情况表示元祖中只有一个数据 需要加一个逗号

a =(18,)
print(type(a))

print(tuple('hello'))  #('h', 'e', 'l', 'l', 'o')

#列表转换成为元祖  相互转换

print(tuple(arr))
print(list(nums))


