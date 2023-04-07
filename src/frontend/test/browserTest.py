import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class BrowserTest(unittest.TestCase):

    longJarble = "This Text is over 4000 characters long, so the rest of it will be nonsense. abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789abcdefghijklmnopqrstuvwxyz0123456789 "
    driver:webdriver

    def setUp(self):
        self.driver = webdriver.Chrome()
        #change this address to whatever address you are testing on
        self.driver.get("localhost:8080")

    def testDeniesLargeSearch(self):
        driver = self.driver
        search_bar = driver.find_element_by_name("searchbar")
        search_bar.clear()
        search_bar.send_keys(self.longJarble)
        search_bar.send_keys(Keys.RETURN)

        assert "no" & "results" in driver.page_source

    def testSearchFromSelection(self):
        driver = self.driver
        search_bar = driver.find_element_by_name("searchbar")
        search_bar.clear()
        search_bar.send_keys("baseball")
        search_bar.send_keys(Keys.RETURN)

        driver.find_element(By.TAG_NAME, 'h2').select()
        driver.find_element(By.CLASS_NAME, 'lookup').click()

        browserTabs = driver.WindowHandles
        assert driver.SwitchTo().Window(browserTabs[1])

    def testLinkInNewTab(self):
        driver = self.driver
        search_bar = driver.find_element_by_name("searchbar")
        search_bar.clear()
        search_bar.send_keys("baseball")
        search_bar.send_keys(Keys.RETURN)

        driver.find_element(By.PARTIAL_LINK_TEXT, 'ba').click()

        browserTabs = driver.WindowHandles
        assert driver.SwitchTo().Window(browserTabs[1])

    def testLessThanTenResults(self):
        driver = self.driver
        search_bar = driver.find_element_by_name("searchbar")
        search_bar.clear()
        search_bar.send_keys("baseball")
        search_bar.send_keys(Keys.RETURN)

        searchResults = driver.find_element(By.CLASS_NAME, "searchResults")
        assert  searchResults.len() < 10

    #TODO test search relevance
    #not entirely sure how to do this, so I left this function as a dummy
    def testRelevantSearchOrder(self):
        assert 1 == 1

    def testThreeResultSections(self):
        driver = self.driver
        search_bar = driver.find_element_by_name("searchbar")
        search_bar.clear()
        search_bar.send_keys("baseball")
        search_bar.send_keys(Keys.RETURN)

        assert driver.find_element(By.CLASS_NAME, "searchResult")
        assert driver.find_element(By.TAG_NAME, 'p')
        assert driver.find_element(By.CLASS_NAME, "linksList")


    #TODO test reasoning
    #implementation dependent, currently a dummy
    def testReasoning(self):
        assert 1 == 1

    #TODO test color coding
    #this will be implementation dependent, so I am leaving it a dummy for now
    def testColorCoding(self):
        assert 1 == 1

    def testHasSearchText(self):
        driver = self.driver
        search_bar = driver.find_element_by_name("searchbar")
        search_bar.clear()
        search_bar.send_keys("baseball")
        search_bar.send_keys(Keys.RETURN)

        assert "baseball" in driver.page_source

    def testNoResults(self):
        driver = self.driver
        search_bar = driver.find_element_by_name("searchbar")
        search_bar.clear()
        search_bar.send_keys("dsfasdjhcfjascnfcahuisheburibwaiucrasdjkchjkxznc")
        search_bar.send_keys(Keys.RETURN)

        assert "no" & "results" in driver.page_source
 
    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
    