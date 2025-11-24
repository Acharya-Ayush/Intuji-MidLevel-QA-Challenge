from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium_tests.setup.data_entry import *



def web_driver(test_name, build_name=build_name):
    options = ChromeOptions()
    options.browser_version = 'latest'
    options.platform_name = 'Windows 10'
    sauce_options = {}
    sauce_options['username'] = saucelabs_username
    sauce_options['accessKey'] = saucelabs_key
    sauce_options['build'] = build_name
    sauce_options['screenResolution'] = '1920x1080'
    sauce_options['name'] = test_name
    sauce_options['extendedDebugging'] = True
    sauce_options['pageLoadStrategy'] = 'none' # or eager
    #sauce_options['capturePerformance'] = True
    sauce_options['timeZone'] = timezone
    options.set_capability('sauce:options', sauce_options)

    url = "https://ondemand.eu-central-1.saucelabs.com:443/wd/hub"
    driver = webdriver.Remote(command_executor=url, options=options)
    driver.maximize_window()

    return driver