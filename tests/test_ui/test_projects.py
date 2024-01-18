import pytest
from allure_commons._allure import step
from selene import browser
from graduation_work.project_page import Project
from tests.functions import api_add_project, api_delete_project


@pytest.mark.usefixtures("browser_config", "auth")
class TestProject:
    def test_add_new_project(self, auth):
        project = Project()
        with step("Click add project"):
            project.click_add_project_button()
        with step("Print project name and announcement"):
            project.input_project_data()
        with step("Click show announcement"):
            project.click_show_announcement()
        with step("Choose suite mode Base"):
            project.choose_siute_mode_base()
        with step("Choose show cases"):
            project.choose_enable_cases()
        with step("Click button add new project"):
            project.click_add_project_button_for_create()
        with step("Check message adding new project succesfully"):
            project.check_message_adding_new_project()

    def test_try_add_empty_name_project(self, auth):
        project = Project()
        with step("Go to main page"):
            browser.open("/")
        with step("Click add project"):
            project.click_add_project_button()
        with step("Click button add new project"):
            project.click_add_project_button_for_create()
        with step("Check error message"):
            project.check_error_message_adding_project()

    def test_edit_project(self):
        with step("Add new project"):
            project = Project()
            project_id = api_add_project(name="Project for edit",
                                         announcement="announcement for edit",
                                         show_announcement=True,
                                         suite_mode=2)
        with step(f"Go to new project page with id {project_id}"):
            project.go_to_project_page(project_id)
        with step("Click edit button"):
            project.click_edit_button()
        with step("Type new name and announcement"):
            project.input_project_data()
        with step("Click Save button"):
            project.click_save_button()
        with step("Check message about changing"):
            project.check_success_message_editing_project()
        with step("Delete project"):
            api_delete_project(project_id)

    def test_search_and_open_project(self):
        with step("Search project"):
            browser.element("#search_query").click().type("First project")
        with step("Click to project in search result"):
            browser.element("#newSearchResultsContent > div:nth-child(2) > ul > li > a").click()
        with step("Check name of open project"):
            pass


