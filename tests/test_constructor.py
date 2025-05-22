
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


from locators import *


class TestConstructor:

    #тест перехода в конструктор по клику на «Конструктор»
    def test_transition_by_click_on_button_constructor(self, driver, user_login):

        driver.find_element(By.XPATH, BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, LINK_PROFILE)))

        driver.find_element(By.XPATH, BUTTON_CONSTRUCTOR).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, BUTTON_PLACE_ORDER)))

        assert driver.find_element(By.XPATH, BUTTON_PLACE_ORDER).text == 'Оформить заказ'

        driver.quit()
    #тест перехода в конструктор по клику на логотип Stellar Burgers
    def test_transition_by_click_on__logo(self, driver, user_login):

        driver.find_element(By.XPATH, BUTTON_PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, LINK_PROFILE)))

        driver.find_element(By.XPATH, LOGO_STELLAR_BURGERS).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, BUTTON_PLACE_ORDER)))

        assert driver.find_element(By.XPATH, BUTTON_PLACE_ORDER).text == 'Оформить заказ'

        driver.quit()

    #тест перехода к разделу Соус
    #"current" in driver.find_element(lskdjflksdjfkdjf).get_attribute("class") and "current" not in
    def test_transition_section_sauce(self, driver):
        driver.get(MAIN_PAGE_URL)

        driver.find_element(By.XPATH, SECTION_SAUCE).find_element(By.XPATH, './/span').click()

        assert  (
                "current" in driver.find_element(By.XPATH, SECTION_SAUCE).get_attribute("class")
                 and "current" not in driver.find_element(By.XPATH, SECTION_BUNS).get_attribute("class")
                 and "current" not in driver.find_element(By.XPATH, SECTION_FILLINGS).get_attribute("class")
                 )

        driver.quit()


    #тест перехода к разделу Булки
    def test_transition_section_buns(self, driver):
        driver.get(MAIN_PAGE_URL)

        driver.find_element(By.XPATH, SECTION_SAUCE).find_element(By.XPATH, './/span').click()
        driver.find_element(By.XPATH, SECTION_BUNS).find_element(By.XPATH, './/span').click()

        assert  (
                "current" in driver.find_element(By.XPATH, SECTION_BUNS).get_attribute("class")
                 and "current" not in driver.find_element(By.XPATH, SECTION_SAUCE).get_attribute("class")
                 and "current" not in driver.find_element(By.XPATH, SECTION_FILLINGS).get_attribute("class")
                 )

        driver.quit()


        #тест перехода к разделу Начинки
    def test_transition_section_fillings(self, driver):
        driver.get(MAIN_PAGE_URL)

        driver.find_element(By.XPATH, SECTION_FILLINGS).find_element(By.XPATH, './/span').click()

        assert (
                "current" in driver.find_element(By.XPATH, SECTION_FILLINGS).get_attribute("class")
                and "current" not in driver.find_element(By.XPATH, SECTION_BUNS).get_attribute("class")
                and "current" not in driver.find_element(By.XPATH, SECTION_SAUCE).get_attribute("class")
        )

        driver.quit()

