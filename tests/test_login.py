import pytest
import os
from dotenv import load_dotenv
from pages.simple_practice_login_page import SimplePracticeLoginPage

load_dotenv

@pytest.mark.usefixtures("browser")
class TestSimplePracticeLogin:

    def test_valid_login(self, browser):
        login_page = SimplePracticeLoginPage(browser)
        login_page.load()
        login_page.login("somab63683@lewenbo.com","GoodLuck777")
        assert login_page.is_logged_in(), "Login failed or invalid user"
