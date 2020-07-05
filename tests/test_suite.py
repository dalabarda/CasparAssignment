# 1. Import the files
import  unittest
from tests.login_test import LoginTest
from tests.intro_test import IntroTest


# 2. Create the object of the class using unitTest
lt = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
it = unittest.TestLoader().loadTestsFromTestCase(IntroTest)
# 3. Create TestSuite
regressionTest = unittest.TestSuite([it, lt])

# 4. Call the Test Runner method
unittest.TextTestRunner(verbosity=1).run(regressionTest)



# This file is just as example for multi test plan execution

