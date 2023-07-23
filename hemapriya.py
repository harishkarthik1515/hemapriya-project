import turtle
import random

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.left(90)

# Function to draw an equilateral triangle
def draw_triangle(side_length):
    for _ in range(3):
        turtle.forward(side_length)
        turtle.left(120)

# Function to draw a circle
def draw_circle(radius):
    turtle.circle(radius)

# Function to draw a petal shape
def draw_petal(size):
    for _ in range(6):
        turtle.color(random.random(), random.random(), random.random())  # Random color
        turtle.circle(size, 60)
        turtle.left(120)
        turtle.circle(size, 60)
        turtle.left(120)

# Set up the turtle
turtle.speed(0)  # Fastest drawing speed
turtle.bgcolor("white")
turtle.pensize(2)

# Draw the pattern using squares, triangles, and circles
turtle.penup()
turtle.goto(-200, 0)  # Move the turtle to the left side
turtle.pendown()
for _ in range(36):  # Draw 36 repetitions of the pattern
    draw_square(150)
    turtle.right(10)

    draw_triangle(180)
    turtle.right(10)

    draw_circle(90)
    turtle.right(10)

# Reset the turtle's position and orientation
turtle.penup()
turtle.goto(200, 0)  # Move the turtle to the right side
turtle.pendown()

# Draw the flower-like pattern
for _ in range(36):  # Draw 36 petals
    draw_petal(200)
    turtle.right(10)

# Hide the turtle
turtle.hideturtle()

# Keep the window open until manually closed
turtle.done()
