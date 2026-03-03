import turtle as T

def goto_click(x, y):
    T.goto(x, y)
    
screen = T.Screen()
screen.onscreenclick(goto_click)

T.done()

