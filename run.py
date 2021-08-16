from os import getenv
from selenium import webdriver
from dotenv import load_dotenv
import tenfakefingers

load_dotenv()


driver = webdriver.Chrome()
email = getenv('email')
password = getenv('password')


tenfakefingers.login(driver, email, password)
# tenfakefingers.type(driver, 'portuguese')


# driver.quit()
