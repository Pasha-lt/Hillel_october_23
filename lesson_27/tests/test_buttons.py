import pytest
from selenium.webdriver.remote.webdriver import WebDriver

from Hillel_october_23.lesson_24.src.pages.page_buttons import PageButtons



@pytest.mark.usefixtures("chrome_class")
class TestButtons:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = PageButtons(driver=self.driver)

    def test_doubleclick_button(self):
        self.page.open()
        self.page.button_doubleclick().doubleclick()
        assert self.page.get_button_doubleclick_message() == 'You have done a double click'

    def test_right_click_button(self):
        pass

    def test_dynamic_id_click_button(self):  #кнопка Click Me
        pass