from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class GoogleMainPage:

    def __init__(self, my_driver):
        self.driver = my_driver
        self.google_search_box = (By.NAME, 'q')

    def search_google(self, search):
        box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.google_search_box))
        box.send_keys(search)
        box.send_keys(Keys.ENTER)

