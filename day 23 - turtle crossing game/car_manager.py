from turtle import Turtle
import random
COLORS = ["red", "orange", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    
    def create_car(self):
        random_chance = random.randint(1, 5)
        if random_chance == 3:
            new = Turtle()
            new.shape("square")
            new.color(random.choice(COLORS))
            new.penup()
            new.shapesize(1.0, 2.0)
            random_y = random.randint(-250, 250)
            new.goto(300, random_y)
            self.all_cars.append(new)

    def move_car(self):
        for car in self.all_cars:
            car.bk(self.car_speed)
    
    def level_up(self):
        self.car_speed += MOVE_INCREMENT

        