persons =[
    {'name':'xiaofeng','age':18},
    {'name':'lulu','age':20},
    {'name':'susu','age':22},
    {'name':'hanhan','age':22},
]

x = input('请输入用户名:')

for person in persons:
    # print(person)
    if person['name'] == x:
        print('你输入的名字已存在')
        break;
else:
    new_person ={'name':x}
    y = int(input('请输入年龄：'))
    new_person['age'] = y
    persons.append(new_person)
    print(persons)
    print(type(persons))
    print('用户添加成功')