from locators import StellarBurgersLocators
from conftest import driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_successful_registration(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")

    # Заполнение имени
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(StellarBurgersLocators.REGISTER_NAME)
    ).send_keys("Tests_User_Name")

    # Заполнение email
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(StellarBurgersLocators.REGISTER_EMAIL)
    ).send_keys("test_5_001@yandex.ru")

    # Заполнение пароля
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(StellarBurgersLocators.REGISTER_PASSWORD)
    ).send_keys("password123")

    # Нажатие кнопки "Зарегистрироваться"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.REGISTER_BUTTON)
    ).click()

    # Проверка успешной регистрации
    # Например, можно ожидать переход на страницу с подтверждением
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")  # Укажите правильный URL, если есть другой
    )
