from turtle import Turtle as Snake

class Snakes():

    def __init__(self) -> None:
        self.snake = []
        self.create_snake()

    

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

    def move_left(self):
        self.snake[0].left(90)

    def move_right(self):
        self.snake[0].right(90)

    def move_clear(self):
        self.snake[0].clear()
        self.snake[0].penup()
        self.snake[0].home()
        self.snake[0].pendown()