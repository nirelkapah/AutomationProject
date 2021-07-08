
from selenium.webdriver.remote.webdriver import WebDriver
from tests.uiTesting.infra.selenium_wrapper import SeleniumWrapper
import tests.uiTesting.env.config as config


class LoginPage:

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.selenium_wrapper = SeleniumWrapper

        self.__username = config.data.get("username")
        self.__password = config.data.get("password")
        self.__base_url = config.data.get("base_url")

    def log_in(self):

        # Click sign in
        sign_in_button = self.selenium_wrapper(self.driver).get_element_by_css_selector_until_presence(css_selector="a[title='Sign in']")
        sign_in_button.click()

        # Insert values
        self.selenium_wrapper(self.driver).send_keys_to_element_by_id(object_identifier="username-pulldown", string_keys=self.__username)
        self.selenium_wrapper(self.driver).send_keys_to_element_by_id(object_identifier="password-pulldown", string_keys=self.__password)

        # Click on buttons
        login_button = self.selenium_wrapper(self.driver).get_element_by_id(id="login-pulldown")
        login_button.click()




