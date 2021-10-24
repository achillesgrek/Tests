import unittest
from selenium import webdriver
from testcase import page


class ReadingPostTest(unittest.TestCase):

    def setUp(self):
        print("setup")
        self.driver = webdriver.Chrome()
        self.driver.get("https://hejto.pl")
        self.driver.maximize_window()

    def test_reading_post_success(self):
        main_page = page.MainPage(self.driver)
        result = main_page.read_post(4)
        assert result == True

    def test_reading_post_fail(self):
        main_page = page.MainPage(self.driver)
        result = main_page.read_post(-77)
        assert result == False

    def tearDown(self):
        self.driver.close()
