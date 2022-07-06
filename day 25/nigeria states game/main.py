import turtle
import pandas
from scoreboard import Guess
scoreboard = Guess()
screen = turtle.Screen()
screen.title("Nigerian States Games")
image = "100-days-of-code/day 25/nigeria states game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()



data = pandas.read_csv("100-days-of-code/day 25/nigeria states game/50_states.csv")


state_list = data.state.to_list()
guessed = []
game_end = False
while game_end != True:
    
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break
    if answer_state in state_list:
        state = data[data.state == f"{answer_state}"]
        x = float(state.x)
        y = float(state.y)
        position = (x, y)
        #writer = Guess(position)
        guessed.append(answer_state)
        writer = turtle.Turtle()
        writer.penup()
        writer.hideturtle()
        writer.goto(position)
        # self.write_score()
        writer.write(f"{answer_state}", align="center", font=("Courier", 9, "normal"))
        print(guessed)
    # writer()
    # answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").capitalize()
        
    else:
        print("false")
        answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").capitalize()

    if len(guessed) == 37:
        scoreboard.victory()
        game_end = True

states_to_learn = [state for state in state_list if state not in guessed]
# for state in state_list:
#     if state in guessed:
#         continue
#     states_to_learn.append(state)

learn = pandas.DataFrame(states_to_learn)
learn.to_csv("100-days-of-code/day 25/nigeria states game/learn these.csv")





screen.exitonclick()