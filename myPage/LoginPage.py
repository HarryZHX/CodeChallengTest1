from myPage.BasePage import BasePage
from selenium.webdriver.common.by import By
from Config.config import TestData


class LoginPage(BasePage):
    # by locators
    username = (By.ID, "username")
    password = (By.ID, "password")
    signButton = (By.ID, "edit-actions")
    forgetPasswordText = (By.CLASS_NAME, "link-font-login")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.base_url)
        self.driver.find_element_by_class_name("landing-page__button-holder").click()

    def getLoginpageTitle(self, title):
        return self.getTitle(title)

    def isForgetPasswordTextExist(self):
        return self.isExist(self.forgetPasswordText)

    """login function"""

    def do_login(self, username, password):
        self.sendKeys(self.username, username)
        self.sendKeys(self.password, password)
        self.clickElement(self.signButton)

