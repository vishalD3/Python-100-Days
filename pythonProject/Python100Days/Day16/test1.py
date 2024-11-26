#creating object
#Calling methods

from turtle import Turtle, Screen

main = Turtle()
print(main)
main.shape("turtle")
main.color("red")
main.forward(100)

myScreen = Screen()
myScreen.exitonclick()