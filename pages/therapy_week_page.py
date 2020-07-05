from base.BasePage import BasePage
import utilities.CustomLogger as cl
from pages.intro_page import IntroPageTest
from pages.login_page import LoginPageTest

class TherapyWeekPageTest(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.ip = IntroPageTest(driver)
        self.lp = LoginPageTest(driver)

    # Locators values in Contact us form
    _actionTherapyWeek = "com.casparhealth.android.patient:id/action_therapy_week" # id
    _therapistChatIcon = "com.casparhealth.android.patient:id/action_chat" # id

    _exercisesCard = "com.casparhealth.android.patient:id/exercises" # id
    _firstExerciseVideo = "0" # index

    _infoMsgText = "com.casparhealth.android.patient:id/message_layout" # id
    _yesMsgButton = "YES" # text # "com.casparhealth.android.patient:id/yes_button" # id

    _settingsButton = "com.casparhealth.android.patient:id/settings_button" # id
    _mirrorSwitch = "com.casparhealth.android.patient:id/mirror_switch" # id
    _recordSwitch = "com.casparhealth.android.patient:id/record_switch" # id
    _permissionButton = "com.android.permissioncontroller:id/permission_allow_button" # id
    _saveSettings = "com.casparhealth.android.patient:id/save" # id

    def clickOnTherapyWeekButton(self):
        self.clickElement(self._actionTherapyWeek,"id")
        cl.allureLogs("Clicked on Therapist Chat Menu Button")

    def clickOnExercisesCard(self):
        self.clickElement(self._exercisesCard,"id")
        cl.allureLogs("Clicked on Exercises Card option")

    def clickOnTheFirstExerciseVideo(self):
        self.clickElement(self._firstExerciseVideo,"index")
        cl.allureLogs("Clicked on the first video displayed in the list")

    def checkInfoMsg(self):
        self.isDisplayed(self._infoMsgText, "id")

    def clickOnYesButton(self):
        self.clickElement(self._yesMsgButton,"text")

    def clickOnSettingsButton(self):
        self.clickElement(self._settingsButton,"id")

    def clickOnMirrorSwitch(self):
        self.clickElement(self._mirrorSwitch,"id")

    def clickOnRecordSwitch(self):
        self.clickElement(self._recordSwitch,"id")

    def clickOnAllowButton(self):
        self.clickElement(self._permissionButton, "id")

    def clickOnSaveSettings(self):
        self.clickElement(self._saveSettings,"id")

    def xxx(self):
        switch = self.getText(self._mirrorSwitch, "id")
        record = self.getText(self._recordSwitch, "id")
        assert switch == record


    # Business layer - functions

    def navigateToTherapyWeek(self):
        self.ip.navigate_to_login()
        self.lp.logging_in()
        self.clickOnTherapyWeekButton()