
import pytest
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from Hillel_october_23.lesson_26.src.pages.page_alert import PageAlerts

@pytest.mark.usefixtures("firefox")
class TestAlerts:

    def setup_method(self):
        self.driver: WebDriver = self.driver
        self.page = PageAlerts(driver=self.driver)
        self.page.open()

    def test_base_alerts(self):
        self.page.open_base_alert()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()  # натискаємо на кнопку ОК на нашому Alert
        assert "clicked" in alert_text

    def test_timer_alert(self):
        self.page.open_timer_alert()
        WebDriverWait(self.driver, 7).until(ec.alert_is_present())
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        assert "appeared" in alert_text

    def test_accept_confirm_alert(self):
        self.page.open_confirm_alert()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.accept()
        assert "confirm" in alert_text
        assert "You selected Ok" in self.page.get_confirm_result()

    def test_decline_confirm_alert(self):
        self.page.open_confirm_alert()
        alert = self.driver.switch_to.alert
        alert_text = alert.text
        alert.dismiss()
        assert "confirm" in alert_text
        assert "You selected Cancel" in self.page.get_confirm_result()