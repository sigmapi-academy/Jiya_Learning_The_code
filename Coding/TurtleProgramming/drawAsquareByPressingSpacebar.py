import turtle as T

def draw_square():
    for _ in range(4):
        T.fd(100)
        T.left(90)
        
screen = T.Screen()
screen.onkeypress(draw_square, "space")
screen.listen()

screen.on
T.done()
