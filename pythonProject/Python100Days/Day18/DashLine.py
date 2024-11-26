from turtle import Turtle,Screen

my_turtle = Turtle()
my_turtle.color("red")


for _ in range(10):
    my_turtle.forward(10)
    my_turtle.pendown()
    my_turtle.forward(10)
    my_turtle.penup()


myScreen = Screen()
myScreen.exitonclick()

