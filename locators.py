from selenium.webdriver.common.by import By


class StellarBurgersLocators:
    # Главная страница
    LOGIN_BUTTON = "//button[text()='Войти в аккаунт']"  # Кнопка "Войти в аккаунт"
    PERSONAL_ACCOUNT_BUTTON = "//a[.='Личный Кабинет']"  # Кнопка "Личный Кабинет"
    SING_UP_BUTTON = "//a[.='Зарегистрироваться']"  # Кнопка "Зарегистрироваться"

    # Регистрация
    # Локатор для поля ввода имени
    REGISTER_NAME =  "//fieldset[1]//input[@name='name']"
    # Локатор для поля ввода email
    REGISTER_EMAIL = "//fieldset[2]//input[@name='name']"
    # Локатор для поля ввода пароля
    REGISTER_PASSWORD = "//fieldset[3]//input[@name='Пароль']"
    # Локатор для кнопки "Зарегистрироваться"
    REGISTER_BUTTON = 'button.button_button__33qZ0'
    #Ссылка "Войти"
    LINK_SIGNIN = ".Auth_link__1fOlj"
    #Ссылка "Восстановить пароль"
    LINK_FORGOT_PASSWORD = "//a[.='Восстановить пароль']"
    #Ссылка "Войти" на вкладке "Восстановить пароль"
    LINK_SIGNIN_ON_FORGOT_PASSWORD_PAGE = ".Auth_link__1fOlj"
    ERROR_MESSAGE = ".input__error"

    #Страница входа
    # Локатор для поля ввода email
    LOGIN_EMAIL = "[name='name']"
    # Локатор для поля ввода пароля
    LOGIN_PASSWORD = "[name='Пароль']"
    # Локатор для кнопки "Войти"
    BUTTON_LOGIN = "button.button_button__33qZ0"

    # Личный кабинет
    # Локатор для кнопки "Выйти"
    EXIT_BUTTON = "button.Account_button__14Yp3"
    CONSTRUCTOR_BUTTON = "//a[.='Конструктор']"
    LOGO = "//div[@class='AppHeader_header__logo__2D0X2']/a[@href='/']"

    # Конструктор
    CONSTRUCTOR_BUNS = "//div[.='Булки']"  # Раздел "Булки"
    CONSTRUCTOR_SAUCES = "//div[.='Соусы']"  # Раздел "Соусы"
    CONSTRUCTOR_FILLINGS = "//div[.='Начинки']"  # Раздел "Начинки"
