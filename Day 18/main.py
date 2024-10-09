from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.color("green")
timmy.shape("turtle")

# for _ in range(4):
#     timmy.forward(100)
#     timmy.right(90)

#timmy.left(180)
#timmy.setheading(0)

# for _ in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

rotate = 360
max_corners = 3
corners = 0
for i in range(8):
    while corners < max_corners:
        timmy.forward(100)
        timmy.right(360/(i+3))
        corners += 1
    max_corners += 1
    corners = 0
    timmy.pencolor(random.choice(["green","red","cyan","blue","yellow","black"]))


screen = Screen()
screen.exitonclick()

