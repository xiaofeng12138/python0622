
import  random
nums =['A','B','C','D','E','F','G','H','I','J']

rooms = [[],[],[]]

for i in nums:
    room = random.choice(rooms)
    room.append(i)
print(rooms)