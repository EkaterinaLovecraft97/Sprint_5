from conftest import driver
import data_generator
from locators import StellarBurgersLocators
from urls import REGISTER_URL, LOGIN_URL


from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from names import get_full_name

class TestRegistrationStellarBurgers:
    def test_successful_registration(driver):
        driver.get(REGISTER_URL)

        # Генерация данных
        email = data_generator.generate_email()
        password = data_generator.generate_password()
        name = get_full_name()

        # Заполнение имени
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_NAME).send_keys(name)
        # Заполнение email
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_EMAIL).send_keys(email)
        # Заполнение пароля
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_PASSWORD).send_keys(password)
        # Нажатие кнопки "Зарегистрироваться"
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.REGISTER_BUTTON).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(LOGIN_URL))

        # Проверка успешной регистрации
        assert driver.current_url == LOGIN_URL

    def test_error_for_short_password(driver):
        driver.get(REGISTER_URL)

        # Генерация данных
        email = data_generator.generate_email()
        password = data_generator.generate_password_less_then5()  # Слишком короткий пароль
        name = get_full_name()

        # Заполнение имени
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_NAME).send_keys(name)
        # Заполнение email
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_EMAIL).send_keys(email)
        # Заполнение пароля
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_PASSWORD).send_keys(password)
        # Нажатие кнопки "Зарегистрироваться"
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.REGISTER_BUTTON).click()

        # Проверка ошибки о коротком пароле
        error_message_element = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, StellarBurgersLocators.ERROR_MESSAGE))
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
        # Заполнение email
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_EMAIL).send_keys(email)
        # Заполнение пароля
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_PASSWORD).send_keys(password)
        # Нажатие кнопки "Зарегистрироваться"
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.REGISTER_BUTTON).click()

        assert driver.current_url == initial_url, f"Ожидался URL {initial_url}, но был {driver.current_url}"


    def test_error_for_invalid_email_format(driver):
        driver.get(REGISTER_URL)

        # Генерация данных
        email = "invalid_email"  # Некорректный email
        password = data_generator.generate_password()
        name = get_full_name()

        # Заполнение имени
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_NAME).send_keys(name)
        # Заполнение email
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_EMAIL).send_keys(email)
        # Заполнение пароля
        driver.find_element(By.XPATH, StellarBurgersLocators.REGISTER_PASSWORD).send_keys(password)
        # Нажатие кнопки "Зарегистрироваться"
        driver.find_element(By.CSS_SELECTOR, StellarBurgersLocators.REGISTER_BUTTON).click()

        # Проверка ошибки о некорректном email
        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "input__error"))
        ).text

        assert error_message == "Такой пользователь уже существует", "Ошибка о некорректном email не отображается"