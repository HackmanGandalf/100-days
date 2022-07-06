from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

URL = "https://mutualtrustmfb.com/wp-admin/"

USERNAME = "username"
PASSWORD = "password"

driver.get(URL)

# login
driver.find_element_by_xpath('//*[@id="user_login"]').send_keys(USERNAME)
driver.find_element_by_xpath('//*[@id="user_pass"]').send_keys(PASSWORD)
driver.find_element_by_xpath('//*[@id="wp-submit"]').click()

# navigate to counter page
driver.find_element_by_xpath('//*[@id="menu-posts-counter_numbers"]/a/div[2]').click()

driver.find_element_by_xpath('//*[@id="post-3285"]/td[1]/strong/a').click()

# update numbers
items = driver.find_elements_by_id('counter_value[]')
for item in items:
    current = int(item.get_attribute("value"))
    print(current)
    if current > 10000000:
        new = current + (15000000 * 6)
        item.clear()
        item.send_keys(new)
        print(new)
    else:
        new = current + (15 * 6)
        item.clear()
        item.send_keys(new)
        print(new)

# publish

# closer = driver.find_element_by_xpath('//*[@id="wpbody-content"]/div[3]/div[3]/button')
# time.sleep(2)
# # closer.click()
publish = driver.find_element_by_xpath('//*[@id="publish"]')
time.sleep(2)
publish.click()

time.sleep(15)

driver.quit()
