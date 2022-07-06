from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

save = "0.1251|492|55|3681|37|3593|21|3723|5|3222|0|7000|0|50000|0|1000000|0|123456789"

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://en.wikipedia.org/wiki/Main_Page")
# driver.get("http://secure-retreat-92358.herokuapp.com/")
driver.get("http://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element_by_css_selector("#cookie")

items = driver.find_elements_by_css_selector("#store div")
item_id = [item.get_attribute("id") for item in items ]

timeout = time.time() + 60 * 5

should_click = True

while should_click:
    cookie.click()

    if time.time() > timeout:
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_price = []

        for item in all_prices:
            element_text = item.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_price.append(cost)
        
        cookie_upgrades = {}
        for n in range(len(item_price)):
            cookie_upgrades[item_price[n]] = item_id[n]
        
        money = driver.find_element_by_id("money").text
        if "," in money:
            remover = money.replace(",", "")
        cookie_count = int(remover)
        
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id
        
        
        # highest_affordable = max(affordable_upgrades)
        # print(highest_affordable)
        # to_buy = affordable_upgrades[highest_affordable]

        # driver.find_element_by_id(to_buy).click()

        try:    
            highest_price_affordable_upgrade = max(affordable_upgrades)
            to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

            driver.find_element_by_id(to_purchase_id).click()
        
        except ValueError:
            continue

        # driver.find_element_by_id(purchasable_upgrades[max(purchasable_upgrades)]).click()
    

# driver.close()

