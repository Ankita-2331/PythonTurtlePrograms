import turtle
colors=['red','yellow','blue','green','orange','pink']
screen=turtle.Screen()
t=turtle.Turtle()
t.speed(0)
screen.bgcolor('black')
for x in range(300):
    t.pencolor(colors[x%6])
    t.width(3)
    t.forward(x)
    t.left(20)
