import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import  NAME_REGISTRATION, EMAIL_REGISTRATION, PASSWORD_REGISTRATION, \
    BUTTON_REGISTRATION, LOGIN_FORM
from urls import Registration_URL


class TestRegistration:

    #Тест успешной регистрации
    def test_registration_success(self, driver):

        driver.get(Registration_URL)

        driver.find_element(By.XPATH, NAME_REGISTRATION).send_keys('Marina')

        email = f'MarinaIgnatieva23{random.randint(100,999)}@ya.ru'
        driver.find_element(By.XPATH, EMAIL_REGISTRATION).send_keys(email)

        driver.find_element(By.XPATH, PASSWORD_REGISTRATION).send_keys('123456')

        driver.find_element(By.XPATH, BUTTON_REGISTRATION).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_FORM)))

        assert driver.current_url == 'https://stellarburgers.nomoreparties.site/login'



    #Тест ошибки для короткого пароля
    def test_short_password(self, driver):

        driver.get('https://stellarburgers.nomoreparties.site/register')

        driver.find_element(By.XPATH, NAME_REGISTRATION).send_keys('Marina')

        email = f'MarinaIgnatieva23{random.randint(100, 999)}@ya.ru'
        driver.find_element(By.XPATH, EMAIL_REGISTRATION).send_keys(email)

        driver.find_element(By.XPATH, PASSWORD_REGISTRATION).send_keys('123')

        driver.find_element(By.XPATH, BUTTON_REGISTRATION).click()


        assert driver.find_element(By.XPATH, "//p[text()='Некорректный пароль']")



