from turtle import Screen
from snake import Snakes
from food import Fooder
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Amazing Snake")
screen.tracer(0)  # Turn off automatic updates

new_snake = Snakes()
new_food = Fooder()

game_is_on = True
screen.listen()

screen.onkey(key="a", fun=new_snake.move_left)
screen.onkey(key="d", fun=new_snake.move_right)
screen.onkey(key="c", fun=new_snake.move_clear)      

while game_is_on:
    screen.update()
    time.sleep(0.1)
    new_snake.move_snake()
    new_food.check_snake_pos(new_snake.snake[0].xcor(), new_snake.snake[0].ycor())
    game_is_on = not (new_snake.snake[0].xcor() > 290 or new_snake.snake[0].xcor() < -290 or new_snake.snake[0].ycor() > 290 or new_snake.snake[0].ycor() < -290)

screen.exitonclick()
    