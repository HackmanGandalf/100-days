from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.color("white")
        self.penup()
        self.score = 0
        self.goto(position)
        self.hideturtle()
        self.write_score()



    def write_score(self):
        self.write(f"{self.score}", move=False, align="center", font=("Courier", 20, "normal"))
        
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write_score()
    