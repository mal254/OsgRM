import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time

class LoginPage(BasePage):

    PAGE_URL = Links.LOGIN_PAGE

    _EMAIL_FIELD = ("xpath", "//input[@formcontrolname='email']")
    _PASSWORD_FIELD = ("xpath", "//input[@formcontrolname='password']")
    _SUBMIT_BUTTON = ("xpath", "//button[@id='loginform-enter-button']")
    _PASSWORD_RECOVERY_BUTTON = ("xpath", "//button[@id='loginform-resore-link']")

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step("Enter login")
    def enter_login(self, login):
        self.wait.until(EC.element_to_be_clickable(self._EMAIL_FIELD)).send_keys(login)
    @allure.step("Enter password")
    def enter_password(self, password):
        self.wait.until(EC.element_to_be_clickable(self._PASSWORD_FIELD)).send_keys(password)

    @allure.step("Testing the button")
    def testing_thee_button(self):
        self.wait.until(EC.visibility_of_element_located(self._PASSWORD_RECOVERY_BUTTON))
        self.wait.until(EC.element_to_be_clickable(self._PASSWORD_RECOVERY_BUTTON))
    @allure.step("Click submit button")
    def click_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self._SUBMIT_BUTTON)).click()
