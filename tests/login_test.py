import unittest
import pytest
import utilities.CustomLogger as cl
from base.BasePage import BasePage
from pages.login_page import LoginPageTest


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class LoginTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.lp = LoginPageTest(self.driver)
        self.bp = BasePage(self.driver)

    #
    @pytest.mark.run(order=2)
    def test_enterDataInLoginForm(self):
        self.lp.enterEmail()
        self.lp.enterPassword()
        self.lp.clickOnLoginButton()
        self.lp.verifyMainScreen()
        cl.allureLogs("You logged in successfully")



    # create others logins test cases
        # login failing
        # characters accepted to login
        # minimum characters accepted
        # ...