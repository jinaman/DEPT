from selenium import webdriver

class WebDriverFactory():

    def __init__(self, browser):

        self.browser = browser
    def getWebDriverInstance(self):


        if self.browser == "iexplorer":
            driver = webdriver.Ie()
        elif self.browser == "firefox":
            driver = webdriver.Firefox()
        elif self.browser == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver