from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)

race_on = True
user_bet = screen.textinput(title="place your bets", prompt="who gon' win bro?")
all_turtles = []

position = [-70, -40, -10, 20, 50, 80]
color = ['red', 'blue', 'yellow', 'black', 'green', 'purple']

for turtle_index in range (0, 6):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.penup()
    new_turtle.color(color[turtle_index])
    new_turtle.goto(x=-230, y=position[turtle_index])
    all_turtles.append(new_turtle)


if user_bet:
    race_on = True

while race_on:
     
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"You won! {winning_color} won.")
            else:
                print(f"You lost! {winning_color} won.")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)


screen.exitonclick()