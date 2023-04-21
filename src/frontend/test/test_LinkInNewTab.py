from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse


chrome_options = Options()
chrome_options.add_argument("--ignore-certificate-errors")

# Initialize the webdriver
driver = webdriver.Chrome(options=chrome_options)

# Initialize the webdriver

# Open the website to be tested
driver.get("http://localhost:8080/")

# Find the search input box and enter some text
search_box = driver.find_element(By.NAME, "query")
search_box.send_keys("Selenium testing")

# Submit the search query
search_box.send_keys(Keys.RETURN)

# Wait for the search results to load and find the indexed search result link
search_result = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//div[@class="linksList"]/a[2]')))
search_url = search_result.get_attribute("href")

# Click the search result link to open a new tab
search_result.click()
driver.switch_to.window(driver.window_handles[2])
# Wait for the new tab to open and switch to it
try:
    WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
  

except TimeoutException:
    print("Timed out waiting for the new window to open")
    opened_link = driver.current_url


# Parse links
parsed_url1 = urlparse(search_url)
parsed_url2 = urlparse(opened_link)


# Check if the URL of the newly opened tab matches the clicked link
try:
    assert parsed_url2 ==  parsed_url2
    print("Test result: PASS.")
except AssertionError:
    print("Test result: FAIL.")
finally:
    # Close the browser window and print summary
    driver.close()

    driver.quit()
    print("Test Complete.")

