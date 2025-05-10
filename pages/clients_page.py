from pages.simple_practice_login_page import SimplePracticeLoginPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select


class ClientPage(SimplePracticeLoginPage):
    #locators to Navigate add client 
    MASTHEAD = (By.CSS_SELECTOR,"div[class*=nav-collapse-button-container]")
    CLIENT_OPT = (By.CSS_SELECTOR,"a[id='ember53']")
    PRESS_ADD_SYMBOL_DROP = (By.ID,"ember27") #div.ember-basic-dropdown-content ember27
    DISPLAY = (By.ID,"ember3158")
    ADD_USER = (By.CSS_SELECTOR,"#ember28 > button")
    FRAME = (By.ID,"ember-basic-dropdown-content")

    #Locators client detail
    NAME_CLIENT = (By.NAME,"firstName")
    LAST_NAME_CLIENT = (By.NAME,"lastName")
    CONTINUE = (By.CSS_SELECTOR,"#ember1224 > button")

    #Locator search
    SEARCHBAR = (By.ID,"spds-input-search-container-6-trigger-input")
    CATEGORY = (By.CSS_SELECTOR,"div[class*=category]")
    CLIENT = (By.CSS_SELECTOR,"div[class*=name]")


    def is_client_page_loaded(self):
        try:
            WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(self.MASTHEAD))
            return True
        except:
            return False
        
    def get_option_menu(self):
        WebDriverWait(self.driver,10).until(EC.element_to_be_clickable(self.CLIENT_OPT)).click()

    def isMenuOn(self):
        a = WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(self.FRAME)).is_displayed
        return a

    def open_sub(self):
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(self.PRESS_ADD_SYMBOL_DROP)).click()

    def open_overlay(self):
        WebDriverWait(self.driver,20).until(EC.element_to_be_clickable(self.ADD_USER)).click()

    def selectOption(self, option):
        #dropdown_element = WebDriverWait(self.driver,12).until(EC.element_to_be_clickable)
        dropdown_element = self.PRESS_ADD_SYMBOL_DROP
        select = Select(dropdown_element)
        select.select_by_index(int(option))

    #Methods to add user

    def addUser(self,clientName,clientlastName):
        WebDriverWait(self.driver,15).until(EC.element_to_be_clickable(self.NAME_CLIENT)).send_keys(clientName)
        WebDriverWait(self.driver,15).until(EC.element_to_be_clickable(self.LAST_NAME_CLIENT)).send_keys(clientlastName)
        WebDriverWait(self.driver,15).until(EC.element_to_be_clickable(self.CONTINUE)).click()

    def checkStatus(self, expected_status="ACTIVE CLIENTS"):
        """Check if the text within the CATEGORY div matches the expected status."""
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.CATEGORY)
            )
            actual_status = element.text.strip()
            assert actual_status == expected_status, f"Expected status '{expected_status}', but got '{actual_status}'"
            return True
        except (AssertionError, TimeoutException) as e:
            print(f"Status validation failed: {str(e)}")
            return False

    def checkName(self, clientName):
        """Check if the text within the CLIENT div matches the provided clientName."""
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located(self.CLIENT)
            )
            actual_name = element.text.strip()
            assert actual_name == clientName, f"Expected client name '{clientName}', but got '{actual_name}'"
            return True
        except (AssertionError, TimeoutException) as e:
            print(f"Name validation failed: {str(e)}")
            return False
