from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os


def web_driver():
    os.environ['WDM_LOCAL'] = '1'
    os.environ['WDM_DIR'] = './drivers'

    driver = webdriver.Chrome(ChromeDriverManager().install())
    return driver