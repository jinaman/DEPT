from selenium import webdriver


class WebDriverFactory:

    def __init__(self, browser):
        self.browser = browser

    def getWebDriverInstance(self):

        if self.browser == "firefox":
            driver = webdriver.Firefox(executable_path='../drivers/geckodriver.exe',  service_log_path=None)
        elif self.browser == "chrome":
            driver = webdriver.Chrome(executable_path=r'../drivers/chromedriver.exe')
        else:
            driver = webdriver.Firefox()
        driver.implicitly_wait(10)
        driver.maximize_window()
        return driver