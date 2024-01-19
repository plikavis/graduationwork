import allure
import pytest
from allure_commons._allure import step
from graduation_work.case_page import Case
from tests.functions import api_add_project, api_delete_project

@allure.id("288")
@allure.title("Try empty case and check message")
@allure.tag("UI", "regress")
@allure.feature("Cases")
@allure.label("owner", "Vishnyakova P.")
@allure.story("UI: Adding interface for cases")
def test_try_add_empty_test_case(browser_config, auth):
    case = Case()
    with step(f"Go to cases page for project with id - 1"):
        case.open_cases_page(1)
    with step("Click 'Add case' button"):
        case.click_add_case_button()
    with step("Click 'Add and next' button"):
        case.click_add_next_button()
    with step("Check message about fail"):
        case.check_message_fail()

@allure.id("250")
@allure.title("Get project request with only read access")
@allure.tag("UI", "Smoke")
@allure.feature("Cases")
@allure.label("owner", "Vishnyakova P.")
@allure.story("UI: Adding interface for cases")
def test_add_test_case_successfully(browser_config, auth):
    case = Case()
    with allure.step("Create new project and get its id"):
        project_id = api_add_project(name="for add case 21",
                                     announcement="announcement for add case",
                                     show_announcement=True,
                                     suite_mode=1)
    with allure.step(f"Go to cases page for project with id - {project_id}"):
        case.open_cases_page(project_id)
    with allure.step("Click 'Add case' button"):
        case.click_add_case_button()
    with allure.step("Input case's name "):
        case.input_case_name_for_add()
    with allure.step("Click create button"):
        case.click_add_case_button_for_create()
    with allure.step("Check message about success"):
        case.check_message_create_success()
    with allure.step(f"Delete case with id - {project_id}"):
        api_delete_project(project_id=project_id)

@allure.id("288")
@allure.title("Get project request with only read access")
@allure.tag("API", "regress")
@allure.feature("Cases")
@allure.label("owner", "Vishnyakova P.")
@allure.story("UI: Adding interface for cases")
def test_edit_test_case(browser_config, auth):
    case = Case()
    with allure.step("Open case card in First project"):
        case.open_case_card()
    with allure.step("Click edit button"):
        case.click_edit_case_button()
    with allure.step("Input new case's name"):
        case.input_case_name_for_edit()
    with allure.step("Click Save Title button"):
        case.click_save_button()
    with allure.step("Check success message"):
        case.check_message_edit_success()
