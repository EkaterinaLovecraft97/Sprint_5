from locators import StellarBurgersLocators
from conftest import driver
import data_generator


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from names import get_full_name

LOGIN_URL = "https://stellarburgers.nomoreparties.site/login"
HOME_URL = "https://stellarburgers.nomoreparties.site/"
PROFILE_URL = "https://stellarburgers.nomoreparties.site/account/profile"

def register_user(driver, name, email, password):
    """Регистрация нового пользователя."""
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.SING_UP_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(StellarBurgersLocators.REGISTER_NAME)
    ).send_keys(name)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(StellarBurgersLocators.REGISTER_EMAIL)
    ).send_keys(email)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(StellarBurgersLocators.REGISTER_PASSWORD)
    ).send_keys(password)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.REGISTER_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))


def login_user(driver, email, password):
    """Авторизация пользователя."""
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(StellarBurgersLocators.LOGIN_EMAIL)
    ).send_keys(email)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(StellarBurgersLocators.LOGIN_PASSWORD)
    ).send_keys(password)

    driver.find_element(By.CSS_SELECTOR, ".button_button__33qZ0").click()


def test_open_account_on_click_account_button(driver):
    driver.get(HOME_URL)

    # Генерация данных
    email = data_generator.generate_email()
    password = data_generator.generate_password()
    name = get_full_name()

    # Регистрация пользователя
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON)
    ).click()
    register_user(driver, name, email, password)

    # Логин пользователя
    login_user(driver, email, password)

    # Проверка перехода в Личный кабинет
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON)
    ).click()
    WebDriverWait(driver, 10).until(EC.url_to_be(PROFILE_URL))

    assert driver.current_url == PROFILE_URL


def test_open_constructor_on_click_constructor_button(driver):
    driver.get(HOME_URL)

    # Генерация данных
    email = data_generator.generate_email()
    password = data_generator.generate_password()
    name = get_full_name()

    # Регистрация и вход
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON)
    ).click()
    register_user(driver, name, email, password)
    login_user(driver, email, password)

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
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON)
    ).click()
    register_user(driver, name, email, password)
    login_user(driver, email, password)

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
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON)
    ).click()
    register_user(driver, name, email, password)
    login_user(driver, email, password)

    # Нажатие кнопки "Личный кабинет"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON)
    ).click()

    WebDriverWait(driver, 10).until(EC.url_to_be(PROFILE_URL))

    # Выход из аккаунта
    driver.find_element(By.CSS_SELECTOR, ".Account_button__14Yp3").click()
    WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))

    assert driver.current_url == LOGIN_URL
