from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time

FORM_LINK =  "https://forms.gle/14xpN7g3ps7K8P3aA"
ZILLOW_LINK = "https://www.zillow.com/homes/for_rent/1-_beds/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3Anull%2C%22mapBounds%22%3A%7B%22west%22%3A-122.56276167822266%2C%22east%22%3A-122.30389632177734%2C%22south%22%3A37.69261345230467%2C%22north%22%3A37.857877098316834%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A12%7D"
CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(CHROME_DRIVER_PATH)

headers = {
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"
}

request = requests.get(ZILLOW_LINK, headers=headers)
webpage = request.text
soup = BeautifulSoup(webpage, "html.parser")

prices = soup.find_all(class_="list-card-price")

price_list = []
for price in prices:
    if "+" in price.getText():
        cost1 = price.getText().split('+')[0]
        price_list.append(cost1)
    else:
        cost2 = price.getText().split('/')[0]
        price_list.append(cost2)

links = soup.select(".list-card-top a")
link_list = []

for item in links:
    href = item["href"]
    if "https" not in href:
        link_list.append(f"https://www.zillow.com{href}")
    else:
        link_list.append(href)

addresses = soup.find_all(class_="list-card-addr")
address_list = []

for address in addresses:
    address_list.append(address.getText())

for i in range(len(address_list)):
    driver.get(FORM_LINK)
    time.sleep(3)
    s_address = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    s_price = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    s_link = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    s_address.send_keys(address_list[i])
    s_price.send_keys(price_list[i])
    s_link.send_keys(link_list[i])

    driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span/span').click()
