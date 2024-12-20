from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class StellarBurgersLocators:
    # Главная страница
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка "Войти в аккаунт"
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")  # Кнопка "Личный Кабинет"
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Логотип

    # Регистрация
    # Локатор для поля ввода имени
    REGISTER_NAME = (By.CSS_SELECTOR, 'input[name="name"]')
    # Локатор для поля ввода email
    REGISTER_EMAIL = (By.CSS_SELECTOR, 'input[name="name"]')
    # Локатор для поля ввода пароля
    REGISTER_PASSWORD = (By.CSS_SELECTOR, 'input[type="password"]')
    # Локатор для кнопки "Зарегистрироваться"
    REGISTER_BUTTON = (By.CSS_SELECTOR, 'button.button_button__33qZ0')

    # Конструктор
    CONSTRUCTOR_BUNS = (By.XPATH, "//span[text()='Булки']")  # Раздел "Булки"
    CONSTRUCTOR_SAUCES = (By.XPATH, "//span[text()='Соусы']")  # Раздел "Соусы"
    CONSTRUCTOR_FILLINGS = (By.XPATH, "//span[text()='Начинки']")  # Раздел "Начинки"
