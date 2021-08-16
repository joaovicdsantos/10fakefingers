from typing import NoReturn
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tenfakefingers.config import Config


def login(driver: WebDriver, email: str, password: str) -> NoReturn:
    '''Log into the 10fastfingers site'''

    driver.get(Config.login_url)

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, Config.id_email)))

    driver.find_element_by_id(Config.id_email).send_keys(email)
    driver.find_element_by_id(Config.id_password).send_keys(password)

    driver.find_element_by_id(Config.id_btn_login).click()


def type(driver: WebDriver, language: str) -> NoReturn:
    '''Start a desired language typing test'''

    driver.get(f'{Config.test_url}{language}')

    try:
        WebDriverWait(driver, 15).until(EC.presence_of_element_located(
            (By.ID, Config.id_cookie)))
        driver.find_element_by_id(Config.id_cookie).click()
    except:
        pass

    WebDriverWait(driver, 15).until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, Config.css_words)))
    words = driver.find_elements_by_css_selector(Config.css_words)

    input_field = driver.find_element_by_id(Config.id_input)

    [input_field.send_keys(word.get_attribute('innerHTML') + ' ')
     for word in words]
