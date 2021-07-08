
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from tests.uiTesting.infra.selenium_wrapper import SeleniumWrapper
import tests.uiTesting.env.config as config


class NewProjectFormPage:

    def __init__(self, driver):
        self.driver: WebDriver = driver
        self.selenium_wrapper = SeleniumWrapper
        self.__base_url = config.data.get("base_url")

    def fill_in_project_name(self, project_name):
        name_input = self.selenium_wrapper(self.driver).get_element_by_id_until_presence(id="formly_3_textInput_name_0")
        name_input.send_keys(project_name)

    def click_advanced_settings(self):
        advanced_settings_button = self.selenium_wrapper(self.driver).get_element_by_css_selector_until_presence(css_selector="button[title='Show/hide']")
        advanced_settings_button.click()

    def check_advance_settings_exist(self):
        try:
            self.selenium_wrapper(self.driver).get_element_by_xpath_until_presence("//div[contains(text(), ' description ')]")
            self.selenium_wrapper(self.driver).get_element_by_xpath_until_presence("//div[contains(text(), ' Public ')]")
            self.selenium_wrapper(self.driver).get_element_by_xpath_until_presence("//div[contains(text(), ' Status ')]")
            self.selenium_wrapper(self.driver).get_element_by_xpath_until_presence("//div[contains(text(), ' Status description ')]")

        except NoSuchElementException:
            return False
        return True

    def fill_in_description(self):
        description = "this is description"

        description_box = self.driver.find_element_by_xpath('//*[@id="formly_9_formattableInput_description_1"]/div/op-ckeditor/div/div[2]/div')
        description_box.send_keys(description)

    def set_status(self):


        status_input = self.driver.find_element_by_xpath('//*[@id="formly_9_selectProjectStatusInput__links.status_4"]/div/div/div[3]/input')
        status_input.click()

        status_on_track = self.driver.find_element_by_xpath("//span[contains(text(), 'On track')]")
        status_on_track.click()

    def click_save(self):
        save_button = self.driver.find_element_by_xpath("//button[contains(text(), 'Save')]")
        save_button.click()
