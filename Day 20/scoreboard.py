from turtle import Turtle

class Scores():
    def __init__(self) -> None:
        self.scoreboard = Turtle()
        self.score = -1
        self.scoreboard.hideturtle()
        self.scoreboard.color("white")
        self.scoreboard.penup()
        self.scoreboard.setposition(0.00, 260.00)

    def write_score(self):
        self.score += 1
        self.scoreboard.clear()
        self.scoreboard.write(f"Your score: {self.score}", move=False, align='center', font=('Arial', 14, 'normal'))