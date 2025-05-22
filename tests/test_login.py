
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

from locators import MAIN_PAGE_URL, LOGIN_FORM, LOGIN_MAIN_PAGE_BUTTON, LOGIN_FORM_EMAIL, LOGIN_FORM_PASSWORD, \
    LOGIN_FORM_BUTTON, BUTTON_PLACE_ORDER, BUTTON_PERSONAL_ACCOUNT, Registration_URL, BUTTON_LOGIN_REGISTRATION, \
    FORGOT_PASSWORD_URL, BUTTON_LOGIN_FORGOT_PASSWORD


class TestLogin():


    #тест входа по кнопке «Войти в аккаунт» на главной странице
    def test_login_button_main_page(self, driver,user_register):

        driver.get(MAIN_PAGE_URL)

        driver.find_element(By.XPATH, LOGIN_MAIN_PAGE_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_FORM)))

        driver.find_element(By.XPATH, LOGIN_FORM_EMAIL ).send_keys(user_register['email'])
        driver.find_element(By.XPATH, LOGIN_FORM_PASSWORD).send_keys(user_register['password'])
        driver.find_element(By.XPATH, LOGIN_FORM_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, BUTTON_PLACE_ORDER)))

        assert driver.find_element(By.XPATH, BUTTON_PLACE_ORDER).text == 'Оформить заказ'

        driver.quit()

    #тест входа через кнопку «Личный кабинет»
    def test_login_personal_accaunt(self, driver, user_register):
        driver.get(MAIN_PAGE_URL)

        driver.find_element(By.XPATH, BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_FORM)))

        driver.find_element(By.XPATH, LOGIN_FORM_EMAIL).send_keys(user_register['email'])
        driver.find_element(By.XPATH, LOGIN_FORM_PASSWORD).send_keys(user_register['password'])
        driver.find_element(By.XPATH, LOGIN_FORM_BUTTON).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, BUTTON_PLACE_ORDER)))

        assert driver.find_element(By.XPATH, BUTTON_PLACE_ORDER).text == 'Оформить заказ'

        driver.quit()

    def test_login_in_form_registration(self, driver, user_register):
        driver.get(Registration_URL)

        driver.find_element(By.XPATH, BUTTON_LOGIN_REGISTRATION).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_FORM)))

        driver.find_element(By.XPATH, LOGIN_FORM_EMAIL).send_keys(user_register['email'])
        driver.find_element(By.XPATH, LOGIN_FORM_PASSWORD).send_keys(user_register['password'])
        driver.find_element(By.XPATH, LOGIN_FORM_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, BUTTON_PLACE_ORDER)))

        assert driver.find_element(By.XPATH, BUTTON_PLACE_ORDER).text == 'Оформить заказ'

        driver.quit()

    #тест входа через кнопку в форме восстановления пароля.
    def test_forgot_password(self, driver, user_register):
        driver.get(FORGOT_PASSWORD_URL)

        driver.find_element(By.XPATH, BUTTON_LOGIN_FORGOT_PASSWORD).click()

        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_FORM)))

        driver.find_element(By.XPATH, LOGIN_FORM_EMAIL).send_keys(user_register['email'])
        driver.find_element(By.XPATH, LOGIN_FORM_PASSWORD).send_keys(user_register['password'])
        driver.find_element(By.XPATH, LOGIN_FORM_BUTTON).click()

        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located((By.XPATH, BUTTON_PLACE_ORDER)))

        assert driver.find_element(By.XPATH, BUTTON_PLACE_ORDER).text == 'Оформить заказ'

        driver.quit()

