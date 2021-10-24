import unittest
from selenium import webdriver
from testcase import page


class LoginTest(unittest.TestCase):

    def setUp(self):
        print("setup")
        self.driver = webdriver.Chrome()
        self.driver.get("https://hejto.pl")
        self.driver.maximize_window()

    def test_login_failed(self):
        main_page = page.MainPage(self.driver)
        print("main page")
        assert main_page.is_title_matches()
        main_page.click_login_button()
        main_page.log_in("pan_tuman", "xxx")
        assert main_page.is_login_fail() == True

    def test_login_successful(self):
        main_page = page.MainPage(self.driver)
        print("main page")
        assert main_page.is_title_matches()
        main_page.click_login_button()
        main_page.log_in("pan_tuman", "jestembotem")
        assert main_page.is_login_fail() == False

    def tearDown(self):
        self.driver.close()
