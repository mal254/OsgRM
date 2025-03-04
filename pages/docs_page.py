import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import time

class DocsPage(BasePage):

    PAGE_URL = Links.DOC_PAGE

    _DOC_BUTTON = ("xpath", "//button[@id='documents-and-scans-menu']")
    _SEARCH_BUTTON = ("xpath", "//button[@id='search-dialog-button-search']")
    _FIRST_FIELD = ("xpath", "//mat-checkbox[@id='mat-checkbox-9']")

    @allure.step("Click button docs")
    def click_button_docs(self):
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable(self._DOC_BUTTON)).click()
    @allure.step("Click button search")
    def click_button_search(self):
        time.sleep(5)
        self.wait.until(EC.element_to_be_clickable(self._SEARCH_BUTTON)).click()
    @allure.step("Field check")
    def field_check(self):
        self.wait.until(EC.visibility_of_element_located(self._FIRST_FIELD))
