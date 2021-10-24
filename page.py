from selenium.webdriver import Keys

from testcase.locator import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver


class MainPage(BasePage):

    def is_title_matches(self):
        return "Hejto" in self.driver.title

    def click_login_button(self):
        element = self.driver.find_element(*MainPageLocators.LOGIN_BUTTON)
        element.click()

    def log_in(self, login=None, password=None):
        login_input = self.driver.find_element(*MainPageLocators.LOGIN_INPUT)
        login_input.send_keys(login)
        password_input = self.driver.find_element(*MainPageLocators.PASSWORD_INPUT)
        password_input.send_keys(password)
        log_in_button = self.driver.find_element(*MainPageLocators.LOG_IN_BUTTON)
        log_in_button.click()

    def is_login_fail(self):
        try:
            self.driver.implicitly_wait(3)
            self.driver.find_element(*MainPageLocators.LOGIN_STATUS)
            print("Login failed...")
            return True
        except:
            print("Login success!")
            return False

    def search_something(self, item=None):
        searchbar = self.driver.find_element(*MainPageLocators.SEARCHBAR)
        searchbar.send_keys(item, Keys.ENTER)
        self.driver.implicitly_wait(3)
        try:
            self.driver.find_element(By.XPATH, f'//h2[text()="{item}"]')
            print("Searching works fine.")
            return True
        except:
            print("404")
            return False

    def read_post(self, post_id=0):
        posts = self.driver.find_elements(*MainPageLocators.POST)
        try:
            self.driver.implicitly_wait(30)
            self.driver.find_element(By.LINK_TEXT, posts[post_id].text).click()
            print(f"Your post id = {post_id}")
            return True
        except Exception as err:
            print("Post not found")
            print(err)
            return False
