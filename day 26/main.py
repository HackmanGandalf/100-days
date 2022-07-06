# numbers = [1, 2, 3]
# new_list = [n + 1 for n in numbers]
# print(new_list)


# name = "Angela"
# new_list = [letter for letter in name]
# print(new_list)

# print([item * 2 for item in range(1, 5)])
import random
# names = ["ALex", "Beth", "Caroline", "Dave", "Elanor", "Fredie"]
# # new_list = [name for name in names if (len(name) <= 4)]
# # print(new_list)
# new_list = [name.upper() for name in names if len(name) >= 5]
# print(new_list)

# numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

# square_numbers = [num * num for num in numbers]
# even_numbers = [num for num in numbers if (num%2 == 0)]
# print(even_numbers)

# student_scores = {name:random.randint(1, 100) for name in names}

# passed_students = {student:score for (student, score) in student_scores.items() if score > 70}
# print(passed_students)

# sentence = "What is the Airspeed Velocity of an Unladen Swallow"
# lister = sentence.split()
# result = {word:len(word) for word in lister}
# print(result)

# weather_c = {
#     "Monday":12,
#     "Tuesday": 14,
#     "Wednesday": 15,
#     "Thursday": 14,
#     "Friday": 21,
#     "Saturday": 22,
#     "Sunday": 24,
# }

# weather_f = {day:((temp *9/5) + 32) for (day, temp) in weather_c.items()}
# print(weather_f)

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

import pandas

student_data_frame = pandas.DataFrame(student_dict)
#print(student_data_frame)
# for (key, value) in student_data_frame.items():
#     print(key)

for (index, row) in student_data_frame.iterrows():
    if row.student == "Angela":
        print(row.score)