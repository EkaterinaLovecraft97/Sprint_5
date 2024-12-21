from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class StellarBurgersLocators:
    # Главная страница
    LOGIN_BUTTON = By.XPATH, "//button[text()='Войти в аккаунт']"  # Кнопка "Войти в аккаунт"
    PERSONAL_ACCOUNT_BUTTON = By.XPATH, "//a[.='Личный Кабинет']"  # Кнопка "Личный Кабинет"
    SING_UP_BUTTON = By.XPATH, "//a[.='Зарегистрироваться']"  # Кнопка "Зарегистрироваться"

    # Регистрация
    # Локатор для поля ввода имени
    REGISTER_NAME = By.XPATH, "//fieldset[1]//input[@name='name']"
    # Локатор для поля ввода email
    REGISTER_EMAIL = By.XPATH, "//fieldset[2]//input[@name='name']"
    # Локатор для поля ввода пароля
    REGISTER_PASSWORD = By.XPATH, "//fieldset[3]//input[@name='Пароль']"
    # Локатор для кнопки "Зарегистрироваться"
    REGISTER_BUTTON = By.CSS_SELECTOR, 'button.button_button__33qZ0'
    #Ссылка "Войти"
    LINK_SIGNIN = By.CSS_SELECTOR, ".Auth_link__1fOlj"
    #Ссылка "Восстановить пароль"
    LINK_FORGOT_PASSWORD = By.XPATH, "//a[.='Восстановить пароль']"
    #Ссылка "Войти" на вкладке "Восстановить пароль"
    LINK_SIGNIN_ON_FORGOT_PASSWORD_PAGE = By.CSS_SELECTOR, ".Auth_link__1fOlj"

    #Страница входа
    # Локатор для поля ввода email
    LOGIN_EMAIL = By.CSS_SELECTOR, "[name='name']"
    # Локатор для поля ввода пароля
    LOGIN_PASSWORD = By.CSS_SELECTOR, "[name='Пароль']"
    # Локатор для кнопки "Войти"
    BUTTON_LOGIN = By.CSS_SELECTOR, ".button_button__33qZ0"

    # Личный кабинет
    # Локатор для кнопки "Выйти"
    EXIT_BUTTON = By.CSS_SELECTOR, "Account_button__14Yp3"
    CONSTRUCTOR_BUTTON = "//a[.='Конструктор']"
    LOGO = "//div[@class='AppHeader_header__logo__2D0X2']/a[@href='/']"

    # Конструктор
    CONSTRUCTOR_BUNS = "//div[.='Булки']"  # Раздел "Булки"
    CONSTRUCTOR_SAUCES = "//div[.='Соусы']"  # Раздел "Соусы"
    CONSTRUCTOR_FILLINGS = "//div[.='Начинки']"  # Раздел "Начинки"
