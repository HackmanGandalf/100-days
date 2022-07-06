##################### Extra Hard Starting Project ######################
import pandas
import random
import smtplib
import datetime as dt

letters = [
    "100-days-of-code/day 32/letter_templates/letter_1.txt",
    "100-days-of-code/day 32/letter_templates/letter_2.txt",
    "100-days-of-code/day 32/letter_templates/letter_3.txt"]
now = dt.datetime.now()

day = now.day
month = now.month

data = pandas.read_csv("100-days-of-code/day 32/birthdays.csv")
for (index, row) in data.iterrows():
    if row.day == day and row.month == month:
        email = row.email
        name = (row["name"])
        letter = random.choice(letters)
        with open(letter) as lettera:
            contents = lettera.read()
            new_content = contents.replace("[NAME]", name)
            print(new_content)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user="email", password="password")
            connection.sendmail(
                from_addr="email",
                to_addrs=email,
                msg=f"Subject: Happy birthday {name}\n\n{new_content}"
                )







