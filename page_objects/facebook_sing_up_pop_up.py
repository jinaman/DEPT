from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class FacebookSingUp:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.sing_up_button = (By.XPATH, '(//button[text()="Sign Up"])[1]')
        self.last_name_alert_symbol = (By.XPATH, '(//i[@class="_5dbc img sp_98fCI7IVTTz sx_54513f"])[2]')

    def click_sing_up_button(self):
        button = WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(self.sing_up_button))
        button.click()

    def first_name_alert_present(self):
        alert = WebDriverWait(self.driver, 5).until(EC.presence_of_element_located(self.last_name_alert_symbol))
        if alert:
            return True

