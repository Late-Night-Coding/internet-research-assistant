from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Initialize the webdriver
driver = webdriver.Chrome()

# Open the website to be tested
driver.get("http://localhost:8080/")

search_box = driver.find_element(By.NAME, "query")
search_box.clear()
search_box.send_keys("dsfasdjhcfjascnfcahuisheburibwaiucrasdjkchjkxznc")
search_box.send_keys(Keys.RETURN)

assert "no" & "results" in driver.page_source

driver.close()
driver.quit()