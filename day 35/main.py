import requests
from twilio.rest import Client
import smtplib

api_key = "api_key"
MY_LAT = 8.874217
MY_LONG = 7.218969
parameters = {
    #"q": "Abuja",
    "appid": api_key,
    "lat": MY_LAT,
    "lon": MY_LONG,
    "exclude":"current,minutely,daily,alerts"

}

account_sid = "account_sid"
auth_token = "auth_token"


response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather = response.json()
weather_slice = weather["hourly"][:12]

need_an_umbrella = False 
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        need_an_umbrella = True


if need_an_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="You are going to need an umbrella today. Bring one. ☂️",
                     from_="+18315401997",
                     to='to'
                 )
    print(message.status)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="user", password="password")
        connection.sendmail(
            from_addr="from_addr",
            to_addrs="to_addrs",
            msg="Subject: ☂️  \n\nYou are going to need an umbrella today. Bring one. ☂️"
                    )
        connection.sendmail(
            from_addr="from_addrs",
            to_addrs="to_addrs",
            msg="Subject: ☂️  \n\nYou are going to need an umbrella today. Bring one. ☂️"
        )