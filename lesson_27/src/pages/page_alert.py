from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class PageAlerts:
    _instance = None
    URL = "https://demoqa.com/alerts"

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance
    
    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver

        self.base_alert_loc = (By.ID, "alertButton")
        self.timer_alert_loc = (By.ID, "timerAlertButton")
        self.confirm_alert_loc = (By.ID, "confirmButton")
        self.prompt_alert_loc = (By.ID, "promtButton")

        self.alert_confirm_result_loc = (By.ID, "confirmResult")
        self.alert_prompt_result_loc = (By.ID, "promptResult")


        #confirmResult
    
    def open(self) -> "PageAlerts":
        self.driver.get(self.URL)
        return self

    def open_base_alert(self) -> None:
       alert_button = self.driver.find_element(*self.base_alert_loc)
       alert_button.click()

    def open_timer_alert(self) -> None:
       timer_button = self.driver.find_element(*self.timer_alert_loc)
       timer_button.click()

    def open_confirm_alert(self) -> None:
       confirm_button = self.driver.find_element(*self.confirm_alert_loc)
       confirm_button.click()

    def open_prompt_alert(self) -> None:
       prompt_button = self.driver.find_element(*self.prompt_alert_loc)
       prompt_button.click()

    def get_confirm_result(self) -> str:
        result = self.driver.find_element(*self.alert_confirm_result_loc).text
        return result

    def get_prompt_result(self) -> str:
        result = self.driver.find_element(*self.alert_prompt_result_loc).text
        return result

    def set_state_from_dropdown(self):
        pass