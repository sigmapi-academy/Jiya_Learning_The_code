import turtle as T

Joe = T.Turtle()
p = Joe.pos()
print(type(p))
print('Position of Joe:', p)
Joe.fd(50)
p = Joe.pos()
print('Position of Joe after moving 50 steps in x axis:', p)

Joe.bk(75)
p = Joe.pos()
print('Position of Joe after moving 75 steps in x axis backward:', p)

print('Current heading:',Joe.heading())
Joe.rt(45)
print('After turning 45 degree right:', Joe.heading())

Joe.left(45)
print('After turning 45 degree left:', Joe.heading())

Joe.penup()
Joe.left(45)
print('After turning 45 degree left:', Joe.heading())
Joe.fd(100)
print('Position of Joe after moving 100 steps towards 45 degree:', p)
print('Current position of Joe is:', Joe.pos())
T.done()