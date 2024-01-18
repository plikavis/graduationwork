import requests
from selene import browser

from config import settings


def api_add_project(name, announcement, show_announcement, suite_mode):
    cookie = browser.driver.get_cookie("tr_session")
    result = requests.post(url=settings.base_url + settings.api + '/add_project/',
                           cookies={"tr_session": cookie['value']},
                           json={"name": name,
                                 "announcement": announcement,
                                 "show_announcement": show_announcement,
                                 "suite_mode": suite_mode},
                           headers={'Content-Type': 'application/json'})
    return result.json()["id"]


def api_delete_project(project_id):
    cookie = browser.driver.get_cookie("tr_session")
    result = requests.post(url=settings.base_url + settings.api + f'/delete_project/{project_id}',
                           cookies={"tr_session": cookie['value']},
                           headers={'Content-Type': 'application/json'})
    return result.text
