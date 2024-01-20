import json
import allure
import requests

from allure_commons.types import AttachmentType
from selene import browser
import jsonschema
from config import settings
from utils.attach import add_logs_request
from utils.utils import load_schema
from tests.conftest import api_add_project


@allure.title("Get project request with admin  access")
@allure.tag("API", "smoke")
@allure.feature("Projects")
@allure.label("owner", "Vishnyakova P.")
@allure.story("API: Adding API for projects")
@allure.step("API: Get project")
def test_get_project_successfully_200(browser_config_api, auth):
    with allure.step("Get cookie"):
        cookie = browser.driver.get_cookie("tr_session")
    with allure.step("Send request"):
        result = requests.get(url=settings.base_url + settings.api + '/get_project/377',
                              cookies={"tr_session": cookie['value']})
    with allure.step("Check answer: response status code, id, json structure"):
        assert result.status_code == 200
        assert result.json()['id'] == 377
        schema = load_schema("get_project.json")
        jsonschema.validate(result.json(), schema)
        add_logs_request(result)


@allure.title("Update project request with admin access")
@allure.tag("API", "smoke")
@allure.feature("Projects")
@allure.label("owner", "Vishnyakova P.")
@allure.story("API: Adding API for projects")
@allure.step("API: Update project")
def test_post_update_project_successfully_200(browser_config_api, auth):
    with allure.step("Get cookie"):
        cookie = browser.driver.get_cookie("tr_session")
    with allure.step("Send request"):
        project_id = api_add_project(name="New project21", announcement="Test",
                                     show_announcement=True, suite_mode=2)
        result = requests.post(url=settings.base_url + settings.api + f'/update_project/{project_id}',
                               cookies={"tr_session": cookie['value']},
                               json={"name": "New_name --update from autotest",
                                     "announcement": "New announcement --update from autotest"})
    with allure.step("Check answer"):
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


@allure.title("Get project request with only read access")
@allure.tag("API", "regress")
@allure.feature("Projects")
@allure.label("owner", "Vishnyakova P.")
@allure.story("API: Adding API for projects")
@allure.step("API: Try to update unknown project")
def test_post_update_unknown_project_400(browser_config_api, auth):
    with allure.step("Get cookie"):
        cookie = browser.driver.get_cookie("tr_session")
    with allure.step("Send request"):
        result = requests.post(url=settings.base_url + settings.api + '/update_project/40004',
                               cookies={"tr_session": cookie['value']},
                               json={"name": "New_name",
                                     "announcement": "New announcement"})
    with allure.step("Check answer"):
        assert result.status_code == 400
        assert result.json() == {'error': 'Field :project_id is not a valid or accessible project.'}
        schema = load_schema("error.json")
        jsonschema.validate(result.json(), schema)
        allure.attach(body=str(result.request.url), name="Request URL", attachment_type=AttachmentType.TEXT,
                      extension="txt")
        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")


@allure.title("Delete project request with admin access")
@allure.tag("API", "smoke")
@allure.feature("Projects")
@allure.label("owner", "Vishnyakova P.")
@allure.story("API: Adding API for projects")
@allure.step("API: Delete project")
def test_post_delete_project_200(browser_config_api, auth):
    with allure.step("Get cookie"):
        cookie = browser.driver.get_cookie("tr_session")
    with allure.step("Send request"):
        project_id = api_add_project(name="New project21", announcement="Test",
                                     show_announcement=True, suite_mode=2)
        result = requests.post(url=settings.base_url + settings.api + f'/delete_project/{project_id}',
                               cookies={"tr_session": cookie['value']},
                               headers={'Content-Type': 'application/json'})
    with allure.step("Check answer"):
        assert result.text == ""
        assert result.status_code == 200
        allure.attach(body=str(result.request.url), name="Request URL", attachment_type=AttachmentType.TEXT,
                      extension="txt")
        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")


@allure.title("Get project request with only read access")
@allure.tag("API", "regress")
@allure.feature("Projects")
@allure.label("owner", "Vishnyakova P.")
@allure.story("API: Adding API for projects")
@allure.step("API: Try delete unknown project ")
def test_post_delete_unknown_project_400(browser_config_api, auth):
    with allure.step("Get cookie"):
        cookie = browser.driver.get_cookie("tr_session")
    with allure.step("Send request"):
        result = requests.post(url=settings.base_url + settings.api + f'/delete_project/4001',
                               cookies={"tr_session": cookie['value']},
                               headers={'Content-Type': 'application/json'})
    with allure.step("Check answer"):
        assert result.json() == {"error": "Field :project_id is not a valid or accessible project."}
        assert result.status_code == 400
        schema = load_schema("error.json")
        jsonschema.validate(result.json(), schema)
        allure.attach(body=str(result.request.url), name="Request URL", attachment_type=AttachmentType.TEXT,
                      extension="txt")
        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
