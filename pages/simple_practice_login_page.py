import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class SimplePracticeLoginPage:
    URL = "https://secure.simplepractice.com"

    USERNAME_INPUT = (By.ID, "user_email")
    PASSWORD_INPUT = (By.ID, "user_password")
    LOGIN_BUTTON = (By.ID, "submitBtn")
    MASTHEADL = (By.CSS_SELECTOR, "div[class*=nav-collapse-button-container]")  # Update this selector as needed

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.USERNAME_INPUT)
        ).send_keys(username)
        self.driver.find_element(*self.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def is_logged_in(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.MASTHEADL)
            )
            return True
        except:
            return False