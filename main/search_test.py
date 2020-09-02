import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

class SearchTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '../resources/chromedriver')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_tee(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('Tee')
        search_field.submit()
        products = driver.find_elements_by_css_selector('ul>li>div>h2>a')
        self.assertEqual(5, len(products))

    def test_search_book(self):
        driver = self.driver
        search_field = driver.find_element_by_name('q')
        search_field.clear()
        search_field.send_keys('Book')
        search_field.submit()
        books = driver.find_elements_by_css_selector('ul>li>div>h2>a')
        self.assertEqual(3, len(books))

    def tearDown(self):
        self.driver.quit()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException:
            return False
        return True

if __name__ == "__main__":
    unittest.main(verbosity = 2)