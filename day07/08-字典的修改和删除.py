person = {'name':'xiaofeng','age':18,'sex':'男','name':'lulu'}

person['name'] = '我爱lulu'

# 如果key 不存在的话  则会新增一个
person['xf'] = '小哥哥'
print(person.pop('name'))  #返回被删除的value
print(person)

