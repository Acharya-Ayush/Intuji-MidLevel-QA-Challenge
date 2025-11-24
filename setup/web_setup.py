from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def web_driver():
    options = ChromeOptions()
    options.browser_version = 'latest'
    options.platform_name = 'Windows 10'
    url = "https://ondemand.eu-central-1.saucelabs.com:443/wd/hub"
    driver = webdriver.Remote(command_executor=url, options=options)
    driver.maximize_window()

    return driver