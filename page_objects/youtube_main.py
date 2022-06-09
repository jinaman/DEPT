from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class YoutubeMainPage:
    def __init__(self, my_driver):
        self.driver = my_driver
        self.search_box = (By.XPATH, '//input[@id="search"]')
        self.musica_ligera_link = (By.XPATH, '(//yt-formatted-string[text()="Soda Stereo - De Musica Ligera (El Último Concierto)"])[1]')
        self.search_button = (By.ID, 'search-icon-legacy')

    def search_video(self, search):
        box = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.search_box))
        box.send_keys(search)
        self.driver.find_element(*self.search_button).click()

    def click_musica_ligera_link(self):
        self.driver.find_element(*self.musica_ligera_link).click()



