from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


# Initialize the webdriver
driver = webdriver.Chrome()

# Open the website to be tested
driver.get("http://localhost:8080/")

# Find the search input box and enter some text
search_box = driver.find_element(By.NAME, "query")
search_box.send_keys("Selenium testing")

# Submit the search query
search_box.send_keys(Keys.RETURN)


# Find all search result divs
# Find the first p element inside the first searchResult div
wait = WebDriverWait(driver, 10)
search_result = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@class="searchResult"][1]//p[1]')))



# Wait for the user to Select the lookup button
lookup_button = wait.until(EC.element_to_be_clickable((By.ID, 'lookup-btn')))
lookup_button.click()

# Get the selected text
selected_text = driver.execute_script('return window.getSelection().toString();')


# Wait for the new search results to load and check if the highlighted text is in the search query
wait.until(EC.staleness_of(search_result))
new_search_query = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@name='query']")))
try:
    assert selected_text in new_search_query.get_attribute("value")
    print("Test result: PASS.")
except AssertionError:
    print("Test result: FAIL.")
finally:
    # Close the browser window and print summary
    driver.quit()
    print("Test Complete.")

