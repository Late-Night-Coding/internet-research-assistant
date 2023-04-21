from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Initialize the webdriver
driver = webdriver.Chrome()

# Open the website to be tested
driver.get("http://127.0.0.1:8080/")

# Find the search input box and enter more than 200 characters
search_box = driver.find_element(By.NAME, "query")
search_box.send_keys("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed auctor ligula velit, sit amet aliquet turpis rhoncus vel. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed vitae nisl id ex consectetur maximus vel eget lacus. Phasellus bibendum ex elit, eget efficitur magna dignissim vel. Donec vel mi tortor. Nullam eu purus auctor, malesuada turpis id, facilisis dolor. Proin maximus leo non diam blandit, non pharetra odio bibendum. Donec feugiat eros odio, et tristique tellus placerat quis. Vivamus vel mauris ut metus commodo sagittis. Donec in malesuada magna. Vivamus sit amet elit quis est pulvinar interdum eu quis velit. Nullam bibendum congue ex, nec porttitor dolor tincidunt vel Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed auctor ligula velit, sit amet aliquet turpis rhoncus vel. Pellentesque habitant morbi tristique senectus et netus et malesuada fames ac turpis egestas. Sed vitae nisl id ex consectetur maximus vel eget lacus. Phasellus bibendum ex elit, eget efficitur magna dignissim vel. Donec vel mi tortor. Nullam eu purus auctor, malesuada turpis id, facilisis dolor. Proin maximus leo non diam blandit, non pharetra odio bibendum. Donec feugiat eros odio, et tristique tellus placerat quis. Vivamus vel mauris ut metus commodo sagittis. Donec in malesuada magna. Vivamus sit amet elit quis est pulvinar interdum eu quis velit. Nullam bibendum congue ex, nec porttitor dolor tincidunt vel")

# Submit the search query
search_box.send_keys(Keys.RETURN)

# Wait for the page to load and check if an error message is displayed
time.sleep(5)
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
