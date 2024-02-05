from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from Hillel_october_23.lesson_24.widgets.components import Button

class PageButtons:
    _instance = None
    URL = "https://demoqa.com/buttons"

    # Singleton pattern
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance


    def __init__(self, driver:WebDriver):
        self.driver = driver
        self.button_doubleclick_loc = (By.ID, "doubleClickBtn")
        self.button_right_click_loc = (By.ID, "rightClickBtn")
        self.button_dynamic_id_loc = (By.XPATH, '//button[.="Click Me"]')
        self.button_doubleclick_message_loc = (By.ID, "doubleClickMessage")
        self.button_right_click_message_loc = (By.ID, "rightClickMessage")
        self.button_dynamic_id_click_message_loc = (By.ID, "dynamicClickMessage")


    def open(self):
        self.driver.get(self.URL)
        return self

    def button_doubleclick(self):
        return Button(self.driver, self.button_doubleclick_loc)

    def get_button_doubleclick_message(self) -> str:
        return self.driver.find_element(*self.button_doubleclick_message_loc).text

    def get_button_right_click_message(self) -> str:
        return self.driver.find_element(*self.button_right_click_message_loc).text

    def get_button_dynamic_id_click_message(self) -> str:
        return self.driver.find_element(*self.button_dynamic_id_click_message_loc).text