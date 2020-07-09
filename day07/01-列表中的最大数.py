

nums = [1,5,8,4,3,0,7,4,9]


# 利用排序方式
# nums.sort()
# print(nums[-1])

x = nums[0]
# for num in nums:
#     if num > x:
#        x = num

i = 0
while i<len(nums):
   if nums[i] > x:
      x = nums[i]
      index = i
   i += 1

print('最大数为%d,他的下表为 %d' % (x,index))
