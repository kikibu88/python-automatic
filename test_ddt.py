import unittest
from selenium import webdriver
from ddt import ddt, data, unpack

@ddt
class SearchDDT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.gmarket.com/")
        self.driver.maximize_window()

    @data(("phones", 2), ("music", 5))
    @unpack
    def test_search(self, search_value, expected_count):
        self.search_field = self.driver.find_element_by_id("keyword")
        self.search_field.clear()
        self.search_field.send_keys(search_value)
        self.search_field.submit()

        list_item = self.driver.find_elements_by_tag_name("li")
        self.assertEqual(expected_count, len(list_item))

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
