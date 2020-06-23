
# 在字符串中可能使用到%展位符号
'''
%s ==> 表示字符串的占位符
%d ==> 表示整数占位符
%nd ==> 打印时显示n位，如果不够在前面使用空格补齐
%f ==>  表示浮点数的占位符
%x  ==> 将数字使用十六进制输出
%%  ==> 输入一个%
'''

print('大家好，是%3d号男嘉宾' %15)
print('大家好，是%-3d号男嘉宾' %15)
print('大家好，是%03d号男嘉宾' %15)
print('我今天挣了%2f元' %3.14)