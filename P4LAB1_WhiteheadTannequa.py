# Tannequa Whitehead
# P4LAB1
# Draw a house using turtle graphics and loops.
# 10/24/2026

# Pseudocode:
# Set the background and turtle colors.
# Draw a square using a while loop.
# Move to the top of the square.
# Draw a triangle using a for loop.
# Keep the drawing window open.

# Import the library
import turtle

# Create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

pen = turtle.Turtle()
pen.pensize(5)
pen.color("deeppink")
pen.shape("turtle")

# Code to draw the shapes
for side in range(4):
    pen.forward(100)
    pen.left(90)

# While look that executes 3 times
sides = 3

while side > 0:
    pen.forward(100)
    pen.left(120)
    side = side - 1

# Wait for user to close window
win.mainloop()