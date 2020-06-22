a = 'xaiofeng'

# len 查询字符串的长度
print(len(a))

#   find   查找指定内容在字符串中是否存在，如果存在就返回该内容在字符串中第⼀次出现的开始位置索引值，如果不存在，则返回-1.
print(a.find('o'))

# index 跟find()⽅法⼀样，只不过，find⽅法未找到时，返回-1,⽽str未找到时，会报⼀个异常
print(a.index('o'))

# isalpha 判断是否纯字母
print(a.isalpha())

# isdigit 判断是否纯数字
print(a.isdigit())

# split  方法

b = ' zhangsan ,lisi,wangwu,zhaoliu,lulu,susu'
c = b.split(',')
print(c)
