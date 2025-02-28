import turtle 
import random 
import time 

screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.title("Turtle Click Oyunu")

t = turtle.Turtle()
t.shape("turtle")
t.color("green")
t.penup()

click_count = 0 
game_time = 10 
start_time = time.time()

def move_turtle():
    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    t.goto(x, y)
    
    
def count_click(x, y):
    global click_count
    click_count += 1 
    move_turtle()

move_turtle()


screen.onclick(count_click)

while True: 
    if time.time() - start_time > game_time: 
        break 
    screen.update()
    
    
t.hideturtle()
game_over = turtle.Turtle()
game_over.hideturtle()
game_over.penup()
game_over.color("black")
game_over.goto(0, 0)
game_over.write(f"Oyun bitti su kadar tiklamissin {click_count}", align="center", font=("Arial", 16, "bold"))


time.sleep(3)
screen.bye()