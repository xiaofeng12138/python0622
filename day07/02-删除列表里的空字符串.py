arr = ['hello', '','xiaofeng','lulu','']

new_arr =[]

for item in arr:
    if item !='':
      new_arr.append(item)
    arr = new_arr
print(arr)