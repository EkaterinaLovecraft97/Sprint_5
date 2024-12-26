import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    # Настраиваем WebDriver
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()