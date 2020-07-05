import unittest
import pytest
import utilities.CustomLogger as cl
from base.BasePage import BasePage
from pages.intro_page import IntroPageTest


@pytest.mark.usefixtures("beforeClass", "beforeMethod")
class IntroTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.it = IntroPageTest(self.driver)
        self.bp = BasePage(self.driver)

    @pytest.mark.run(order=1)
    def test_passingThroughIntro(self):
        self.it.clickNextButton()
        self.it.clickNextButton()
        self.it.clickStartButton()

