from utils import *
from variables import *
import time


def test_ylab_page():
    driver = get_driver()

    driver.get(base_url)

    click_on(driver, by_xpath, proj)
    click_on(driver, by_css, all_stacks)
    click_on(driver, by_xpath, java)
    time.sleep(2)
    click_on(driver, by_css, b2b)

    description_body = "Включает такие сервисы как: электронный документооборот (ЭДО), проверка контрагентов, " \
                       "взыскание дебиторской задолженности и прочие."

    time.sleep(2)
    description = get_description(driver)
    validate_text(description_body, description)

    driver.close()
    driver.quit()
