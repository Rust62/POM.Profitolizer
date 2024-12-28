from Config.Test_Data import TestData
from Pages.Login_Page import LoginPage
from Tests.test_Base import BaseTest



class Test_Login(BaseTest):

	def test_log_page_title(self):
		self.loginPage = LoginPage(self.driver)
		title = self.loginPage.get_title(TestData.Login_Page_Title)
		assert title == "Home - Profitolizer"


	def test_login_panel_is_visible(self):
		self.loginPage = LoginPage(self.driver)
		#logger.info ( "**********Verify that Admin area demo is visible**************" )
		flag = self.loginPage.is_visible(LoginPage.Main_Title)
		assert flag


	def test_login(self):
		self.loginPage = LoginPage ( self.driver )
		self.loginPage.do_login ( TestData.username , TestData.password)
		text = self.loginPage.get_element_text(LoginPage.New_project)
		print(f"print the text SO i can see it: {text}")
		assert text == "New Project"
