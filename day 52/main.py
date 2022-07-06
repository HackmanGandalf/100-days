from selenium import webdriver
import time
import selenium.common.exceptions

chrome_driver_path = "C:\Development\chromedriver.exe"

class InstaFollower:
    def __init__(self, driver):
        self.driver = webdriver.Chrome(chrome_driver_path)
        
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(15)
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys('username')
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("password")
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button').click()
        time.sleep(15)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button').click()
        time.sleep(15)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]').click()
    
    def find_followers(self):
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input').send_keys('herosunited')
        time.sleep(10)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]').click()
        time.sleep(5)
        self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[3]/a').click()
        time.sleep(10)
    
    def follow(self):
        list = self.driver.find_elements_by_css_selector("li button")
        print(len(list))
        for item in list:
            item.click()
            time.sleep(2)

instabot = InstaFollower(chrome_driver_path)

instabot.login()
instabot.find_followers()
instabot.follow()