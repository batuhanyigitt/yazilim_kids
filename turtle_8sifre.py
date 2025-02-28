import turtle
import time
correct_password = "turtle123"

password = turtle.textinput("Password Required", "Enter the password to start:")

if password == correct_password:
    # Display success message
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    screen.title("Access Granted! Enjoy the Project")
    # Create a turtle object to draw the pattern
    t = turtle.Turtle()
    t.speed(0)
    t.width(2)
    colors = ["red", "blue", "green", "yellow", "purple", "orange"]
    # Draw a colorful star pattern
    for i in range(72):
        t.color(colors[i % len(colors)])  # Cycle through colors
        t.forward(200)
        t.left(144)  # Angle for a star
        t.forward(200)
        t.right(144 + 5) 
    t.hideturtle()
    turtle.done()
else:

    screen = turtle.Screen()
    screen.bgcolor("red")
    screen.title("Access Denied")
    
    error_turtle = turtle.Turtle()
    error_turtle.color("white")
    error_turtle.write("Incorrect Password! Access Denied.", align="center", font=("Arial", 18, "bold"))
    
    time.sleep(3)
    turtle.bye()
