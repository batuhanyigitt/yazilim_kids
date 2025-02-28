import turtle
import time
import random

# Set the correct password
correct_password = "race123"

# Prompt the user for the password
password = turtle.textinput("Password Required", "Enter the password to start:")

# Check if the password is correct
if password == correct_password:
    # Display success message
    screen = turtle.Screen()
    screen.title("Turtle Race Game")
    screen.bgcolor("lightgreen")
    
    # Create the race track
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, 100)
    t.pendown()
    for step in range(6):
        t.write(step * 50, align="center")
        t.right(90)
        t.forward(300)
        t.backward(300)
        t.left(90)
        t.penup()
        t.forward(50)
        t.pendown()
    t.hideturtle()

    # Create turtles for the race
    colors = ["red", "blue", "yellow", "purple", "orange"]
    turtles = []
    start_y = 80
    for color in colors:
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape("turtle")
        racer.penup()
        racer.goto(-220, start_y)
        start_y -= 40
        turtles.append(racer)

    # Start the race
    is_race_on = True
    while is_race_on:
        for racer in turtles:
            racer.forward(random.randint(1, 5))
            if racer.xcor() > 200:  # Finish line
                is_race_on = False
                winner_color = racer.color()[0]
                break

    result = turtle.Turtle()
    result.penup()
    result.hideturtle()
    result.color("black")
    result.goto(0, -150)
    result.write(f"kazanan kaplumbaga {winner_color} ", align="center", font=("Arial", 16, "bold"))
    
    turtle.done()

else: 
    screen = turtle.Screen()
    screen.bgcolor("red")
    screen.title("Erisim Reddedildi")
    
    error_turtle = turtle.Turtle()
    error_turtle.color("white")
    error_turtle.write("yanlis sifre girdiniz.", align="center", font=("Arial", 18, "bold"))
    
    time.sleep(5)
    turtle.bye()