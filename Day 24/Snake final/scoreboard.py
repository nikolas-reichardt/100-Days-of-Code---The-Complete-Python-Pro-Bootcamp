from turtle import Turtle
import os

#initialize a file to store the highscore
# Öffne die Datei mit einem Kontextmanager
DIR = os.path.dirname(__file__)  # Directory of the current script
PATH = os.path.join(DIR, "data.txt")

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.read_highscore()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open(PATH, "w") as file:
                file.write(str(self.highscore))
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def read_highscore(self):
        try:
            # Attempt to open and read the file
            with open(PATH, "r") as file:
                content = file.read()

                # Check if the file content is empty
                if not content:
                    raise ValueError("File is empty.")
                
                # Assign the content to highscore or do other processing
                self.highscore = int(content)

        except FileNotFoundError:
            # This will catch the case where the file doesn't exist
            print(f"Error: The file at '{PATH}' was not found.")
            self.highscore = 0  # You can set a default value or handle it as needed

        except ValueError as e:
            # This will catch the case where the file is empty or has invalid data
            print(f"Error: {e}")
            self.highscore = 0  # Set default value in case of an error