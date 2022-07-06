from selenium import webdriver

chrome_driver_path = "C:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

# driver.get("https://www.amazon.com/Samsung-Galaxy-A31-128GB-4GB-International/dp/B087CCGB54/ref=sr_1_1?dchild=1&keywords=samsung&nav_sdd=aps&pd_rd_r=1d745308-8de9-41a6-8cdb-a597a02c306e&pd_rd_w=yBEzO&pd_rd_wg=J2A8J&pf_rd_p=d6955c87-af17-429d-b87f-553c0e6191e5&pf_rd_r=599BRP7WP9DTHEPYJ7Y4&qid=1615290088&refinements=p_36%3A14674875011&s=wireless&sr=1-1")
driver.get("https://www.python.org/")
# price = driver.find_element_by_id("priceblock_ourprice").split("$")[0]
# print(price.text)

event_times = driver.find_elements_by_css_selector(".event-widget time")
dates_list = [date.text for date in event_times]

event_names = driver.find_elements_by_css_selector(".event-widget a")
events_list = [event.text for event in event_names]
events = {}

for n in range(len(event_times)):
    events[n] = {
        "time" : dates_list[n],
        "name" : events_list[n],
    }

print(events)

# driver.close()
driver.quit()