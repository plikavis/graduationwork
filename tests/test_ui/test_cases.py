import pytest
from allure_commons._allure import step
from graduation_work.case_page import Case
from tests.functions import api_add_project, api_delete_project



@pytest.mark.usefixtures("browser_config", "auth")
class TestTestCases:
    def test_add_test_case_successfully(self, auth):
        case = Case()
        with step("Create new project and get its id"):
            project_id = api_add_project(name="Project for add case",
                                         announcement="announcement for add case",
                                         show_announcement=True,
                                         suite_mode=1)
        with step(f"Go to cases page for project with id - {project_id}"):
            case.open_cases_page(project_id)
        with step("Click 'Add case' button"):
            case.click_add_case_button()
        with step("Input case's name "):
             case.input_case_name()
        with step("Click create button"):
            case.click_add_case_button_for_create()
        with step("Check message about success"):
            case.check_message_success("Successfully added the new test case.")
        with step(f"Delete case with id - {project_id}"):
            api_delete_project(project_id=project_id)

    def test_try_add_empty_test_case(self, auth):
        case = Case()
        with step(f"Go to cases page for project with id - 1"):
            case.open_cases_page(1)
        with step("Click 'Add case' button"):
            case.click_add_case_button()
            # browser.all('[data-testid="suiteAddCaseLink"]').first.click()
        with step("Click 'Add and next' button"):
            case.click_add_next_button()
        with step("Check message about fail"):
            case.check_message_fail()

    def test_edit_test_case(self, auth):
        case = Case()
        with step("Open case card in First project"):
            case.open_case_card()
        with step("Click edit button"):
            case.click_edit_case_button()
        with step("Input new case's name"):
            case.input_case_name()
        with step("Click Save Title button"):
            case.click_save_button()
        with step("Check success message"):
            case.check_message_success("Successfully updated the test case.")




