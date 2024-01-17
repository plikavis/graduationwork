import pytest
import requests
from allure_commons._allure import step
from selene import browser, have, be
from graduation_work.project_page import Project
from tests.functions import api_add_project, api_delete_project


@pytest.mark.usefixtures("browser_config", "auth")
class TestTestCases:
    def test_add_test_case_successfully(self, auth):
        browser.open("/suites/view/1")
        browser.all('[data-testid="suiteAddCaseLink"]').first.click()
        browser.element('[data-testid="addEditCaseTitle"]').type("New test case by autotest1")
        browser.element('[data-testid="addTestCaseButton"]').click()
        browser.element('[data-testid="messageSuccessDivBox"]').should(be.visible)
        # проверить что добавлен

    def test_try_add_empty_test_case(self, auth):
        browser.open("/suites/view/1")
        browser.all('[data-testid="suiteAddCaseLink"]').first.click()
        browser.element("#accept_and_next").click()
        browser.element('#content-inner > div.message.message-error').should(be.visible).should(have.text("Field Title is a required field."))
        # проверить что не добавлен

    def test_edit_test_case(self, auth):
        pass

    def test_delete_test_case(self, auth):
        pass



    def test_check_form_add_test_case(self, auth):
        pass
