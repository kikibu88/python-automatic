import unittest
from selenium import webdriver

class SearchProducts(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.gmarket.com/")
        self.driver.maximize_window()

    def testSearchByCategory(self):
        self.search_field = self.driver.find_element_by_id("keyword")
        self.search_field.clear()
        self.search_field.send_keys('phones')
        self.search_field.submit()
        list_item = self.driver.find_elements_by_tag_name("li")
        self.assertEqual(260, len(list_item))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
