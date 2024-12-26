from locators import StellarBurgersLocators
from conftest import driver
import data_generator
from urls import REGISTER_URL, LOGIN_URL, HOME_URL, PROFILE_URL

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from names import get_full_name

class TestProfileStellarBurgers:
    def test_open_account_on_click_account_button(driver):
        driver.get(HOME_URL)

        # Генерация данных
        email = data_generator.generate_email()
        password = data_generator.generate_password()
        name = get_full_name()

        driver.find_element(By.XPATH, StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
        driver.find_element(By.XPATH, StellarBurgersLocators.SING_UP_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(REGISTER_URL))
        # Заполнение имени
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_NAME).send_keys(name)
        # Заполнение email
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_EMAIL).send_keys(email)
        # Заполнение пароля
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_PASSWORD).send_keys(password)
        # Нажатие кнопки "Зарегистрироваться"
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))

        # Заполнение email
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.LOGIN_EMAIL).send_keys(email)
        # Заполнение пароля
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.LOGIN_PASSWORD).send_keys(password)
        # Нажатие кнопки "Войти"
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(HOME_URL))
        # Проверка перехода в Личный кабинет
        driver.find_element(By.XPATH, StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(PROFILE_URL))

        assert driver.current_url == PROFILE_URL


    def test_open_constructor_on_click_constructor_button(driver):
        driver.get(HOME_URL)

        # Генерация данных
        email = data_generator.generate_email()
        password = data_generator.generate_password()
        name = get_full_name()

        driver.find_element(By.XPATH, StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
        driver.find_element(By.XPATH, StellarBurgersLocators.SING_UP_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(REGISTER_URL))
        # Заполнение имени
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_NAME).send_keys(name)
        # Заполнение email
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_EMAIL).send_keys(email)
        # Заполнение пароля
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_PASSWORD).send_keys(password)
        # Нажатие кнопки "Зарегистрироваться"
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))

        # Заполнение email
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.LOGIN_EMAIL).send_keys(email)
        # Заполнение пароля
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.LOGIN_PASSWORD).send_keys(password)
        # Нажатие кнопки "Войти"
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(HOME_URL))

        # Переход в конструктор
        driver.find_element(By.XPATH, StellarBurgersLocators.CONSTRUCTOR_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(HOME_URL))

        assert driver.current_url == HOME_URL


    def test_open_constructor_on_click_logo_button(driver):
        driver.get(HOME_URL)

        # Генерация данных
        email = data_generator.generate_email()
        password = data_generator.generate_password()
        name = get_full_name()

        # Регистрация и вход
        driver.find_element(By.XPATH, StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
        driver.find_element(By.XPATH, StellarBurgersLocators.SING_UP_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(REGISTER_URL))
        # Заполнение имени
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_NAME).send_keys(name)
        # Заполнение email
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_EMAIL).send_keys(email)
        # Заполнение пароля
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_PASSWORD).send_keys(password)
        # Нажатие кнопки "Зарегистрироваться"
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))

        # Заполнение email
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.LOGIN_EMAIL).send_keys(email)
        # Заполнение пароля
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.LOGIN_PASSWORD).send_keys(password)
        # Нажатие кнопки "Войти"
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(HOME_URL))

        # Нажатие на логотип
        driver.find_element(By.XPATH, StellarBurgersLocators.LOGO).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(HOME_URL))

        assert driver.current_url == HOME_URL


    def test_exit_from_account_on_click_exit_button(driver):
        driver.get(HOME_URL)

        # Генерация данных
        email = data_generator.generate_email()
        password = data_generator.generate_password()
        name = get_full_name()

        # Регистрация и вход
        driver.find_element(By.XPATH, StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))
        driver.find_element(By.XPATH, StellarBurgersLocators.SING_UP_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(REGISTER_URL))
        # Заполнение имени
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_NAME).send_keys(name)
        # Заполнение email
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_EMAIL).send_keys(email)
        # Заполнение пароля
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_PASSWORD).send_keys(password)
        # Нажатие кнопки "Зарегистрироваться"
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))

        # Заполнение email
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.LOGIN_EMAIL).send_keys(email)
        # Заполнение пароля
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.LOGIN_PASSWORD).send_keys(password)
        # Нажатие кнопки "Войти"
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.BUTTON_LOGIN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(HOME_URL))

        # Нажатие кнопки "Личный кабинет"
        driver.find_element(By.XPATH, StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(PROFILE_URL))

        # Выход из аккаунта
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.EXIT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))

        assert driver.current_url == LOGIN_URL
