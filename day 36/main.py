import requests
from twilio.rest import Client
import smtplib
import html

newsapi = "newsapi"
api_key = "api_key"

account_sid = "accound_sid"
auth_token = "auth_token"

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

parameters = {
    "symbol": STOCK_NAME,
    "function":"TIME_SERIES_DAILY",
    "apikey": api_key
}

response = requests.get(url=STOCK_ENDPOINT, params=parameters)
response.raise_for_status()
stock_history = response.json()["Time Series (Daily)"]

data_list = [value for (key, value) in stock_history.items()]
yesterday_data = data_list[1]
yesterday_closing = float(yesterday_data["4. close"])

two_days_ago = data_list[2]
two_days_ago_closing = float(two_days_ago["4. close"])

positive_diff = yesterday_closing - two_days_ago_closing
up_down = None
if positive_diff > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

percentage_diff = round((positive_diff/yesterday_closing) * 100)

if percentage_diff > 5:
    parameters = {
        "qInTitle": STOCK_NAME,
        "apikey": newsapi
    }

    news_request = requests.get(url=NEWS_ENDPOINT, params=parameters)
    articles = news_request.json()["articles"]
    three_articles = articles[:3]

    new_list = [f"{STOCK_NAME}: {up_down}{percentage_diff}% \nHeadline: {item['title']}. \nBrief: {item['description']}. \nRead more at {item['url']}" for item in three_articles]
    
    for item in new_list:
        client = Client(account_sid, auth_token)
        message = client.messages \
                    .create(
                        body=item,
                        from_="+18315401997",
                        to='phone'
                    )

    
        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user="email", password="shirereckoning")
        #     connection.sendmail(
        #         from_addr="email",
        #         to_addrs="email",
        #         msg=item
        #                 )
            # connection.sendmail(
            #     from_addr="email",
            #     to_addrs="email",
            #     msg="Subject: Market Update  \n\nYou are going to need an umbrella today. Bring one. ☂️"
            # )


#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

