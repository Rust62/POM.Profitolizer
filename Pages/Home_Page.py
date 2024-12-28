from selenium.webdriver.common.by import By

from Config.Test_Data import TestData
from Pages.Base_Page import BasePage


class HomePage(BasePage):
	def __init__(self, driver):
		super().__init__(driver)




	User_name = (By.XPATH, "//span[@class='d-none d-md-block dropdown-toggle ps-2']")
	Log_out = (By.XPATH, "//span[normalize-space()='Log Out']")
	User_name_toggle = (By.XPATH , "//span[@class='d-none d-md-block dropdown-toggle ps-2']")
	Add_project = (By.XPATH, "//span[normalize-space()='Add Project']")
	New_project = (By.XPATH, "//h1")






