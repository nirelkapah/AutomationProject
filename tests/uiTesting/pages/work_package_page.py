from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.remote.webdriver import WebDriver
from tests.uiTesting.infra.selenium_wrapper import SeleniumWrapper
import tests.uiTesting.env.config as config


class WorkPackagePage:

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

    def count_work_packages_rows(self):
        table_rows = self.selenium_wrapper(self.driver).get_elements_by_xpath_until_presence("//div[@wp-isolated-query-space]//tbody//tr[@data-class-identifier]")
        return len(table_rows)

    def click_create_task(self):
        self.driver.find_element_by_xpath("//button[.='Create']").click()
        self.selenium_wrapper(self.driver).get_element_by_xpath_until_presence("//*[@id='types-context-menu']/ul/li/a/span[.='Task']").click()

    def check_new_work_package_title_exist(self, work_package_status, work_package_type ) -> bool:
        try:
            self.selenium_wrapper(self.driver).get_element_by_xpath_until_visible(f"//ng-select//span[.={work_package_status}]")
            self.selenium_wrapper(self.driver).get_element_by_xpath_until_visible(f"//ng-select//span[.={work_package_type}]")
        except NoSuchElementException:
            return False
        return True

    def fill_in_task(self, subject: str, description: str):
        subject_input = self.selenium_wrapper(self.driver).get_element_by_id_until_clickable("wp-new-inline-edit--field-subject")
        subject_input.send_keys(subject)

        description_input = self.selenium_wrapper(self.driver).get_element_by_xpath_until_clickable("//op-ckeditor//div[@role='textbox']")
        description_input.send_keys(description)

    def save_task(self):
        save_button = self.selenium_wrapper(self.driver).get_element_by_id_until_clickable("work-packages--edit-actions-save")
        save_button.click()

    def wait_until_successful_creation_is_visible(self, subject_string: str):
        self.selenium_wrapper(self.driver).get_element_by_xpath_until_visible(f"//table/tbody/tr/td/span/span[.={subject_string}]")

    def get_work_packages_range(self):
        span_element = self.selenium_wrapper(self.driver).get_element_by_xpath_until_clickable("//li[@class='pagination--range']/span")
        paging_string = span_element.get_attribute("innerHTML")
        work_packages = paging_string.rsplit('/', 1)[-1]
        return int(work_packages.replace(')', ''))

    def navigate_to_last_work_package(self):
        id_button = self.selenium_wrapper(self.driver).get_element_by_id_until_clickable("id")
        id_button.click()
        descending_filter_button = self.selenium_wrapper(self.driver).get_element_by_xpath_until_clickable("//div[@id='column-context-menu']/ul/li/a[.='Sort descending']")
        descending_filter_button.click()

    def verify_subject_and_type_of_created_task(self, original_subject_string: str, original_type_string: str):
        try:
            self.selenium_wrapper(self.driver).get_element_by_xpath_until_visible(f"//tbody[1]/tr[1]/td[3]/span/span[.={original_subject_string}]")
            self.selenium_wrapper(self.driver).get_element_by_xpath_until_visible(f"//tbody[1]/tr[1]/td[4]/span/span[.={original_type_string}]")
        except NoSuchElementException:
            return False
        return True
