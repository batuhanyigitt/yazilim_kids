import turtle

# Create the turtle
t = turtle.Turtle()
t.speed(0)
t.left(90)  # Start pointing up
t.color("brown")

# Recursive function to draw a fractal tree
def draw_branch(length, angle):
    if length < 10:  # Base case
        t.color("green")  # Small branches are green
        t.stamp()  # Represent leaves
        t.color("brown")
        return
    
    # Draw the branch
    t.forward(length)
    
    # Draw left branch
    t.left(angle)
    draw_branch(length - 15, angle)
    
    # Draw right branch
    t.right(2 * angle)
    draw_branch(length - 15, angle)
    
    # Go back to the original position
    t.left(angle)
    t.backward(length)

# Draw the tree
draw_branch(100, 30)
t.hideturtle()
turtle.done()
