
a=13
b=20
# 方法一
#
# c = b
# b = a
# a = c

# 方法2 异或运算符
# a = a^b
# b = a^b
# a =a^b

# 方法3 py特有
a,b = b,a

print(a)
print(b)