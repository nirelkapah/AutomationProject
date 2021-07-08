from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class SeleniumWrapper:

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def get_element_by_xpath(self, xpath):
        try:
            return self.driver.find_element_by_xpath(xpath)
        except NoSuchElementException as e:
            return None

    def get_element_by_id(self, id):
        try:
            return self.driver.find_element_by_id(id)
        except NoSuchElementException as e:
            return None

    def get_element_from_list_by_text(self, locator: By, locator_value, text_to_search: str) -> WebElement:
        element_list = self.driver.find_elements(locator, locator_value)
        for element in element_list:
            element_text = element.text
            print(element_text)
            if text_to_search in element_text:
                return element
        return None

    def get_element_from_list_by_text_by_class(self, class_text, text_to_search):
        return self.get_element_from_list_by_text(By.CLASS_NAME, class_text, text_to_search)

    def get_element_from_list_by_text_by_id(self, resource_id, text_to_search):
        return self.get_element_from_list_by_text(By.ID, resource_id, text_to_search)

    def validate_title_exists(self):
        return len(self.driver.title) > 0

    def validate_page_title(self, expected_title):
        actual_title = self.driver.title
        return actual_title == expected_title

    def get_element_parent(self, element: WebElement) -> WebElement:
        return element.find_element_by_xpath("../")

    def _mouse_hover_element(self, element: WebElement):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()

    def switch_to_last_opened_tab(self):
        window_handles = self.driver.window_handles
        self.driver.switch_to.window(window_handles[len(window_handles) - 1])

    def get_all_current_windows_title(self):
        window_handles = self.driver.window_handles
        titles = []
        initial_handle = self.driver.current_window_handle
        for window_handle in window_handles:
            self.driver.switch_to.window(window_handle)
            titles.append(self.driver.title)

        self.driver.switch_to.window(initial_handle)
        return titles

    # ME ############################################################

    def send_keys_to_element_by_id(self, object_identifier: str, string_keys: str):
        self.driver.find_element(By.ID, object_identifier).send_keys(string_keys)

    # Until Presence

    def get_element_by_css_selector_until_presence(self, css_selector: str):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, css_selector)))

    def get_element_by_id_until_presence(self, id: str):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, id)))

    def get_element_by_xpath_until_presence(self, xpath: str):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath)))

    def get_elements_by_xpath_until_presence(self, xpath: str):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, xpath)))


    # Until Clickable

    def get_element_by_css_selector_until_clickable(self, css_selector: str):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, css_selector)))

    def get_element_by_id_until_clickable(self, id: str):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.ID, id)))

    def get_element_by_xpath_until_clickable(self, xpath: str):
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath)))

    # Until Invisible
    def get_element_by_xpath_until_visible(self, xpath: str):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element((By.XPATH, xpath)))