import random

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from helper import generate_email, generate_password
from locators import *
from urls import MAIN_PAGE_URL, Registration_URL


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def user_register(driver):
    driver.get(Registration_URL)

    driver.find_element(By.XPATH, NAME_REGISTRATION).send_keys('Marina')

    email = generate_email()
    password = generate_password()
    print(email, password)
    driver.find_element(By.XPATH, EMAIL_REGISTRATION).send_keys(email)
    driver.find_element(By.XPATH, PASSWORD_REGISTRATION).send_keys(password)
    driver.find_element(By.XPATH, BUTTON_REGISTRATION).click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_FORM)))

    return {'email': email, 'password': password}

@pytest.fixture
def user_login(driver):
    driver.get(MAIN_PAGE_URL)

    driver.find_element(By.XPATH, LOGIN_MAIN_PAGE_BUTTON).click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, LOGIN_FORM)))

    driver.find_element(By.XPATH, LOGIN_FORM_EMAIL).send_keys('MarinaIgnatieva23777@ya.ru')
    driver.find_element(By.XPATH, LOGIN_FORM_PASSWORD).send_keys('123456')
    driver.find_element(By.XPATH, LOGIN_FORM_BUTTON).click()

    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, BUTTON_PLACE_ORDER)))

    return True