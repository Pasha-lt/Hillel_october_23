from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class PagePracticeForm:
    _instance = None
    URL = "https://demoqa.com/automation-practice-form"

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, driver: WebDriver):
        self.driver: WebDriver = driver
        self.state_dropdown_loc = (By.ID, "state")
        self.locator = (By.XPATH, "//div[contains(@id, 'option')]")


    def open(self) -> "PagePracticeForm":
        self.driver.get(self.URL)
        return self


    def show_filtered_results_in_dropdown(self, state: str):
        element = self.driver.find_element(*self.state_dropdown_loc)
        element.location_once_scrolled_into_view
        WebDriverWait(driver=self.driver, timeout=10).until(ec.visibility_of_element_located(self.state_dropdown_loc))
        element.click()
        state_input = self.driver.find_element(By.XPATH, "//div[@id='state']//input")
        state_input.send_keys(state)
        return state_input

    def set_state_via_input(self, state):
        state_input = self.show_filtered_results_in_dropdown(state)
        state_input.send_keys(Keys.ENTER)

    def get_result_from_dropdown(self) -> list:
        elements = self.driver.find_elements(*self.locator)
        result = [element.text for element in elements]
        return result