from selenium.webdriver.common.by import By

base_url = "https://ylab.io/"
proj = '(//a[contains(text(),\'Проекты\')])[1]'
all_stacks = '[title="Все стеки"]'
java = '//div[contains(text(),\'Java\')]'
b2b = 'div.ProjectCard.yellow'

by_xpath = By.XPATH
by_css = By.CSS_SELECTOR
