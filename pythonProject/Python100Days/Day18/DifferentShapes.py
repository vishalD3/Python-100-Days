from turtle import Turtle,Screen
import random

my_turtle = Turtle()

color = ["navy","greenyellow","crimson","maroon","mediumslateblue","coral","darksalmon","gold","olivedrab"]

def draw_shapes(num_side):
    for _ in range(num_side):
        angle = 360 / num_side
        my_turtle.forward(100)
        my_turtle.right(angle)

for shape_sides_n in range (3 , 11):
    my_turtle.color(random.choice(color))
    draw_shapes(shape_sides_n)

myScreen = Screen()
myScreen.exitonclick()