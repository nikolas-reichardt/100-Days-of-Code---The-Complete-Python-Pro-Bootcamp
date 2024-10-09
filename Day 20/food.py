from turtle import Turtle
import random
import math
from scoreboard import Scores

class Fooder(Turtle):
    def __init__(self) -> None:
        super().__init__()
        #self.circle = Turtle()
        self.shape("circle")
        self.color("red")
        self.create_points()
    score_on_board = Scores()


    def create_points(self):
        self.penup()
        self.setposition(random.randint(-260,260),random.randint(-260,260))
        self.score_on_board.write_score()
        

    def check_snake_pos(self, x_cords, y_cords):
        # Calculate the distance between the snake's head and the circle
        distance = math.sqrt(
            (x_cords - self.xcor())**2 +
            (y_cords - self.ycor())**2
        )
        # If the distance is less than a certain threshold, trigger point creation
        if distance < 20:  # Assuming 20 is a reasonable threshold based on your snake size
            self.create_points()