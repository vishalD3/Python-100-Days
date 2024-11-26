from turtle import Screen
import turtle as t
import random

my_turtle = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b= random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


direction = [0, 90, 180, 270]
my_turtle.pensize(10)
my_turtle.speed("fastest")
for _ in range(200):
    my_turtle.color(random_color())
    my_turtle.forward(30)
    my_turtle.setheading(random.choice(direction))




myScreen = Screen()
myScreen.exitonclick()
