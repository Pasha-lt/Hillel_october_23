# Selenium IDE!
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class Test12321():
    def setup_method(self, method):
        self.driver = webdriver.Chrome(executable_path="./chromedriver")
        self.vars = {}

    def teardown_method(self, method):
        self.driver.quit()

    def test_12321(self):
        self.driver.get("https://www.wikipedia.org/")
        time.sleep(5)
        self.driver.set_window_size(1512, 864)
        time.sleep(5)
        self.driver.find_element(By.ID, "searchInput").send_keys("123213")
        time.sleep(5)
        self.driver.find_element(By.ID, "searchInput").send_keys(Keys.ENTER)
        self.driver.close()

