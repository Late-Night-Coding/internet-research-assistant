from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# TODO find component names
driver = webdriver.Chrome('./chromedriver')
driver.get("localhost:8080")
search_bar = driver.find_element_by_name("searchbar")
search_bar.clear()
search_bar.send_keys("baseball")
search_bar.send_keys(Keys.RETURN)

# TODO: figure out what to assert
assert()
driver.close()