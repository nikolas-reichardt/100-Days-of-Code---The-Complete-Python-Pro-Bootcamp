from turtle import Turtle, Screen
import random

# tim = Turtle()
# screen = Screen()

# def move_forward():
#     tim.forward(10)

# def move_backward():
#     tim.backward(10)

# def move_counter_clock():
#     tim.setheading(tim.heading()-10)

# def move_clock():
#     tim.setheading(tim.heading()+10)

# def move_clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()

# screen.listen()
# screen.onkey(key="w", fun=move_forward)
# screen.onkey(key="s", fun=move_backward)
# screen.onkey(key="a", fun=move_counter_clock)
# screen.onkey(key="d", fun=move_clock)
# screen.onkey(key="c", fun=move_clear)
# screen.exitonclick()

screen= Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")
colors =["red", "green", "purple", "cyan", "black", "blue"]

def create_turtles(colors):
    position = -100
    turtles={}
    for i in range(len(colors)):
        turtles[i] = Turtle(shape="turtle")
        turtles[i].color(colors[i])
        turtles[i].penup()
        turtles[i].goto(x=-230, y=position)
        position += 30
    return turtles

turtles = create_turtles(colors)

def start_race(turtles):
    game_on = True
    while game_on:
        for i in turtles:
            turtles[i].forward(random.randint(0,30))
            # Get the turtle's current position (x, y)
            current_x, current_y = turtles[i].position()
            if current_x > 200:
                game_on = False
                print(f"Turtel {turtles[i].pencolor()} won the race!")
                return turtles[i].pencolor()
        

if start_race(turtles) == user_bet:
    print("Good choice. You've won the bet!")
else:
    print("Poor choice. You've lost the bet!")


screen.exitonclick()