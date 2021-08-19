from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def isExist(self, by_locator):
        wait = WebDriverWait(self.driver, 10)
        result = wait.until(EC.visibility_of_element_located(by_locator))
        return result

    def clickElement(self, by_locator):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(by_locator)).click()

    def sendKeys(self, by_locator, text):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def getTitle(self, title):
        wait = WebDriverWait(self.driver, 10)
        wait.until(EC.title_is(title))
        return self.driver.title

    def getElement(self, by_locator):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.visibility_of_element_located(by_locator))
        return element
