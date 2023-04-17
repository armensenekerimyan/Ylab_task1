from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wdw
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver import Chrome


def get_driver():
    driver = Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    return driver


def click_on(driver, by, selector):
    element = wdw(driver, 10).until(ec.element_to_be_clickable((by, selector)))
    element.click()


def validate_text(expected_result, actual_result):
    assert actual_result == expected_result, f"Expected result: {expected_result}, Actual result: {actual_result}"


def get_description(driver):
    return wdw(driver, 10).until(ec.visibility_of_element_located((By.XPATH, "(//p)[2]"))).text
