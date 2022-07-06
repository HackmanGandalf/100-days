import smtplib
import datetime as dt
import random

my_email = "email"
password = "password"

now = dt.datetime.now()
day_of_week = now.weekday()


if day_of_week == 2:
    with open("100-days-of-code/day 32/quotes.txt") as quotes:
        all_quotes = quotes.readlines()
        single_quote = random.choice(all_quotes)
    
    print(single_quote)
    
    with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr="from_addr",
            to_addrs="to_addrs",
            msg=f"Subject:Mic Check \n\n {single_quote}"
            )