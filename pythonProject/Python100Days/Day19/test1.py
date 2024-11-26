import turtle as t
from turtle import Screen
myTurtle = t.Turtle()


def move_forward():
    myTurtle.forward(10)



myScreen = t.Screen()
myScreen.listen()
myScreen.onkey(key="space",fun=move_forward)
myScreen.exitonclick()
