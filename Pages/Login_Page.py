import pytest
from selenium.webdriver.common.by import By
from Config.Test_Data import TestData
from Pages.Base_Page import BasePage
from Tests.test_HomePage import HomePage
import time

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

        self.driver.get(TestData.Base_URL)

    User = (By.XPATH, "//a[contains(text(),'Users')]//ancestor::div[@id='mobMenu']")
    How_it_works = (By.XPATH, "//li[@id='menu-item-72']/a")
    Key_Features = (By.XPATH, "//li[@id='menu-item-73']/a[contains(text(),'Key Features')]")
    Contact = (By.XPATH, "//li[@id='menu-item-74']/a[contains(text(),'Contact')]")
    Login = (By.XPATH, "//a[normalize-space()='Login']")
    Sign_Up = (By.XPATH, "//a[contains(text(),'SignUp')]")
    Main_Title = (By.XPATH, "//h1")
    Sub_title = (By.XPATH, "//h3[@class='hero-sub-title _mobile']")
    Username = (By.XPATH, "//input[@name='username']")
    Password = (By.XPATH, "//input[@name='password']")
    Login_submit = (By.XPATH, "//button[@type='submit']")
    Header = (By.ID, "#resizableTitle")
    New_project = (By.XPATH, "//h1")

    Scr_Sh = "Screenshots/test_LoginPage.png"

    def do_login(self , username , password):
        self.do_click(self.Login)
        self.do_clear ( self.Username )
        self.do_send_keys ( self.Username, username )
        self.do_clear(self.Password)
        self.do_send_keys ( self.Password , password )
        self.do_click ( self.Login_submit )
        return HomePage ( self.driver )



