import pickle

def test_cookies_download(firefox2):
    driver = firefox2
    driver.get("https://rozetka.com.ua")

    # - початок- код логін з пошуком всіх полів вводом логіна та пароля, та натискання кнопок

    # user_button = driver.find_element(By.XPATH, '(//button[contains(@class, "header__button")])[2]')
    # user_button.click()

    # email_field = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
    # password_field = driver.find_element(By.CSS_SELECTOR, "input#auth_pass")
    # email_field.send_keys("почта")
    # password_field.send_keys("пароль")

    # remember_checkbox = driver.find_element(By.CSS_SELECTOR, "label[for='remember_me']")
    # remember_checkbox.click()

    # submit_button = driver.find_element(By.XPATH, "//button[contains(@class, 'auth-modal__submit')]")
    # submit_button.click()

    # - кінець- код логін з пошуком всіх полів вводом логіна та пароля, та натискання кнопок

    cookies = driver.get_cookies() # витягуємо кукі
    print(type(cookies))
    with open("cookies.pkl", "wb") as file:
        pickle.dump(cookies, file)

def test_cookies_use(firefox2):
    driver = firefox2
    driver.get("https://rozetka.com.ua")

    with open("cookies.pkl", "rb") as file:
        cookies = pickle.load(file)
        for cookie in cookies:
            driver.add_cookie(cookie)

    driver.refresh()
