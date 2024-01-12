import pytest
from selenium import webdriver

@pytest.fixture
def chrome():
    driver = webdriver.Chrome(executable_path="/Users/pavlokostyshen/Desktop/hillel/Hillel_october_23/lesson_19/chromedriver")
    yield driver
    driver.quit()
