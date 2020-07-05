from base.BasePage import BasePage
import utilities.CustomLogger as cl


class LoginPageTest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    _loginbutton ="com.code2lead.kwad:id/Login" # id
    _signInButton = "3" # index
    _enterEmail = "Email or Caspar ID:" # text
    _enterPassword ="Password:" # text
    _clickloginButton ="com.code2lead.kwad:id/Btn3" # id
    _wrongCredentials = "Wrong Credentials" # text
    _pageTitle ="My Training" # text
    _enterText ="com.code2lead.kwad:id/Edt_admin" # id
    _submitButton ="SUBMIT" # text


    def enterEmail(self):
        self.sendText("LTB7620",self._enterEmail,"text")
        cl.allureLogs("Entered email id")

    def enterPassword(self):
        self.sendText("12345678",self._enterPassword,"text")
        cl.allureLogs("Entered Password")

    def clickOnLoginButton(self):
        self.clickElement(self._signInButton,"index")
        cl.allureLogs("Clicked on Login Button in Login Screen")

    # check whether the text of the main widget is displayed or not. Validating a successful login
    def verifyMainScreen(self):
        mainScreen = self.isDisplayed(self._pageTitle,"text")
        assert mainScreen == True
        cl.allureLogs("Opened Main Screen")


    # Business layer -
    def logging_in(self):
        self.enterEmail()
        self.enterPassword()
        self.clickOnLoginButton()
        self.verifyMainScreen()
        cl.allureLogs("You logged in successfully")