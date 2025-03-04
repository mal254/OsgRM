import pytest
from config.data import Data
from pages.login_page import LoginPage
from pages.docs_page import DocsPage



class BaseTest:

    data: Data
    login_page: LoginPage
    docs_page: DocsPage


    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.data = Data()
        request.cls.login_page = LoginPage(driver)
        request.cls.docs_page = DocsPage(driver)