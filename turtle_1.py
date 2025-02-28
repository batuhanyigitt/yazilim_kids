import turtle 

screen = turtle.Screen()
screen.bgcolor("lightblue")

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.speed(2)

for _ in range(4):
    t.forward(100)
    t.left(90)

t.hideturtle()
turtle.done()