import turtle

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")  # Set the background color to black

# Create a turtle object
spiral = turtle.Turtle()
spiral.shape("turtle")
spiral.speed(10)  # Set the turtle's speed to maximum

# List of colors to cycle through
colors = ["red", "yellow", "green", "blue", "purple", "orange"]

# Draw the spiral
for i in range(360):
    spiral.pencolor(colors[i % 6])  # Change the pen color in a cycle
    spiral.width(i // 100 + 1)  # Increase pen width as the spiral grows
    spiral.forward(i * 3 / 5 + i)  # Move the turtle forward
    spiral.left(59)  # Turn the turtle to create the spiral effect

# Hide the turtle and display the drawing
spiral.hideturtle()
turtle.done()
