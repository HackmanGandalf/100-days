from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&keywords=python%20developer&sortBy=R"

driver.get(URL)

sign_in = driver.find_element_by_link_text("Sign in")
sign_in.click()

username = driver.find_element_by_id("username")
username.send_keys("kesteronah@gmail.com")
password = driver.find_element_by_id("password")
password.send_keys("evangelist123")
submit = driver.find_element_by_xpath('//*[@id="organic-div"]/form/div[3]/button')
submit.click()

search_results = driver.find_elements_by_class_name("jobs-search-results__list-item")

for item in search_results:
    item.click()
    try:
        time.sleep(3)
        driver.find_element_by_class_name("jobs-apply-button--top-card").click()
        try:
            progress = driver.find_element_by_tag_name("progress")
            driver.find_element_by_class_name("artdeco-button__icon").click()
            time.sleep(3)
            driver.find_elements_by_class_name("artdeco-modal__confirm-dialog-btn")[1].click()
        except NoSuchElementException:
            driver.find_element_by_id("ember413").click()
            driver.find_element_by_class_name("artdeco-button__icon").click()
    
    except NoSuchElementException:
        pass




# driver.find_element_by_xpath('//*[@id="ember275"]/li-icon/svg').click()
# //*[@id="ember275"]/li-icon/svg
# web_developer = driver.find_element_by_link_text("Web Developer")
# web_developer.click()

# apply_now = driver.find_element_by_class_name("jobs-apply-button--top-card")
# apply_now.click()


# try:
#     mobile_number = driver.find_element_by_name("urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2444131857,21033189,phoneNumber~nationalNumber)")
#     mobile_number.send_keys("08135229159")
# # try:
# #     mobile_number = driver.find_element_by_name("urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2426759649,7164258241519019912,phoneNumber~nationalNumber)")
# #     mobile_number.send_keys("08135229159")
# except:
#     mobile_number = driver.find_element_by_name("urn:li:fs_easyApplyFormElement:(urn:li:fs_normalized_jobPosting:2413450707,9,phoneNumber~nationalNumber)")
#     mobile_number.send_keys("08135229159")

# try:
#     next_step = driver.find_element_by_id("ember407")
#     next_step.click()
# except:
#     driver.find_element_by_id("ember413").click()

# try:
#     while True:
#         next_step.click()
# except:
#     pass