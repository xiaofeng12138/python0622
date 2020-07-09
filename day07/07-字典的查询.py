person = {'name':'xiaofeng','age':18,'sex':'男','name':'lulu'}

#可以使用key获取对应的value
print(person['name'])

x = 'age'
print(person[x])

#属性不存在会保存  使用get方法可以不报错  如果未找到 则使用后面的默认值
# print(person['xf'])
print(person.get('xf','小哥哥'))