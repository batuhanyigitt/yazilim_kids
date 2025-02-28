import turtle

# Create turtle object
circle_drawer = turtle.Turtle()
circle_drawer.speed(5)

# Draw the circle
circle_drawer.penup()
circle_drawer.goto(0, -150)  # Move to starting position
circle_drawer.pendown()
circle_drawer.circle(150)

# Draw squares inside the circle
for size in range(30, 150, 30):
    circle_drawer.penup()
    circle_drawer.goto(-size, size)  # Move to top-left corner of the square
    circle_drawer.pendown()
    for _ in range(4):
        circle_drawer.forward(size * 2)
        circle_drawer.right(90)

turtle.done()
