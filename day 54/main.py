# from flask import Flask
# app = Flask(__name__)
#
# @app.route('/')
# def hello_world():
#     return "Solomon Onah"
# import time
# def delay_decorator(function):
#     def wrapper_function():
#         for i in range(20):
#             print(i)
#             time.sleep(1)
#         function()
#     return wrapper_function
#
# # @delay_decorator
# def say_hello():
#     print("hello")
#
# delay = delay_decorator(say_hello)
# delay()

import time

# current_time = time.time()
# print(current_time)


def speed_calc_decorator(function):
    def speed_calc():
        first = time.time()
        function()
        second = time.time()
        print(second - first)
    return speed_calc

@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i

@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i

slow_function()
