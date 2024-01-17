import pytest
from selene import browser
from config import settings
import allure
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType


@pytest.mark.usefixtures("browser_config", "auth_read")
class TestUserReadOnly:
    def test_get_project_no_access_403(self, auth_read):
        with step("Get cookie"):
            cookie = browser.driver.get_cookie("tr_session")
        with step("Send request"):
            result = requests.get(url=settings.base_url + settings.api + '/get_project/1',
                                  cookies={"tr_session": cookie['value']})
        with step("Check answer"):
            assert result.status_code == 403
            assert result.json() == {"error": "The requested project does not exist or you do not"
                                              " have the permissions to access it."}
            allure.attach(body=str(result.request.url), name="Request URL", attachment_type=AttachmentType.TEXT,
                          extension="txt")
            allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
            allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    def test_post_delete_project_user_read_only_403(self, auth_read):
        with step("Get cookie"):
            cookie = browser.driver.get_cookie("tr_session")
        with step("Send request"):
            result = requests.post(url=settings.base_url + settings.api + '/delete_project/1',
                                   cookies={"tr_session": cookie['value']},
                                   headers={'Content-Type': 'application/json'})
        with step("Check answer"):
            assert result.json() == {"error": "You are not allowed to delete projects "
                                              "(requires administrator privileges)."}
            assert result.status_code == 403
            allure.attach(body=str(result.request.url), name="Request URL", attachment_type=AttachmentType.TEXT,
                          extension="txt")
            allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
            allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
