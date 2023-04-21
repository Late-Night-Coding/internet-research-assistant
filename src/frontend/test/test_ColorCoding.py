from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.color import Color
import time

# Initialize the webdriver
driver = webdriver.Chrome()

# Open the website to be tested
driver.get("http://localhost:8080/")

# Make a search
search_box = driver.find_element(By.NAME, "query")
search_box.clear()
search_box.send_keys("baseball")
search_box.send_keys(Keys.RETURN)

#Find links
links = driver.find_elements(By.CLASS_NAME, "linksList_link")

for link in links:
    hue = link.getCssValue("link-hue")
    hueHex = Color.from_string(hue)
    if(hueHex == '#FFFFFF'):
        assert False

assert True

driver.close()
driver.quit()