import unittest
import pytest

from base.BasePage import BasePage
from pages.therapy_week_page import TherapyWeekPageTest

import utilities.CustomLogger as cl


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class TherapyWeekTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.tp = TherapyWeekPageTest(self.driver)
        self.bp = BasePage(self.driver)

    @pytest.mark.run(order=1)
    def test_chatWithTherapistGIF(self):
        cl.allureLogs("App Launched")
        self.tp.navigateToTherapyWeek()
        self.tp.clickOnExercisesCard()
        self.tp.clickOnTheFirstExerciseVideo()
        # if self.tp.checkInfoMsg():
        self.tp.clickOnYesButton()

        self.tp.clickOnSettingsButton()

        self.tp.clickOnMirrorSwitch()
        self.tp.clickOnAllowButton()
        self.tp.clickOnRecordSwitch()
        self.tp.clickOnSaveSettings()

        self.tp.clickOnSettingsButton()
        self.tp.xxx()


        #self.bp.keyCode(63)
        #self.driver.press_keycode(63)



