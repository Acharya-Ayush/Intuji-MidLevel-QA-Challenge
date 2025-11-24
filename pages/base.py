from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    #locator
    dropdown_container = (By.XPATH, "//div[contains(@id, 'listbox')]")


    def __init__(self, driver, wait_time=20):
        self.driver = driver
        self.wait_time = wait_time


    def find_element(self, locator, wait_time = 30):
        return WebDriverWait(self.driver, wait_time).until(
            EC.presence_of_element_located(locator)
        )


    def clear_element(self, locator):
        element = self.find_element(locator)
        element.click()
        #element.clear()
        element.send_keys(Keys.CONTROL + "a", Keys.DELETE)


    def insert_keys(self, locator, text, clear_element:bool=False):
        if clear_element is True:
            self.clear_element(locator)

        element = self.find_element(locator)
        element.send_keys(text)


    def navigate_to(self, url):
        self.driver.get(url)


    def click_element(self, locator, wait_time=30):
        WebDriverWait(self.driver, wait_time).until(
            EC.element_to_be_clickable(locator)
        ).click()

    def double_click_element(self, locator):
        element = self.wait_for_visibility(locator)
        ActionChains(self.driver).double_click(element).perform()

    def wait_for_visibility(self, locator, wait_time=30):
        return WebDriverWait(self.driver, wait_time).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_element_to_disappear(self, locator, wait_time=10):
        """waits until the element is no longer visible or present in DOM"""
        WebDriverWait(self.driver, wait_time).until(
            EC.invisibility_of_element_located(locator)
        )


    def type_and_select_from_dropdown(self, input_locator, dropdown_locator, text_to_select, contains :bool = True):
        """
        Types into a dropdown input field and selects an option based on the provided text.

        :param input_locator: Locator for the input field (By.<method>, 'value')
        :param dropdown_locator: Locator for the dropdown options container (By.<method>, 'value')
        :param text_to_select: The text of the option to select
        :param contains: If True the locator text_to_select uses contains() else it uses normalize-space()
        """
        self.clear_element(input_locator)
        self.insert_keys(input_locator, text_to_select)

        dropdown_container = self.wait_for_visibility(dropdown_locator)

        # Find the option to click that matches the provided text in dropdown container
        WebDriverWait(dropdown_container, 30).until(
            EC.visibility_of_element_located((By.XPATH, f".//*[contains(., '{text_to_select}')]"))
        )
        if contains is True:
            option = dropdown_container.find_element(By.XPATH, f".//*[contains(., '{text_to_select}')]")
        else:    
            option = dropdown_container.find_element(By.XPATH, f".//*[normalize-space(.) = '{text_to_select}']")
        
        self.click_element(option)
        print(f"{text_to_select} selected")


    def perform_right_click(self, locator):
        element = self.find_element(locator)
        actions = ActionChains(self.driver)
        actions.context_click(element).perform()


    def hover_over_element(self, locator_to_hover):
        element = self.wait_for_visibility(locator_to_hover)
        ActionChains(self.driver).move_to_element(element).perform()


    def get_element_text(self, locator):
        element = self.find_element(locator)
        return element.text


    def get_input_value(self, locator):
        input_field = self.find_element(locator)
        return input_field.get_attribute("value")


    def accept_alert(self):
        """Accepts the alert (Clicks OK)."""
        alert =  self.driver.switch_to.alert
        alert.accept()


    def dismiss_alert(self):
        """Dismisses the alert (Clicks Cancel)."""
        alert = self.driver.switch_to.alert
        alert.dismiss()















