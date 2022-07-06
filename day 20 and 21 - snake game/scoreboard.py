from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(x=0, y=270)
        self.hideturtle()
        self.write_score()
    
    def write_score(self):
        self.write(f"Score: {self.score}", move=False, align="center", font=("Courier", 20, "normal"))
        
    def increase_score(self):
        self.clear()
        self.score += 1
        self.write_score()
    
    def game_over(self):
        self.penup()
        self.color("white")
        self.goto(x=0, y=0)
        self.hideturtle()
        self.write(f"GAME OVER!", move=False, align="center", font=("Courier", 20, "normal"))

        