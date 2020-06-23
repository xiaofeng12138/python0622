

# {} 表示一个占位符
a= '大家好，我是{}，今年{}岁了'.format('xiaofeng',18)
print(a)


# {0} 数字表示下标
b= '大家好，我是{0}，今年{1}岁了'.format('lulu',19)
print(b)

# {变量名}
c= '大家好，我是{name}，今年{age}岁了'.format(name='susu',age=15)
print(c)


arr=['xiaofeng',18,'anhui']
d= '大家好，我是{}，今年{}岁了,我来自{}'.format(*arr)
print(d)

info={'name':'lulu','age':19,'addr':'maanshan'}
e= '大家好，我是{name}，今年{age}岁了,我来自{addr}'.format(**info)
print(e)



