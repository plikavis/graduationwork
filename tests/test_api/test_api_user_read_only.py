import jsonschema
from selene import browser
from config import settings
import allure
import requests

from testrail_project_test.utils.attach import add_logs_request
from utils import load_schema


@allure.title("Get project request with only read access")
@allure.tag("API", "regress")
@allure.feature("Projects")
@allure.label("owner", "Vishnyakova P.")
@allure.story("API: Adding API for projects")
@allure.step("API: Try to get project without access`")
def test_get_project_no_access_403(browser_config_api, auth_read):
    with allure.step("Get cookie"):
        cookie = browser.driver.get_cookie("tr_session")
    with allure.step("Send request"):
        result = requests.get(url=settings.BASE_URL + settings.ENDPOINT + '/get_project/377',
                              cookies={"tr_session": cookie['value']})
    with allure.step("Check answer"):
        assert result.status_code == 403
        assert result.json() == {"error": "The requested project does not exist or you do not"
                                          " have the permissions to access it."}
        schema = load_schema("error.json")
        jsonschema.validate(result.json(), schema)
        add_logs_request(result)


@allure.title("Delete project request with only read access")
@allure.tag("API", "regress")
@allure.feature("Projects")
@allure.label("owner", "Vishnyakova P.")
@allure.story("API: Adding API for projects")
@allure.step("API:Try delete project  with only read access")
def test_post_delete_project_user_read_only_403(browser_config_api, auth_read):
    with allure.step("Get cookie"):
        cookie = browser.driver.get_cookie("tr_session")
    with allure.step("Send request"):
        result = requests.post(url=settings.BASE_URL + settings.ENDPOINT + '/delete_project/377',
                               cookies={"tr_session": cookie['value']},
                               headers={'Content-Type': 'application/json'})
    with allure.step("Check answer"):
        assert result.json() == {"error": "You are not allowed to delete projects "
                                          "(requires administrator privileges)."}
        assert result.status_code == 403
        schema = load_schema("error.json")
        jsonschema.validate(result.json(), schema)
        add_logs_request(result)
