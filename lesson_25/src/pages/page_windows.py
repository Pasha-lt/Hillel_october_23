from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Hillel_october_23.lesson_25.widgets.components import Button


class WindowPage:
    URL = "https://demoqa.com/browser-windows"
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open(self) -> "WindowPage":
        self.driver.get(self.URL)
        return self

    def open_new_tab(self):
        button_open_tab = Button(self.driver, (By.ID, "tabButton"))
        button_open_tab.click()

    def open_new_window(self):
        button_open_tab = Button(self.driver, (By.ID, "windowButton"))
        button_open_tab.click()

    def open_window_message(self):
        button_open_tab = Button(self.driver, (By.ID, "messageWindowButton"))
        button_open_tab.click()