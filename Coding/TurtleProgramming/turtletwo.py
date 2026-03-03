import turtle as T

jack = T.Turtle()

jack.shape('turtle')
print('current position of jack:',jack.pos())
currentSpeed = jack.speed()
print('Default speed of the turtle Jack:', currentSpeed)
jack.speed(1) #slowest
print('Now the speed of Jack the turtle:', jack.speed())
jack.goto(100, 150)
print('current position of jack:',jack.pos())
jack.color('red')
jack.circle(50) #radius = 10 units
print('current position of jack:',jack.pos())

jack.pencolor('purple')
jack.penup()
jack.goto(-10, -10)
jack.pendown()
jack.circle(50)
print('current position of jack:',jack.pos())

T.done() #to complete the execution of window

