from selenium.webdriver.remote.webdriver import WebDriver
from tests.uiTesting.infra.selenium_wrapper import SeleniumWrapper
import tests.uiTesting.env.config as config


class ProjectPage:

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.selenium_wrapper = SeleniumWrapper
        self.__base_url = config.data.get("base_url")

    def navigate_to_work_packages_by_click(self):
        work_packages_button = self.selenium_wrapper(self.driver).get_element_by_id_until_clickable("main-menu-work-packages")
        work_packages_button.click()

    def return_project_name(self):
        project_menu = self.selenium_wrapper(self.driver).get_element_by_id_until_clickable("projects-menu")
        return project_menu.get_attribute("title")
