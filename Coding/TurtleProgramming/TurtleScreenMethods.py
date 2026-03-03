import turtle as T

# Most of the examples in this section refer to a TurtleScreen instance called screen.

canvas = T.getcanvas()

screen = T.TurtleScreen(canvas)

# screen.bgcolor("#C24F81")

# print(screen.bgcolor())

screen.bgpic('TurtleProgramming/smilinggiraffe.gif')
hari = T.RawTurtle(screen)

hari.fd(100)

screen.mainloop()

T.done()


