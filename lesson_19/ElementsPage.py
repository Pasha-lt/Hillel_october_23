from selenium.webdriver.common.by import By


class ElementsPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://demoqa.com/elements"
        self.element_categories = By.XPATH, "//div[contains(@class, show)]//li"

    def open(self):
        self.driver.get(self.url)
        return self

    def get_elements_page_categories(self):
        categories = [cat.text for cat in self.driver.find_elements(*self.element_categories)]
        return categories



