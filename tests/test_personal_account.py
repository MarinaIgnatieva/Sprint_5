
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import  BUTTON_PERSONAL_ACCOUNT, LOGIN_FORM, \
    LINK_PROFILE, BUTTON_LOGOUT
from urls import PROFILE_URL, LOGIN_URL


class TestPersonalAccount():

    #тест перехода по клику на кнопку Личный кабинет
    def test_click_on_button_personal_account(self, user_login, driver):
        driver.find_element(By.XPATH, BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, LINK_PROFILE)))

        assert driver.current_url == PROFILE_URL



    #тест выхода по кнопке «Выйти» в личном кабинете
    def test_logout(self, driver, user_login):
        driver.find_element(By.XPATH, BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, LINK_PROFILE)))

        driver.find_element(By.XPATH, BUTTON_LOGOUT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_FORM)))

        assert driver.current_url == LOGIN_URL



