from selenium import webdriver
import time
from selenium.common.exceptions import NoSuchElementException


chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/app/recs")

driver.find_element_by_xpath('//*[@id="t-429325247"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/button').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="t--1610880557"]/div/div/div[1]/div/div[3]/span/div[2]/button').click()
time.sleep(5)

base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

num = driver.find_element_by_class_name('inputtext')
num.send_keys("08135229159")
password = driver.find_element_by_xpath('//*[@id="pass"]')
password.send_keys('iQ<$a"5mp-Cya=#')
driver.find_element_by_name("login").click()
time.sleep(5)
driver.switch_to.window(base_window)

try:
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="t--1610880557"]/div/div/div/div/div[3]/button[1]').click()
except:
    time.sleep(5)
    driver.find_element_by_xpath('//*[@id="t--1610880557"]/div/div/div/div/div[3]/button[1]').click()

try: 
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="t--1610880557"]/div/div/div/div/div[3]/button[2]').click()
except:
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="t--1610880557"]/div/div/div/div/div[3]/button[2]').click()

try:    
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="t-429325247"]/div/div[2]/div/div/div[1]/button').click()
except:
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="t-429325247"]/div/div[2]/div/div/div[1]/button').click()

while True:
    try:
        driver.find_element_by_xpath('//*[@id="t-429325247"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button').click()
    except NoSuchElementException:
        time.sleep(5)
        driver.find_element_by_xpath('//*[@id="t-429325247"]/div/div[1]/div/main/div[1]/div/div/div[1]/div[1]/div[2]/div[2]/button').click()
