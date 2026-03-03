import turtle

def draw_square():
    for _ in range(4):
        turtle.forward(100)
        turtle.left(90)
    turtle.penup()
    turtle.home()
    turtle.pendown()

def draw_circle():
    turtle.circle(50)
    turtle.penup()
    turtle.home()
    turtle.pendown()

def draw_triangle():
    for _ in range(3):
        turtle.forward(100)
        turtle.left(120)
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen = turtle.Screen()
screen.onkey(draw_square, 's')    # Press 's' for square
screen.onkey(draw_circle, 'c')    # Press 'c' for circle
screen.onkey(draw_triangle, 't')  # Press 't' for triangle

screen.listen()
turtle.mainloop()
