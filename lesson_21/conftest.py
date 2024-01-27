import pytest
from selenium import webdriver

@pytest.fixture
def chrome():
    driver = webdriver.Chrome(executable_path="/Users/pavlokostyshen/Desktop/hillel/Hillel_october_23/lesson_21/chromedriver")
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def firefox(request):
    driver = webdriver.Firefox(executable_path="/Users/pavlokostyshen/Desktop/hillel/Hillel_october_23/lesson_21/geckodriver")
    request.cls.driver = driver
    driver.implicitly_wait(5)  # імплісіті вейт це вся реалізація
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def chrome_class(request):
    driver = webdriver.Chrome(executable_path="/Users/pavlokostyshen/Desktop/hillel/Hillel_october_23/lesson_21/chromedriver")
    request.cls.driver = driver
    yield driver
    driver.quit()