import time
from selenium import webdriver
from tests.uiTesting.pages.login_page import LoginPage
from tests.uiTesting.pages.home_page import HomePage
from tests.uiTesting.pages.project_page import ProjectPage
from tests.uiTesting.pages.work_package_page import WorkPackagePage
import tests.uiTesting.utils.utils as utils


def test_10_create_task():
    driver = webdriver.Chrome("../chrome_driver/chromedriver.exe")
    driver.maximize_window()

    HomePage(driver).navigate_to_home_page()
    LoginPage(driver).log_in()
    HomePage(driver).select_project("TestProject1")
    ProjectPage(driver).navigate_to_work_packages_by_click()

    work_packages_count = WorkPackagePage(driver).get_work_packages_range()

    WorkPackagePage(driver).click_create_task()

    assert WorkPackagePage(driver).check_new_work_package_title_exist('New', 'Task'), "New Task Title Was Not Shown"

    subject_string = utils.generate_random_text()
    description_string = utils.generate_random_text()
    WorkPackagePage(driver).fill_in_task(subject_string, description_string)
    WorkPackagePage(driver).save_task()

    WorkPackagePage(driver).wait_until_successful_creation_is_visible(subject_string)

    # wait for complete task upload
    time.sleep(3)

    new_work_packages_count = WorkPackagePage(driver).get_work_packages_range()

    assert new_work_packages_count == work_packages_count+1, "New Task was NOT Added To List As Expected"

    WorkPackagePage(driver).navigate_to_last_work_package()

    assert WorkPackagePage(driver).verify_subject_and_type_of_created_task(subject_string, "Type"), "Last Task Data In Table Does Not Match New Created Task"

    driver.quit()





