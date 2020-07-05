## CasparAssignment

Here you find the test automation stack used for this assignment \
Tools and materials for setting up test environment:


__1. Install the latest python x64 (3.8.3)__ \
--- [Python 3.8.3](https://www.python.org/downloads/release/python-383/) Follow the default instalation process.
	
__2. Appium and python libraries ([Appium Python Client](https://pypi.org/project/Appium-Python-Client/))__ \
---	``` pip install Appium-Python-Client ``` \
---	``` pip install -r requirements.txt ```  -> to install other libs


__3. PyCharm Community version IDE__ \
--- Follow the default installation process.

___4. Appium Desktop file configuration:___ \
--- https://appium.io/

__5. Android Studio Installation__ \
--- https://developer.android.com/studio

__6. Install Java:__ \
--- https://www.java.com/en/download/win10.jsp \
Java JRE is important to manage virtual devices. 

---
After several attempts trying to make the virtual machine working, the approach used to 
accomplish this exercise was using my own device to automate one test case. 

The objective of this repo is provide execution of one test case automated.   The design pattern of choise is Page Object Model (POM)

POM is an Object Repository design pattern which  creates our testing code maintainable, reusable. 
Under this model, for each web page in the application, there should be a corresponding Page Class. This Page class will identify the WebElements of that web page and also contains Page methods which perform operations on those WebElements. Name of these methods should be given as per the task they are performing