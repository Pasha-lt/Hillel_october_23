from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class PageDynamicProperties:
    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.url = "https://demoqa.com/dynamic-properties"
        self.invisible_visible_button = "visibleAfter"
        self.disable_enable_button = (By.ID,  "enableAfter")

    def open(self):
        self.driver.get(self.url)
        return self

    def button_invisible_visible(self):
        button = self.driver.find_element(By.ID ,self.invisible_visible_button)
        return button

    def button_disable_enable(self) -> WebElement:
        button = self.driver.find_element(*self.disable_enable_button)
        return button