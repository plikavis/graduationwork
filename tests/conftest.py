import allure
import pytest
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from selene import have
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from attach import attach
import requests
from selene import browser
from config import settings



@pytest.fixture(scope="function")
def browser_config_ui(request):
    browser_version = settings.BROWSER_VERSION
    browser_version = browser_version if browser_version != "" else "100"
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = settings.LOGIN_SELENOID
    password = settings.PASSWORD_SELENOID
    driver = webdriver.Remote(command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
                              options=options)
    browser.config.base_url = "https://graduationwork.testrail.io/index.php?"
    browser.config.driver = driver
    browser.config.window_width = 1440
    browser.config.window_height = 1440

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    browser.quit()


@pytest.fixture(scope="function")
def browser_config_api(request):
    browser_version = settings.BROWSER_VERSION
    browser_version = browser_version if browser_version != "" else "100"
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    login = settings.LOGIN_SELENOID
    password = settings.PASSWORD_SELENOID
    driver = webdriver.Remote(command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
                              options=options)
    browser.config.base_url = "https://graduationwork.testrail.io"
    browser.config.driver = driver
    browser.config.window_width = 1440
    browser.config.window_height = 1440

    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def auth():
    with step("LOGIN"):
        result = requests.post(url=settings.BASE_URL + "/index.php?/auth/login/",
                               data={'name': settings.LOGIN,
                                     'password': settings.PASSWORD},
                               allow_redirects=False)
        allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
        cookie_auth = result.cookies.get("tr_session")
        browser.open("/")
        browser.driver.add_cookie({"name": "tr_session", "value": cookie_auth})
        browser.open("/")
        browser.element(".navigation-username").should(have.text("Polina Test"))


@pytest.fixture(scope="function")
def auth_read():
    with step("LOGIN"):
        result = requests.post(url=settings.BASE_URL + "/index.php?/auth/login/",
                               data={'name': settings.LOGIN_READ,
                                     'password': settings.PASSWORD_READ},
                               allow_redirects=False)
        allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
        cookie_auth = result.cookies.get("tr_session")
        browser.open("/")
        browser.driver.add_cookie({"name": "tr_session", "value": cookie_auth})
        browser.open("/")
        browser.element(".navigation-username").should(have.text("Autotest"))


def api_add_project(name, announcement, show_announcement, suite_mode):
    cookie = browser.driver.get_cookie("tr_session")
    result = requests.post(url=settings.BASE_URL + settings.ENDPOINT + '/add_project/',
                           cookies={"tr_session": cookie['value']},
                           json={"name": name,
                                 "announcement": announcement,
                                 "show_announcement": show_announcement,
                                 "suite_mode": suite_mode},
                           headers={'Content-Type': 'application/json'})
    return result.json()["id"]


def api_delete_project(project_id):
    cookie = browser.driver.get_cookie("tr_session")
    result = requests.post(url=settings.BASE_URL + settings.ENDPOINT + f'/delete_project/{project_id}',
                           cookies={"tr_session": cookie['value']},
                           headers={'Content-Type': 'application/json'})
    return result.text

