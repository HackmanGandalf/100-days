from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-280, 265)
        self.write_score()

    def write_score(self):
        self.write(f"Level: {self.level}", move=False, align="left", font=(FONT))
    
    def level_up(self):
        self.clear()
        self.level += 1
        self.write_score()
    
    def game_over(self):
        self.penup()
        self.goto(x=0, y=0)
        self.hideturtle()
        self.write(f"GAME OVER!", move=False, align="center", font=("Courier", 20, "normal"))
