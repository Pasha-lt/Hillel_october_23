from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

class TextBoxPage:
    def __init__(self, driver: WebDriver):
        self.url = "https://demoqa.com/text-box"
        self.driver = driver
        self.full_name_field = (By.ID, "userName")
        # self.full_name_field = (By.XPATH, "//input[@id='userName']")  # дублювання доступу до поля юзер нейм, але через xPAXTH
        self.full_email_field = (By.ID, "userEmail")
        self.full_current_text_area_field = (By.CSS_SELECTOR, "textarea#currentAddress")
        self.full_permanent_text_area_field = (By.CSS_SELECTOR, "textarea#permanentAddress")  # для різноманіття, можна було по айті як попереднє
        self.submit_btn = (By.ID, "submit")

        self.result_fullname = (By.ID, "name")
        self.result_email = (By.ID, "email")
        self.result_curr_addr = (By.CSS_SELECTOR, "p#currentAddress")
        self.result_perm_addr = (By.CSS_SELECTOR, "p#permanentAddress")


    def open(self) -> "TextBoxPage":
        self.driver.get(self.url)
        return self

    def clear_full_name_field(self) -> None:
        self.driver.find_element(*self.full_name_field).clear()

    def fill_full_name_field(self, text: str) -> None:
        self.driver.find_element(*self.full_name_field).send_keys(text)

    def clear_email_field(self) ->None:
        self.driver.find_element(*self.full_email_field).clear()

    def fill_email_field(self, text: str) ->None:
        self.driver.find_element(*self.full_email_field).send_keys(text)

    def clear_current_address_field(self) ->None:
        self.driver.find_element(*self.full_current_text_area_field).clear()

    def fill_current_address_field(self, text: str) ->None:
        self.driver.find_element(*self.full_current_text_area_field).send_keys(text)

    def clear_permanent_address_field(self) ->None:
        self.driver.find_element(*self.full_permanent_text_area_field).clear()

    def fill_permanent_address_field(self, text: str) ->None:
        self.driver.find_element(*self.full_permanent_text_area_field).send_keys(text)

    def click_submit(self) -> None:
        self.driver.find_element(*self.submit_btn).click()

    def get_result_fullname(self):
       return self.driver.find_element(*self.result_fullname).text

    def get_result_email(self):
       return self.driver.find_element(*self.result_email).text

    def get_result_current_address(self):
       return self.driver.find_element(*self.result_curr_addr).text

    def get_result_permanent_address(self):
       return self.driver.find_element(*self.result_perm_addr).text

    def scroll_down(self) -> None:
        self.driver.execute_script("window.scrollBy(0, 500);")