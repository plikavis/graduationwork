import allure
import requests
import pytest
from allure_commons._allure import step
from allure_commons.types import AttachmentType
from selene import browser, have
from config import settings


@pytest.fixture(scope="class")
def browser_config():
    browser.config.timeout = 10.0
    browser.config.window_height = 900
    browser.config.window_width = 1028
    browser.config.base_url = "https://graduationwork.testrail.io/index.php?"


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
    yield
    browser.quit()
    # browser.driver.name = "Chrome"
    # webdriver.Remote для селенои

# фикстура чистки


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
    yield
    browser.quit()
