import turtle
def draw_square(t):
    for i in range(4):
        t.forward(200)
        t.right(90)
def draw_art():
    Ankita=turtle.Turtle()
    Ankita.color("yellow")
    Ankita.pensize(2)
    Ankita.speed(0)
    for j in range(36):
        draw_square(Ankita)
        Ankita.right(10)
    
    Kamboj=turtle.Turtle()
    Kamboj.color("blue")
    Kamboj.pensize(2)
    Kamboj.speed(0)
    size=1
    for k in range(300):
        Kamboj.forward(size)
        Kamboj.right(91)
        size+=1
window=turtle.Screen()
window.bgcolor("black")
draw_art()
window.exitonclick()