from turtle import Turtle as Snake

class Snakes():

    def __init__(self) -> None:
        self.snake = []
        self.create_snake()

    def add_snake_body(self):
        new_snake_body = Snake()
        new_snake_body.color("white")
        new_snake_body.shape("square")
        new_snake_body.penup()

        # Position the new segment at the location of the last segment
        last_segment = self.snake[-1]  # Get the last segment of the snake
        new_snake_body.goto(last_segment.xcor(), last_segment.ycor())  # Place the new segment behind the last segment
        self.snake.append(new_snake_body)

    def create_snake(self):  
        for i in range(3):
            print(i)
            self.snake.append(Snake())
            self.snake[i].color("white")
            self.snake[i].shape("square")
            self.snake[i].penup()
            if i > 0:
                self.snake[i].setx(self.snake[i-1].xcor() - 20)

    def move_snake(self):
        # match direction:
        #     case "a":
        #         for i in self.snake:
        #             self.snake[i].
        #     case "d":
        #         self.forward(100)
        for i in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[i - 1].xcor()
            new_y = self.snake[i - 1].ycor()
            self.snake[i].goto(new_x, new_y) 
        self.snake[0].forward(20)

 # Direction control methods
    def go_up(self):
        if self.snake[0].heading() != 270:  # Prevent going directly opposite
            self.snake[0].setheading(90)    # Set heading to "up"

    def go_down(self):
        if self.snake[0].heading() != 90:
            self.snake[0].setheading(270)   # Set heading to "down"

    def go_left(self):
        if self.snake[0].heading() != 0:
            self.snake[0].setheading(180)   # Set heading to "left"

    def go_right(self):
        if self.snake[0].heading() != 180:
            self.snake[0].setheading(0)     # Set heading to "right"