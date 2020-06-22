m = 'abcdefghijklmnopqrstuvwxyz'

#切片语法
# m[start:end:step]   包含start  不包含end  step表示间隔  每次间隔step-1 个  step为负数代码从右往左取值
print(m[::])  #打印全部
print(m[:: -1])  #打印全部倒序  zyxwvutsrqponmlkjihgfedcba
print(m[2:9])  # cdefghi
print(m[2:])  # cdefghijklmnopqrstuvwxyz  未设置结束值 则默认取到末尾

print(m[2:9:2]) # cegi