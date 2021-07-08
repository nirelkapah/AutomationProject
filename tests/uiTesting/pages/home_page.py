from selenium.webdriver.remote.webdriver import WebDriver
from tests.uiTesting.infra.selenium_wrapper import SeleniumWrapper
import tests.uiTesting.env.config as config


class HomePage:

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.selenium_wrapper = SeleniumWrapper
        self.__base_url = config.data.get("base_url")

    def navigate_to_home_page(self):
        self.driver.get(self.__base_url)

    def open_new_project_form(self):

        sign_in_button = self.selenium_wrapper(self.driver).get_element_by_xpath_until_presence(xpath='//*[@id="content"]/section[1]/div[2]/div[2]/a[1]')
        sign_in_button.click()

    def select_project(self, project_name):
        self.driver.find_element_by_id("projects-menu").click()
        self.selenium_wrapper(self.driver).get_element_by_id_until_clickable("project_autocompletion_input").send_keys(project_name)
        self.selenium_wrapper(self.driver).get_element_by_xpath_until_presence(f"//div/a/mark[contains(text(), {project_name})]").click()

