import pytest
from selene import browser, have, be


def test_add_new_project(auth):
    browser.element('[data-testid="sidebarProjectsAddButton"]').should(be.visible).click()
    browser.element('[data-testid="addProjectNameInput"]').type("New project by autotest 1")
    browser.element('[data-testid="addEditProjectAnnouncement"]').type("Announcement by autotest 1")
    browser.element('[data-testid="addEditProjectShowAnnouncement"]').should(be.visible).click()
    browser.element('[data-testid="addEditProjectSuiteModeSingleBaseline"]').should(be.visible).click() #сделать параметризированным
    browser.element('[data-testid="addEditProjectCaseStatusesEnabled"]').should(be.visible).click()
    browser.element('[data-testid="addEditProjectAddButton"]').should(be.visible).click()


# '[data-testid=""]'
def test_add_test_case_successfully(auth):
    browser.open("/suites/view/1")
    browser.all('[data-testid="suiteAddCaseLink"]').first.click()
    browser.element('[data-testid="addEditCaseTitle"]').type("New test case by autotest1")
    browser.element('[data-testid="addTestCaseButton"]').click()
    browser.element('[data-testid="messageSuccessDivBox"]').should(be.visible)
    #проверить что добавлен


def test_try_add_empty_test_case(auth):
    browser.open(API_URL + "/index.php?/suites/view/1")
    browser.all('[data-testid="suiteAddCaseLink"]').first.click()
    browser.element('[data-testid="addTestCaseButton"]').click()
    browser.element('.message message-error').should(be.visible).should(have.text("Field Title is a required field."))
    # проверить что не добавлен

def test_edit_test_case(auth):
    pass


def test_delete_test_case(auth):
    pass


def test_try_add_empty_project(auth):
    pass


def test_check_form_add_test_case():
    pass