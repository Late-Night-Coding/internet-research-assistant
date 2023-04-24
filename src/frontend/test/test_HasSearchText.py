from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the webdriver
driver = webdriver.Chrome()

# Open the website to be tested
driver.get("http://localhost:8080/")

# Make a search
search_box = driver.find_element(By.NAME, "query")
search_box.clear()
search_box.send_keys("baseball")
search_box.send_keys(Keys.RETURN)

#Use of Amir's try/except method
try:
    #Gets stuff from the website
    search_results = driver.find_elements(By.CLASS_NAME, "searchResult")
    search_links = driver.find_elements(By.CLASS_NAME, "linksList_link") 

    #Asserts whether or not relevant items are on the website or not
    assert len(search_results) != 0
    assert len(search_links) != 0
    print("Test result: PASS.")
except AssertionError:
    print("Test result: FAIL.")
finally:
    # Close the browser window and print summary
    driver.quit()
    print("Test Complete.")