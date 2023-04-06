import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BrowserTest(unittest.TestCase):

    driver:webdriver
    def setUp(self):
        self.driver = webdriver.Chrome('./chromedriver')
 
    
    def testHasResults(self):
        driver = self.driver
        driver.get("localhost:8080")
        search_bar = driver.find_element_by_name("searchbar")
        search_bar.clear()
        search_bar.send_keys("baseball")
        search_bar.send_keys(Keys.RETURN)

        assert driver.find_element_by_name("searchResults") is not 0
 
    def tearDown(self):
        self.driver.close()
    