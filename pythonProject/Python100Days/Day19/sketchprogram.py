from turtle import  Turtle, Screen

t = Turtle()
myScreen = Screen()

def move_forward():
    t.forward(10)

def backward():
    t.backward(10)

def turn_right():
    t.right(10)

def turn_left():
    t.left(10)

def clear():
    t.clear()
    t.penup()
    t.home()
    t.pendown()


def draw_sketch():
    myScreen.listen()
    myScreen.onkey(key="w",fun=move_forward)
    myScreen.onkey(key="s",fun=backward)
    myScreen.onkey(key="d",fun=turn_right)
    myScreen.onkey(key="a",fun=turn_left)
    myScreen.onkey(key="c", fun=clear)

draw_sketch()
myScreen.exitonclick()