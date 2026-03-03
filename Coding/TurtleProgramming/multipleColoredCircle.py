import turtle as T

kia = T.Turtle()

colors = ['red', 'green', 'orange', 'blue', 'purple', 'pink', 'brown', 'yellow']

for i in range(36):
    kia.color(colors[i % len(colors)])
    kia.circle(100)
    kia.left(10)
    
T.done()
