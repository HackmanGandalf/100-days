from turtle import Turtle


class Guess(Turtle):
    def __init__(self):
        super().__init__()
        # self.penup()
        # self.hideturtle()
        # self.goto(position)
        # # self.write_score()
        # self.write("hello", align="center", font=("Courier", 9, "normal"))

    def victory(self):
        self.penup()
        self.hideturtle()
        self.goto(0,0)
        # self.write_score()
        self.write("Congratulations! You win!", align="center", font=("Courier", 30, "normal"))