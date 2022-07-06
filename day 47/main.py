from bs4 import BeautifulSoup
import requests
import smtplib

url = "https://www.amazon.com/Samsung-Galaxy-A31-128GB-4GB-International/dp/B087CCGB54/ref=sr_1_1?dchild=1&keywords=samsung&nav_sdd=aps&pd_rd_r=1d745308-8de9-41a6-8cdb-a597a02c306e&pd_rd_w=yBEzO&pd_rd_wg=J2A8J&pf_rd_p=d6955c87-af17-429d-b87f-553c0e6191e5&pf_rd_r=599BRP7WP9DTHEPYJ7Y4&qid=1615290088&refinements=p_36%3A14674875011&s=wireless&sr=1-1"

headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}

response = requests.get(url, headers=headers)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

price = float(soup.find(name="span", class_="a-size-medium a-color-price priceBlockBuyingPriceString").getText().split("$")[1])

if price == price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user="email", password="password")
        connection.sendmail(
            from_addr="email",
            to_addrs="email",
            msg=f"Subject:Low Price Alert!\n\nSamsung Galaxy A31 now costs ${price}!. Log into Amazon to buy now.".encode('utf-8')
        )