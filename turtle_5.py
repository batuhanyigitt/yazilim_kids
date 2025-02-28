import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the face
face = turtle.Turtle()
face.color("yellow")
face.begin_fill()
face.circle(100)
face.end_fill()

# Create the eyes
eye = turtle.Turtle()
eye.penup()
eye.goto(-35, 120)
eye.pendown()
eye.color("black")
eye.begin_fill()
eye.circle(10)
eye.end_fill()

eye.penup()
eye.goto(35, 120)
eye.pendown()
eye.begin_fill()
eye.circle(10)
eye.end_fill()

# Create the smile
smile = turtle.Turtle()
smile.penup()
smile.goto(-50, 70)
smile.setheading(-60)
smile.pendown()
smile.circle(50, 120)  # Draw an arc for the smile

turtle.done()
