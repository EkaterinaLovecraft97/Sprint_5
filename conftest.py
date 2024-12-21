import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Настраиваем WebDriver
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)  # Явное ожидание
    yield driver
    driver.quit()

@pytest.fixture
def open_registration_page(driver):
    driver.get("https://stellarburgers.nomoreparties.site/register")
    yield driver