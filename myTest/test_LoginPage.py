from myTest.test_Base import BaseTest
from myPage.LoginPage import LoginPage
from Config.config import TestData


class Test_Login(BaseTest):

    def test_forgetpasswordtext_visible(self):
        """create a object"""
        self.LoginPage = LoginPage(self.driver)
        result = self.LoginPage.isForgetPasswordTextExist()
        assert result

    def test_page_tile(self):
        self.LoginPage = LoginPage(self.driver)
        title = self.LoginPage.getTitle(TestData.loginpagetitle)
        assert title == TestData.loginpagetitle

    def test_login(self):
        self.LoginPage = LoginPage(self.driver)
        self.LoginPage.do_login(TestData.user_name, TestData.password)
        title = self.LoginPage.getTitle(TestData.Homepagetile)
        assert title == TestData.Homepagetile
