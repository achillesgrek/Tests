import unittest
from selenium import webdriver
from testcase import page


class SearchbarTest(unittest.TestCase):

    def setUp(self):
        print("setup")
        self.driver = webdriver.Chrome()
        self.driver.get("https://hejto.pl")
        self.driver.maximize_window()

    def test_searchbar_successful(self):
        main_page = page.MainPage(self.driver)
        result = main_page.search_something("test")
        assert result == True

    def test_searchbar_fail(self):
        main_page = page.MainPage(self.driver)
        result = main_page.search_something("")
        assert result == False

    def tearDown(self):
        self.driver.close()
