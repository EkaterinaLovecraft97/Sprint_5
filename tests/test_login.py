from locators import StellarBurgersLocators
from conftest import driver
import data_generator


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from names import get_full_name

LOGIN_URL = "https://stellarburgers.nomoreparties.site/login"
HOME_URL = "https://stellarburgers.nomoreparties.site"
PROFILE_URL = "https://stellarburgers.nomoreparties.site/account/profile"

def test_login_button_sign_in_to_account(driver):
    driver.get(HOME_URL)
    # Нажатие кнопки "Войти в аккаунт"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.LOGIN_BUTTON)
    ).click()

    assert driver.current_url == LOGIN_URL


def test_login_button_personal_cabinet(driver):
    driver.get(HOME_URL)
    # Нажатие кнопки "Личный Кабинет"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON)
    ).click()

    assert driver.current_url == LOGIN_URL


def test_login_button_on_registration_page(driver):
    driver.get(HOME_URL)
    # Нажатие кнопки "Личный Кабинет"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON)
    ).click()

    # Нажатие кнопки "зарегистрироваться"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.SING_UP_BUTTON)
    ).click()

    # Нажатие кнопки "Войти"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.LINK_SIGNIN)
    ).click()

    assert driver.current_url == LOGIN_URL


def test_login_button_on_forgot_password_page(driver):
    driver.get(HOME_URL)
    # Нажатие кнопки "Личный Кабинет"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON)
    ).click()

    # Нажатие кнопки "Восстановить пароль"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.LINK_FORGOT_PASSWORD)
    ).click()

    # Нажатие кнопки "Войти"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.LINK_SIGNIN_ON_FORGOT_PASSWORD_PAGE)
    ).click()

    assert driver.current_url == LOGIN_URL
