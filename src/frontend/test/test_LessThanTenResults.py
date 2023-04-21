from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the webdriver
driver = webdriver.Chrome()

# Open the website to be tested
driver.get("http://localhost:8080/")

search_box = driver.find_element(By.NAME, "query")
search_box.send_keys("Selenium testing")

# Submit the search query
search_box.send_keys(Keys.RETURN)
time.sleep(2)

# Find all the searchResult divs and count them
search_results = driver.find_elements(By.CLASS_NAME, "searchResult")
num_results = len(search_results)

# Check if there are less than ten searchResult divs
try:
    assert num_results <  10
    print("Test result: PASS.")
except AssertionError:
    print("Test result: FAIL.")
finally:
    # Close the browser window
    driver.close()
    driver.quit()
    print("Test Complete.")