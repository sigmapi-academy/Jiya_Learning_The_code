import turtle as T

def move_left():
    T.setheading(180)
    T.fd(50)

def move_right():
    T.setheading(0)
    T.fd(50)

def move_up():
    T.setheading(90)
    T.fd(50)

def move_down():
    T.setheading(270)
    T.fd(50)

screen = T.Screen()
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.listen()

T.mainloop() #or T.done()
