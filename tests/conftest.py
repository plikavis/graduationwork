import allure
import requests
import pytest
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from selene import browser, have
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from config import settings
from utils import attach


@pytest.fixture(scope="class", autouse=True)
def browser_config(request):
    browser_version = settings.browser_version
    # browser_version = request.config.getoption('--browser_version')
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

    login = settings.login_selenoid
    password = settings.password_selenoid

    driver = webdriver.Remote(command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
                              options=options)
    browser.config.base_url = "https://graduationwork.testrail.io/index.php?"
    browser.config.driver = driver
    browser.config.window_width = 1440
    browser.config.window_height = 1024

    yield browser

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    browser.quit()


@pytest.fixture(scope="class")
def auth():
    with step("LOGIN"):
        result = requests.post(url=settings.base_url + "/index.php?/auth/login/",
                               data={'name': settings.LOGIN,
                                     'password': settings.PASSWORD},
                               allow_redirects=False)
        allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
        cookie_auth = result.cookies.get("tr_session")
        browser.open("/")
        browser.driver.add_cookie({"name": "tr_session", "value": cookie_auth})
        browser.open("/")
        browser.element(".navigation-username").should(have.text("Polina Test"))


@pytest.fixture(scope="class")
def auth_read():
    with step("LOGIN"):
        result = requests.post(url="https://graduationwork.testrail.io/index.php?/auth/login/",
                               data={'name': settings.LOGIN_READ,
                                     'password': settings.PASSWORD_READ},
                               allow_redirects=False)
        allure.attach(body=str(result.cookies), name="Cookies", attachment_type=AttachmentType.TEXT, extension="txt")
        cookie_auth = result.cookies.get("tr_session")
        browser.open(f"{settings.base_url}")
        browser.driver.add_cookie({"name": "tr_session", "value": cookie_auth})
        browser.open(f"{settings.base_url}")
        browser.element(".navigation-username").should(have.text("Autotest"))

