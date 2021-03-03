import turtle
t=turtle.Turtle()
colors=['green','yellow','pink','blue','red','purple']
screen=turtle.Screen()
t.speed(0)
screen.bgcolor('black')
t.width(10)
t.right(90)
t.forward(80)
t.right(120)
t.forward(80)
t.right(144)         
for i in range(10000):
    t.pencolor(colors[i%6])
    t.forward(380)
    t.left(190)

'''To make a particular shape, just adjust the angles in line number 12 and 16..just remember both the angles need to be the same!!'''