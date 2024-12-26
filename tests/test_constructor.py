from locators import StellarBurgersLocators
from conftest import driver
from urls import HOME_URL

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestConstructorStellarBurgers:
    def test_move_on_toppings_by_click(driver):
        driver.get(HOME_URL)

        driver.find_element(By.XPATH, StellarBurgersLocators.CONSTRUCTOR_FILLINGS).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(HOME_URL))

        assert 'tab_tab_type_current__2BEPc' in driver.find_element(By.XPATH, StellarBurgersLocators.CONSTRUCTOR_FILLINGS).get_attribute("class")


    def test_move_on_sauces_by_click(driver):
        driver.get(HOME_URL)

        driver.find_element(By.XPATH, StellarBurgersLocators.CONSTRUCTOR_SAUCES).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(HOME_URL))

        assert 'tab_tab_type_current__2BEPc' in driver.find_element(By.XPATH, StellarBurgersLocators.CONSTRUCTOR_SAUCES).get_attribute("class")


    def test_move_on_buns_by_click(driver):
        driver.get(HOME_URL)

        driver.find_element(By.XPATH, StellarBurgersLocators.CONSTRUCTOR_SAUCES).click()
        WebDriverWait(driver, 10).until(EC.url_to_be(HOME_URL))
        driver.find_element(By.XPATH, StellarBurgersLocators.CONSTRUCTOR_BUNS).click()

        assert 'tab_tab_type_current__2BEPc' in driver.find_element(By.XPATH, StellarBurgersLocators.CONSTRUCTOR_BUNS).get_attribute("class")