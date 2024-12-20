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
