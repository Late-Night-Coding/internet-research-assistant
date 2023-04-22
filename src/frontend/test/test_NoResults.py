from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the webdriver
driver = webdriver.Chrome()

# Open the website to be tested
driver.get("http://localhost:8080/")

search_box = driver.find_element(By.NAME, "query")
search_box.clear()
search_box.send_keys("dsfasdjhcfjascnfcahuisheburibwaiucrasdjkchjkxznc")
search_box.send_keys(Keys.RETURN)

#Amir's try/catch is his test cases
try:
    error_message = driver.find_element(By.XPATH, "//h1")
    assert error_message.text == "413"
    print("Test result: PASS.")
except AssertionError:
    print("Test result: FAIL.")
finally:
    # Close the browser window and print summary
    driver.quit()
    print("Test Complete.")