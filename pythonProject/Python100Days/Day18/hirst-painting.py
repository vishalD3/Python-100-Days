#import colorgram

#colors = colorgram.extract('C://Users//deshpandev//PycharmProjects//pythonProject//Python100Days//Day18//img//hirst.jpg'
 #                         , 30)
#rgb_colors = []
#for color in colors:
#    r = color.rgb.r
#    g = color.rgb.g
#    b = color.rgb.b
#    new_color = (r,g,b)
#    rgb_colors.append(new_color)

#print(rgb_colors)

import turtle as turtle_module
import random


turtle_module.colormode(255)
tur = turtle_module.Turtle()
turtle_module.setup(1020,1200,250,0)
tur.speed("fastest")
tur.penup()
tur.hideturtle()



color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50),
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
              (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158),
              (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129),
              (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]


tur.setheading(250)
tur.forward(300)
tur.setheading(0)

number_dot = 100
def color_dot():
    for dot_count in range(1, number_dot+1):
        tur.dot(20, random.choice(color_list))
        #tur.penup()
        tur.forward(50)
        if dot_count % 10 == 0:
            tur.setheading(90)
            tur.forward(50)
            tur.setheading(180)
            tur.forward(500)
            tur.setheading(0)

color_dot()

screen = turtle_module.Screen()
screen.exitonclick()