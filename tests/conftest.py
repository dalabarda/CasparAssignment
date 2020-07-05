from base.DriverClass import Driver
import pytest
import time


@pytest.yield_fixture(scope='class')
def beforeClass(request):
    print('Before Class')
    driver1 = Driver()
    driver = driver1.getDriverMethod()
    if request.cls is not None:
        request.cls.driver = driver

    yield driver

    time.sleep(4)
    driver.quit()
    print('After Class')

@pytest.yield_fixture()
def beforeMethod():
    print('Before Method')
    yield
    print('After Method')