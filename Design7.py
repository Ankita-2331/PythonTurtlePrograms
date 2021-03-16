import turtle
t=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("black")
t.speed(0)
t.pencolor("pink")
t.penup()
t.goto(0,200)
t.pendown()
a=0
b=0
while True:
    t.forward(a)
    t.right(b)
    a+=3     #increase a to increase the size of design
    b+=1
    if b==200:
        break
wn.exitonclick()


