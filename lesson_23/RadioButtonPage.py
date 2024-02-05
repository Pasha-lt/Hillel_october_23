from selenium.webdriver.remote.webdriver import WebDriver


class RadioButton:

    def __init__(self, driver: WebDriver = None, locator: tuple = None, name: str = None):
        self.driver = driver
        self.locator = locator
        self.by, self.loc = self.locator
        if name:
            self.name: str = name
            self.loc = self.loc.format(self.name)

    def select(self, name=None):
        if self.name:
            self.driver.find_element(self.by, self.loc).click()
        else:
            self.driver.find_element(*self.locator).click()