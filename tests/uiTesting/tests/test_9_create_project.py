from selenium import webdriver
from tests.uiTesting.pages.login_page import LoginPage
from tests.uiTesting.pages.home_page import HomePage
from tests.uiTesting.pages.new_project_page import NewProjectFormPage
from tests.uiTesting.pages.project_page import ProjectPage
import tests.uiTesting.utils.utils as utils


def test_9_create_project():
    driver = webdriver.Chrome("../chrome_driver/chromedriver.exe")
    driver.maximize_window()

    HomePage(driver).navigate_to_home_page()
    LoginPage(driver).log_in()
    HomePage(driver).open_new_project_form()
    project_name = utils.generate_random_name()
    NewProjectFormPage(driver).fill_in_project_name(project_name)
    NewProjectFormPage(driver).click_advanced_settings()

    assert NewProjectFormPage(driver).check_advance_settings_exist(), "Advanced Options Did Not Show Up"

    NewProjectFormPage(driver).fill_in_description()
    NewProjectFormPage(driver).set_status()
    NewProjectFormPage(driver).click_save()

    ProjectPage(driver).navigate_to_work_packages_by_click()
    received_project_name = ProjectPage(driver).return_project_name()

    assert received_project_name == project_name, "Current Project Name Is Not Equal To Created"

    dashed_project_name = utils.generate_string_to_url(project_name)
    assert dashed_project_name in driver.current_url, "Project's Name Is Not Equal To Identifier In URL"

    driver.quit()





