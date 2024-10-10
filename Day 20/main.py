from turtle import Screen, Turtle
from snake import Snakes
from food import Fooder
import time

def start_game(x, y, start_button, new_snake, new_food):
    # Entferne den Start-Text und starte das Spiel
    start_button.clear()  # Entferne den "Play Game" Text
    run_game(new_snake, new_food)  # Starte das Spiel (z. B. die Funktion, die das Spiel startet)

def run_game(new_snake, new_food):
    game_is_on = True
    screen.listen()

    screen.onkey(key="Up", fun=new_snake.go_up)
    screen.onkey(key="Down", fun=new_snake.go_down)
    screen.onkey(key="Left", fun=new_snake.go_left)
    screen.onkey(key="Right", fun=new_snake.go_right)

    while game_is_on:
        screen.update()
        time.sleep(0.1)
        new_snake.move_snake()
        x = new_snake.snake[0].xcor()
        y = new_snake.snake[0].ycor()
        if new_food.check_snake_pos(x, y):
            new_snake.add_snake_body()
        game_is_on = not (x > 290 or x < -290 or y > 290 or y < -290)

    # Wenn das Spiel zu Ende ist, lösche alle Turtle-Objekte und starte neu
    clear_game(new_snake, new_food)

def clear_game(new_snake, new_food):
    # Clear alle Turtles und reset
    for segment in new_snake.snake:
        segment.hideturtle()  # Verstecke alle Schlangen-Segmente
        segment.clear()  # Lösche alle gezeichneten Linien und Objekte
    new_snake.snake.clear()  # Lösche alle Schlangen-Segmente aus der Liste

    # Futter clearen
    new_food.hideturtle()
    new_food.clear()
    new_food.clear_points()  # Clear das Scoreboard (über Fooder)

    #Zeige die Aktualisierungen auf dem Bildschirm
    screen.update()

    # Starte das Spiel neu
    reinit()

def reinit():
    # Erstelle die Zutaten des Spieles
    new_snake = Snakes()
    new_food = Fooder()
    # Erstelle den Turtle, der den "Play Game"-Button darstellt
    start_button = Turtle()
    start_button.hideturtle()
    start_button.penup()
    start_button.color("white")
    start_button.goto(0, 0)  # Positioniere den "Play Game"-Text in der Mitte des Bildschirms
    start_button.write("Play Game", align="center", font=("Arial", 24, "normal"))
    # Füge eine Funktion hinzu, die auf Mausklicks auf dem Bildschirm reagiert
    screen.onclick(lambda x, y: start_game(x, y, start_button, new_snake, new_food))

# Setze das Turtle-Screen auf
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Amazing Snake")
screen.tracer(0)  # Turn off automatic updates
reinit()

# Starte den Haupt-Event-Loop von Turtle
screen.mainloop()
screen.exitonclick()






    