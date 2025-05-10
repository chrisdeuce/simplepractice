import pytest
from pages.clients_page import ClientPage

@pytest.mark.usefixtures("browser")
class TestClientPage:

    def test_client_option(self,browser):
        page = ClientPage(browser)
        page.load()
        page.login("somab63683@lewenbo.com","GoodLuck777")

        #page.get_option_menu()
        page.open_sub()
        disp = page.isMenuOn()
        if(disp):
            page.open_sub()
            page.selectOption("0")
            page.addUser("Pedro","Navajas")

        page.checkStatus()
        page.checkName("Pedro Navajas")

        #assert page.is_logged_in()
        #assert page.is_client_page_loaded(), page.click