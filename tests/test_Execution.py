import pytest
import unittest
from selenium.webdriver.common.by import By
from page_objects.youtube_main import YoutubeMainPage
from page_objects.google_main import GoogleMainPage
from page_objects.facebook_main import FacebookMainPage
from page_objects.facebook_sing_up_pop_up import FacebookSingUp


@pytest.mark.usefixtures("oneTimeSetUp")
class TestingDEPT(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.youtubemainpage = YoutubeMainPage(self.driver)
        self.googlemainpage = GoogleMainPage(self.driver)
        self.facebookmainpage = FacebookMainPage(self.driver)
        self.facebooksingup = FacebookSingUp(self.driver)

    @pytest.mark.run(order=1)
    def test_youtube(self):
        youtube_url = 'https://www.youtube.com/'
        google_url = 'https://www.google.com/'
        self.driver.get(youtube_url)
        self.youtubemainpage.search_video('musica ligera ultimo concierto')
        self.youtubemainpage.click_musica_ligera_link()
        musica_ligera_url = self.driver.current_url
        self.driver.execute_script("window.open('');")
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.driver.get(google_url)
        self.googlemainpage.search_google('musica ligera ultimo concierto')
        self.assertTrue(self.driver.find_element(By.XPATH, '//a[@href="{}"]'.format(musica_ligera_url)))

    def test_facebook_validation(self):
        facebook_url = 'https://www.facebook.com'
        self.driver.get(facebook_url)
        self.facebookmainpage.click_create_new_account_button()
        self.facebooksingup.click_sing_up_button()
        last_name_alert_present = self.facebooksingup.first_name_alert_present()
        self.assertTrue(last_name_alert_present)



