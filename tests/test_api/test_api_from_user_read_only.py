import pytest
import requests
from selene import browser
from config import settings


@pytest.mark.usefixtures("auth_read")
class TestUserReadOnly:
    def test_get_project_no_access_403(self, auth_read):
        cookie = browser.driver.get_cookie("tr_session")
        result = requests.get(url=settings.base_url + settings.api + '/get_project/1',
                              cookies={"tr_session": cookie['value']})
        assert result.status_code == 403
        assert result.json() == {"error": "The requested project does not exist or you do not"
                                          " have the permissions to access it."}

    def test_post_delete_project_user_read_only_403(self, auth_read):
        cookie = browser.driver.get_cookie("tr_session")
        result = requests.post(url=settings.base_url + settings.api + '/delete_project/1',
                               cookies={"tr_session": cookie['value']},
                               headers={'Content-Type': 'application/json'})
        assert result.json() == {"error": "You are not allowed to delete projects (requires administrator privileges)."}
        assert result.status_code == 403
