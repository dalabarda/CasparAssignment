from base.BasePage import BasePage
import utilities.CustomLogger as cl


class IntroPageTest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators values in Contact us form
    _nextButton ="com.casparhealth.android.patient:id/next_button" # id
    _startButton = "com.casparhealth.android.patient:id/start_button"  # id


    def clickNextButton(self):
        self.clickElement(self._nextButton,"id")
        cl.allureLogs("Click on NEXT Button")

    def clickStartButton(self):
        self.clickElement(self._startButton,"id")
        cl.allureLogs("Click on NEXT Button")


    # Business layer - functions

    def navigate_to_login(self):
        self.clickNextButton()
        self.clickNextButton()
        self.clickStartButton()