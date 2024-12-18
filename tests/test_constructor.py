from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import StellarBurgersLocators


def test_constructor_sections(driver):
    driver.get("https://stellarburgers.nomoreparties.site/")

    # Проверяем раздел "Булки"
    buns_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.CONSTRUCTOR_BUNS)
    )
    ActionChains(driver).move_to_element(buns_tab).click().perform()
    assert "Булки" in driver.page_source

    # Проверяем раздел "Соусы"
    sauces_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.CONSTRUCTOR_SAUCES)
    )
    ActionChains(driver).move_to_element(sauces_tab).click().perform()
    assert "Соусы" in driver.page_source

    # Проверяем раздел "Начинки"
    fillings_tab = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(StellarBurgersLocators.CONSTRUCTOR_FILLINGS)
    )
    ActionChains(driver).move_to_element(fillings_tab).click().perform()
    assert "Начинки" in driver.page_source

