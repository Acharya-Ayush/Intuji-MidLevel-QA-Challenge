# web_setup.py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

def web_driver():
    options = Options()
    # Only use below option if you wanna run headless tests.
    # options.add_argument("--headless=new")  # NOTE: use new headless mode (Chrome 109+)
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-software-rasterizer") 
    options.add_argument("--no-sandbox") # For linux uses
    options.add_argument("--disable-accelerated-2d-canvas") # NOTE: disables extra GPU acceleration
    options.add_argument("--disable-dev-shm-usage") # NOTE: avoids memory issues in Docker/VMs

    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    driver.maximize_window()
    return driver
