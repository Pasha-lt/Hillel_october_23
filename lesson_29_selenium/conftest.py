import pytest
import requests
from selenium import webdriver
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service

@pytest.fixture
def chrome():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")  # запуск від рута, треба при роботі СІСД
    options.add_argument("--disable-gpu")  # не використовує відеокарту
    options.add_argument("--headless")  # без графічної відмальовки браузера.
    driver = webdriver.Chrome(options=options, executable_path="/Users/pavlokostyshen/Desktop/hillel/Hillel_october_23/lesson_22/chromedriver")
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def firefox(request):
    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service)
    #якщо використовуємо драйвер менеджер то нам не потрібно викачувати мануально наш драйвер
    # driver = webdriver.Firefox(executable_path="/Users/pavlokostyshen/Desktop/hillel/Hillel_october_23/lesson_22/geckodriver")
    request.cls.driver = driver
    driver.implicitly_wait(5)  # імплісіті вейт це вся реалізація
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def chrome_class(request):
    driver = webdriver.Chrome(executable_path="/Users/pavlokostyshen/Desktop/hillel/Hillel_october_23/lesson_22/chromedriver")
    request.cls.driver = driver
    yield driver
    driver.quit()

#фікстура яка приймає декілька параметрів.
@pytest.fixture(scope="class", params=['fashion', 'food', 'history'])
def fixture_chuck_category(request):
    category = request.param
    URL = f"https://api.chucknorris.io/jokes/random?category={category}"
    print(URL)
    response = requests.request(method="GET", url=URL)
    request.cls.response = response
    yield response


@pytest.fixture
def firefox2(request):
    driver = webdriver.Firefox(executable_path="/Users/pavlokostyshen/Desktop/hillel/Hillel_october_23/lesson_22/geckodriver")
    yield driver
    driver.quit()