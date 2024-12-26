from locators import StellarBurgersLocators
from conftest import driver
from urls import HOME_URL, LOGIN_URL

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestLoginStellarBurgers:
    def test_login_button_sign_in_to_account(driver):
        driver.get(HOME_URL)
        # Нажатие кнопки "Войти в аккаунт"
        driver.find_element(By.XPATH, StellarBurgersLocators.LOGIN_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))

        assert driver.current_url == LOGIN_URL

    def test_login_button_personal_cabinet(driver):
        driver.get(HOME_URL)
        # Нажатие кнопки "Личный Кабинет"
        driver.find_element(By.XPATH, StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))

        assert driver.current_url == LOGIN_URL


    def test_login_button_on_registration_page(driver):
        driver.get(HOME_URL)
        # Нажатие кнопки "Личный Кабинет"
        driver.find_element(By.XPATH, StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        # Нажатие кнопки "зарегистрироваться"
        driver.find_element(By.XPATH, StellarBurgersLocators.SING_UP_BUTTON).click()
        # Нажатие кнопки "Войти"
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.LINK_SIGNIN).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))

        assert driver.current_url == LOGIN_URL


    def test_login_button_on_forgot_password_page(driver):
        driver.get(HOME_URL)
        # Нажатие кнопки "Личный Кабинет"
        driver.find_element(By.XPATH, StellarBurgersLocators.PERSONAL_ACCOUNT_BUTTON).click()
        # Нажатие кнопки "Восстановить пароль"
        driver.find_element(By.XPATH, StellarBurgersLocators.LINK_FORGOT_PASSWORD).click()
        # Нажатие кнопки "Войти"
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.LINK_SIGNIN_ON_FORGOT_PASSWORD_PAGE).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))

        assert driver.current_url == LOGIN_URL
