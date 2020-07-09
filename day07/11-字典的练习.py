
#获取下面列表中出现次数最多的字母

chars = ['a','c','c','c','a','f','e','a','r','a']

chars_count ={}

for x in chars:
    if x in chars_count:
        chars_count[x] += 1
    else:
        chars_count[x] = 1
# print(chars_count)

vs = max(chars_count.values())

for k,v in chars_count.items():
     if (v == vs):
         print(k)


