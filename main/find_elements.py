import unittest
from pyunitreport import HTMLTestRunner
from selenium import webdriver

class HelloWorld(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = '../resources/chromedriver')
        driver = self.driver
        driver.get('http://demo-store.seleniumacademy.com/')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_search_text_field_by_id(self):
        search_field = self.driver.find_element_by_id('search')

    def test_search_test_field_by_name(self):
        search_field = self.driver.find_element_by_name('q')

    def test_search_test_field_by_class_name(self):
        search_field = self.driver.find_elements_by_class_name('input-text')

    def test_button_search_enabled(self):
        button_search = self.driver.find_elements_by_class_name('button')

    def count_banners(self):
        banner_list = self.driver.find_element_by_class_name('promos')
        banners = banner_list.find_element_by_tag_name('img')
        self.assertEqual(3, len(banners))

    def test_image_man_xpath(self):
        image_man = self.driver.find_element_by_xpath('//*[@id="top"]/body/div/div[2]/div[2]/div/div/div[2]/div[1]/ul/li[4]/a/img')

    def test_shopping_cart(self):
        shopping_cart = self.driver.find_element_by_css_selector('div.header-minicart span.icon')

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main(testRunner = HTMLTestRunner(output = 'find_elements', report_name = 'report_find_elements'))