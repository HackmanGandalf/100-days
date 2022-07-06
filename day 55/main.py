from flask import Flask
import random

app = Flask(__name__)

guess = random.randint(0,9)
print(guess)
# def make_bold(function):
#     def bold():
#         return "<strong>" + function() + "</strong>"
#     return bold
#
# def make_underline(function):
#     def underline():
#         return "<u>" + function() + "</u>"
#     return underline
#
# def make_emphasis(function):
#     def emphasize():
#         return "<em>" + function() + "</em>"
#     return emphasize

# @app.route('/')
# @make_bold
# @make_underline
# @make_emphasis
# def hello():
#     return "Bye"
#

@app.route('/')
def greet():
    return "<h1 style='color: black'> Welcome the number guessing game! Guess a number to play</h1>" \
           "<img src='https://media3.giphy.com/media/Kehzyp9EFa2IYDte8P/giphy.gif'>"

@app.route('/<int:number>')
def bye(number):
    if number < guess:
        return "<h1 style='color: red'> You guessed too low! </h1>" \
               "<img src='https://media0.giphy.com/media/3oKHWfu68Q6XOz2I6Y/giphy.gif'>"
    if number == guess:
        return "<h1 style='color: green'> You guessed correctly! </h1>" \
               "<img src='https://media.tenor.com/images/0a81b89954678ebe228e15e35044f7a5/tenor.gif'>"
    if number > guess:
        return "<h1 style='color: red'> You guessed too high! </h1>" \
               "<img src='https://media.tenor.com/images/533b9f5eea4b2d7a05f4afc18a49da64/tenor.gif'>"

if __name__ == "__main__":
    app.run(debug=True)

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.is_logged_in = False
#
# def authenticator_decorator(function):
#     def wrapper(*args):
#         if args[0].is_logged_in == True:
#             function(args[0])
#     return wrapper
#
# @authenticator_decorator
# def create_blog_post(User):
#     print(f"This is {User.name}'s blog")
#
# new_user = User("John")
# new_user.is_logged_in = True
# create_blog_post(new_user)