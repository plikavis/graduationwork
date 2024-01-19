from selene import browser
from config import settings
import allure
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType




@allure.id("288")
@allure.title("Get project request with only read access")
@allure.tag("API", "regress")
@allure.feature("Projects")
@allure.label("owner", "Vishnyakova P.")
@allure.story("API: Adding API for projectst")
@allure.step("API: Try to get project without access`")
def test_get_project_no_access_403(browser_config, auth_read):
    with allure.step("Get cookie"):
        cookie = browser.driver.get_cookie("tr_session")
    with allure.step("Send request"):
        result = requests.get(url=settings.base_url + settings.api + '/get_project/377',
                              cookies={"tr_session": cookie['value']})
    with allure.step("Check answer"):
        assert result.status_code == 403
        assert result.json() == {"error": "The requested project does not exist or you do not"
                                          " have the permissions to access it."}
        allure.attach(body=str(result.request.url), name="Request URL", attachment_type=AttachmentType.TEXT,
                      extension="txt")
        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")


@allure.id("288")
@allure.title("Delete project request with only read access")
@allure.tag("API", "regress")
@allure.feature("Projects")
@allure.label("owner", "Vishnyakova P.")
@allure.story("API: Adding API for projectst")
@allure.step("API:Try delete project  with only read access")
def test_post_delete_project_user_read_only_403(browser_config, auth_read):
    with allure.step("Get cookie"):
        cookie = browser.driver.get_cookie("tr_session")
    with allure.step("Send request"):
        result = requests.post(url=settings.base_url + settings.api + '/delete_project/377',
                               cookies={"tr_session": cookie['value']},
                               headers={'Content-Type': 'application/json'})
    with allure.step("Check answer"):
        assert result.json() == {"error": "You are not allowed to delete projects "
                                          "(requires administrator privileges)."}
        assert result.status_code == 403
        allure.attach(body=str(result.request.url), name="Request URL", attachment_type=AttachmentType.TEXT,
                      extension="txt")
        allure.attach(body=result.text, name="Response", attachment_type=AttachmentType.TEXT, extension="txt")
        allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
