from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the webdriver
driver = webdriver.Chrome()

# Open the website to be tested
driver.get("http://localhost:8080/")

search_box = driver.find_element(By.NAME, "query")
search_box.clear()
search_box.send_keys("baseball")
search_box.send_keys(Keys.RETURN)

#Usage of Amir's try/except
try:
    # Find all the searchResult divs and count them
    search_results = driver.find_elements(By.CLASS_NAME, "searchResult")
    num_results = len(search_results)
    assert num_results == 3
    print("Test result: PASS.")
except AssertionError:
    print("Test result: FAIL.")
finally:
    # Close the browser window and print summary
    driver.quit()
    print("Test Complete.")