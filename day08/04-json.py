
import json
person = {"name":"xiaofeng","age":18,"sex":'man'}
x = json.dumps(person)  # dunms方法将字典转换成字符串
# print(type(x))

n = '["nihao","hello"]'
y = json.loads(n)   #loads 可以将json的字符串转成py里面的对象
print(y)