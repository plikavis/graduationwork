import requests
import pytest
from selene import browser, have
from config import settings


@pytest.fixture(scope="session", autouse=True)
def browser_config():
    browser.config.timeout = 3.0
    browser.config.window_height = 900
    browser.config.window_width = 1028
    browser.config.base_url = "https://graduationwork.testrail.io/index.php?"


@pytest.fixture(scope="class")
def auth():
    result = requests.post(url=settings.base_url + "/index.php?/auth/login/",
                           data={'name': settings.LOGIN,
                                 'password': settings.PASSWORD},
                           allow_redirects=False)
    cookie_auth = result.cookies.get("tr_session")
    browser.open("/")
    browser.driver.add_cookie({"name": "tr_session", "value": cookie_auth})
    browser.open("/")
    browser.element(".navigation-username").should(have.text("Polina Test"))
    yield
    browser.close()
    # browser.driver.name = "Chrome"
    # webdriver.Remote для селенои


@pytest.fixture(scope="class")
def auth_read():
    result = requests.post(url="https://graduationwork.testrail.io/index.php?/auth/login/",
                           data={'name': settings.LOGIN_READ,
                                 'password': settings.PASSWORD_READ},
                           allow_redirects=False)
    cookie_auth = result.cookies.get("tr_session")
    browser.open(f"{settings.base_url}")
    browser.driver.add_cookie({"name": "tr_session", "value": cookie_auth})
    browser.open(f"{settings.base_url}")
    browser.element(".navigation-username").should(have.text("Autotest"))
    yield
    browser.close()
