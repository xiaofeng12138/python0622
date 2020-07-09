
import  copy
words = ['hello','hi',[100,200,300],'ok','are','you']

# 浅拷贝 只能拷贝一层

word1 = copy.copy(words)
# 深拷贝只能使用copy的函数
word2 = copy.deepcopy(words)

words[2][0] = 1

print(word1)
print(word2)

# ['hello', 'hi', [1, 200, 300], 'ok', 'are', 'you']
# ['hello', 'hi', [100, 200, 300], 'ok', 'are', 'you']