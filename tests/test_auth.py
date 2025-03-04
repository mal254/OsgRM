import allure
import pytest
from base.base_test import BaseTest

@allure.feature("Authorization in the personal account")
class TestProfileFeature(BaseTest):

    @allure.title("Authorization")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_auth(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        self.login_page.testing_thee_button()
        self.login_page.click_submit_button()
        self.docs_page.click_button_docs()
        self.docs_page.click_button_search()
        self.docs_page.field_check()
        self.docs_page.make_screenshot("Success")