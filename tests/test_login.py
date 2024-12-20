from locators import StellarBurgersLocators
from conftest import driver


def test_login_via_account_button(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Нажимаем кнопку "Войти в аккаунт"
    driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON).click()

    # Вводим данные для входа
    driver.find_element(*StellarBurgersLocators.REGISTER_EMAIL).send_keys("test_5_001@yandex.ru")
    driver.find_element(*StellarBurgersLocators.REGISTER_PASSWORD).send_keys("password123")
    driver.find_element(*StellarBurgersLocators.REGISTER_BUTTON).click()

    # Проверяем, что открылась страница личного кабинета
    assert "Личный Кабинет" in driver.page_source
