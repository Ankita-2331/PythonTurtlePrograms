import turtle
t=turtle.Turtle()
wn=turtle.Screen()
wn.bgcolor("black")
t.pensize(4)       #change this for changing thickness of circles 
t.shape("circle")
t.speed(0)
b=['red','yellow','green','purple']
for i in range(100):   #change this for changing the frequnecy of making the circles 
    for a in b:
        t.color(a)
        t.circle(150)  #change this for changing  radius of circles 
        t.left(10)    #change this for changing spaces between circles 
wn.exitonclick()