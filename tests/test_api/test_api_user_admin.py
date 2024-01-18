import json
import allure
import pytest
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from selene import browser
import jsonschema
from config import settings
from utils.utils import load_schema
from tests.functions import api_add_project


@pytest.mark.usefixtures("browser_config", 'auth')
class TestAdminUser:
    def test_get_project_successfully_200(self, auth):
        with step("Get cookie"):
            cookie = browser.driver.get_cookie("tr_session")
        with step("Send request"):
            result = requests.get(url=settings.base_url + settings.api + '/get_project/1',
                                  cookies={"tr_session": cookie['value']})
        with step("Check answer"):
            assert result.status_code == 200
            assert result.json()['id'] == 1
            schema = load_schema("get_project.json")
            jsonschema.validate(result.json(), schema)
            allure.attach(body=str(result.request.url), name="Request URL", attachment_type=AttachmentType.TEXT,
                          extension="txt")
            allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
            allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    def test_post_update_project_successfully_200(self, auth):
        with step("Get cookie"):
            cookie = browser.driver.get_cookie("tr_session")
        with step("Send request"):
            new_project = api_add_project(name="New project21", announcement="Test",
                                          show_announcement=True, suit_mode=2, cookie=cookie)
            project_id = new_project["id"]
            result = requests.post(url=settings.base_url + settings.api + f'/update_project/{project_id}',
                                   cookies={"tr_session": cookie['value']},
                                   json={"name": "New_name --update from autotest",
                                         "announcement": "New announcement --update from autotest"})
        with step("Check answer"):
            schema_request = load_schema("update_project_200_request.json")
            jsonschema.validate(json.loads(result.request.body), schema_request)
            assert result.status_code == 200
            assert result.json()['name'] == "New_name --update from autotest"
            assert result.json()['announcement'] == "New announcement --update from autotest"
            schema = load_schema("update_project_200.json")
            jsonschema.validate(result.json(), schema)
            allure.attach(body=str(result.request.url), name="Request URL", attachment_type=AttachmentType.TEXT,
                          extension="txt")
            allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
            allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    def test_post_update_unknown_project_400(self, auth):
        with step("Get cookie"):
            cookie = browser.driver.get_cookie("tr_session")
        with step("Send request"):
            result = requests.post(url=settings.base_url + settings.api + '/update_project/404',
                                   cookies={"tr_session": cookie['value']},
                                   json={"name": "New_name",
                                         "announcement": "New announcement"})
        with step("Check answer"):
            assert result.status_code == 400
            assert result.json() == {'error': 'Field :project_id is not a valid or accessible project.'}
            allure.attach(body=str(result.request.url), name="Request URL", attachment_type=AttachmentType.TEXT,
                          extension="txt")
            allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
            allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    def test_post_delete_project_200(self, auth):
        with step("Get cookie"):
            cookie = browser.driver.get_cookie("tr_session")
        with step("Send request"):
            new_project = api_add_project(name="New project21", announcement="Test",
                                          show_announcement=True, suit_mode=2, cookie=cookie)
            project_id = new_project["id"]
            result = requests.post(url=settings.base_url + settings.api + f'/delete_project/{project_id}',
                                   cookies={"tr_session": cookie['value']},
                                   headers={'Content-Type': 'application/json'})
        with step("Check answer"):
            assert result.text == ""
            assert result.status_code == 200
            allure.attach(body=str(result.request.url), name="Request URL", attachment_type=AttachmentType.TEXT,
                          extension="txt")
            allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
            allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")

    def test_post_delete_unknown_project_400(self, auth):
        with step("Get cookie"):
            cookie = browser.driver.get_cookie("tr_session")
        with step("Send request"):
            result = requests.post(url=settings.base_url + settings.api + f'/delete_project/4001',
                                   cookies={"tr_session": cookie['value']},
                                   headers={'Content-Type': 'application/json'})
        with step("Check answer"):
            assert result.json() == {"error": "Field :project_id is not a valid or accessible project."}
            assert result.status_code == 400
            allure.attach(body=str(result.request.url), name="Request URL", attachment_type=AttachmentType.TEXT,
                          extension="txt")
            allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
            allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
