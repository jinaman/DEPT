from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class FacebookMainPage:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.create_new_account_button = (By.XPATH, '//a[@data-testid="open-registration-form-button"]')


    def click_create_new_account_button(self):
        button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.create_new_account_button))
        button.click()
