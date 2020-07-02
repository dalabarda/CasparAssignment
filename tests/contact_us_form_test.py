from base.DriverClass import Driver
import utilities.CustomLogger as cl
from base.BasePage import BasePage

driver1 = Driver()
log = cl.customLogger()

driver = driver1.getDriverMethod()
bp = BasePage(driver)

log.info("Launch APP")
# element = bp.waitForElement("")
# element.click()

bp.clickElement("com.code2lead.kwad:id/ContactUs", "id")