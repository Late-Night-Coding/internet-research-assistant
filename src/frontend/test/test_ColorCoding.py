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

#Used from Amir's test cases
try:
    for link in links:
        #get the RGBA value of the link class background
        hue = link.value_of_css_property("background-color")

        #convert the RGBA to HEX
        hueHex = Color.from_string(hue).hex
        if(hue == '#ffffff'):
            assert False
    assert True
    print("Test result: PASS.")
except AssertionError:
    print("Test result: FAIL.")
finally:
    # Close the browser window and print summary
    driver.quit()
    print("Test Complete.")