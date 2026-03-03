# import turtle as t

# harry = t.Turtle()

# pos = harry.pos()
# print(pos)
# harry.color('blue', 'red')
# harry.begin_fill()
# harry.teleport(60)
# pos = harry.pos()
# print(pos)

# harry.teleport(y= 50)
# pos = harry.pos()
# print(pos)

# harry.teleport(20, 30)
# pos = harry.pos()
# print(pos)
# harry.teleport(40, 60)
# pos = harry.pos()
# print(pos)
# harry.teleport(-40, 60)
# pos = harry.pos()

# # harry.home()
# # print(harry.pos())
# harry.end_fill()


# t.done()

# import turtle as t

# import os
# os.system('cls') # to clear terminal window

# harry = t.Turtle()

# p = harry.heading()
# print(p)

# harry.seth(270)

# t.done()

# import turtle as t

# import os
# os.system('cls') # to clear terminal window

# harry = t.Turtle()
# harry.fd(50); harry.dot(50,'blue'); harry.fd(50)
# print(harry.pos())
# t.done()


# import turtle as t

# import os
# os.system('cls') # to clear terminal window

# harry = t.Turtle()
# harry.speed(1)
# harry.color('blue')
# stamp_id = harry.stamp()
# print(stamp_id)
# harry.fd(100)
# stamp_id2 = harry.stamp()
# harry.seth(90)
# harry.fd(50)
# print(stamp_id2)
# print(harry.pos())
# harry.clearstamp(stamp_id)
# harry.clearstamps()
# t.done()

import turtle as t
import os
os.system('cls') # to clear terminal window

harry = t.Turtle()
harry.speed(1)

for i in range(5):
    harry.fd(50)
    harry.lt(72)
    
for i in range(5):
    harry.undo()
    
t.done()
