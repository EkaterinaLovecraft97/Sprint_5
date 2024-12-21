from conftest import driver
import data_generator
from locators import StellarBurgersLocators


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from names import get_full_name

REGISTER_URL = "https://stellarburgers.nomoreparties.site/register"

def test_successful_registration(driver):
    driver.get(REGISTER_URL)

    # Генерация данных
    email = data_generator.generate_email()
    password = data_generator.generate_password()
    name = get_full_name()

    # Заполнение имени
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(StellarBurgersLocators.REGISTER_NAME)
    ).send_keys(name)

    # Заполнение email
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(StellarBurgersLocators.REGISTER_EMAIL)
    ).send_keys(email)

    # Заполнение пароля
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(StellarBurgersLocators.REGISTER_PASSWORD)
    ).send_keys(password)

    # Нажатие кнопки "Зарегистрироваться"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.REGISTER_BUTTON)
    ).click()

    # Проверка успешной регистрации
    # Например, можно ожидать переход на страницу с подтверждением
    WebDriverWait(driver, 10).until(
        EC.url_contains("/login")  # Укажите правильный URL, если есть другой
    )
def test_error_for_short_password(driver):
    driver.get(REGISTER_URL)

    # Генерация данных
    email = data_generator.generate_email()
    password = data_generator.generate_password_less_then5()  # Слишком короткий пароль
    name = get_full_name()

    # Заполнение имени
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(StellarBurgersLocators.REGISTER_NAME)
    ).send_keys(name)

    # Заполнение email
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(StellarBurgersLocators.REGISTER_EMAIL)
    ).send_keys(email)

    # Заполнение пароля
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(StellarBurgersLocators.REGISTER_PASSWORD)
    ).send_keys(password)

    # Нажатие кнопки "Зарегистрироваться"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.REGISTER_BUTTON)
    ).click()

    # Проверка ошибки о коротком пароле
    error_message_element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.input__error'))
    )

    # Получаем текст ошибки
    error_message = error_message_element.text

    # Проверяем текст ошибки
    assert error_message == "Некорректный пароль", f"Ожидался текст ошибки 'Некорректный пароль', но был '{error_message}'"


def test_error_for_empty_name_field(driver):
    driver.get(REGISTER_URL)
    initial_url = driver.current_url

    # Генерация данных
    email = data_generator.generate_email()
    password = data_generator.generate_password()

    # Пустое поле имени
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(StellarBurgersLocators.REGISTER_EMAIL)
    ).send_keys(email)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(StellarBurgersLocators.REGISTER_PASSWORD)
    ).send_keys(password)

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.REGISTER_BUTTON)
    ).click()

    assert driver.current_url == initial_url, f"Ожидался URL {initial_url}, но был {driver.current_url}"


def test_error_for_invalid_email_format(driver):
    driver.get(REGISTER_URL)

    # Генерация данных
    email = "invalid_email"  # Некорректный email
    password = data_generator.generate_password()
    name = get_full_name()

    # Заполнение данных
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

    # Проверка ошибки о некорректном email
    error_message = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "input__error"))
    ).text

    assert error_message == "Такой пользователь уже существует", "Ошибка о некорректном email не отображается"