import turtle

# Create turtle object
star = turtle.Turtle()
star.color("blue")
star.speed(3)

# Draw a star
for _ in range(5):
    star.forward(100)
    star.right(144)  # Turn the turtle by 144 degrees to form a star

turtle.done()
