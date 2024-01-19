import allure
from selene import browser
from graduation_work.project_page import Project
from tests.functions import api_add_project, api_delete_project


@allure.title("Add new project")
@allure.tag("UI", "smoke")
@allure.feature("Projects")
@allure.label("owner", "Vishnyakova P.")
@allure.story("UI: Adding interface for projects")
@allure.step("UI: Add new project")
def test_add_new_project(browser_config, auth):
    project = Project()
    with allure.step("Click add project"):
        project.click_add_project_button()
    with allure.step("Print project name and announcement"):
        project.input_project_data()
    with allure.step("Click show announcement"):
        project.click_show_announcement()
    with allure.step("Choose suite mode Base"):
        project.choose_siute_mode_base()
    with allure.step("Choose show cases"):
        project.choose_enable_cases()
    with allure.step("Click button add new project"):
        project.click_add_project_button_for_create()
    with allure.step("Check message adding new project succesfully"):
        project.check_message_adding_new_project()


@allure.title("Try empty project and check message")
@allure.tag("UI", "regress")
@allure.feature("Projects")
@allure.label("owner", "Vishnyakova P.")
@allure.story("UI: Adding interface for projects")
@allure.step("UI: Try to add new project with empty name")
def test_try_add_empty_name_project(browser_config, auth):
    project = Project()
    with allure.step("Go to main page"):
        browser.open("/")
    with allure.step("Click add project"):
        project.click_add_project_button()
    with allure.step("Click button add new project"):
        project.click_add_project_button_for_create()
    with allure.step("Check error message"):
        project.check_error_message_adding_project()


@allure.title("Edit project name and save data")
@allure.tag("UI", "regress")
@allure.feature("Projects")
@allure.label("owner", "Vishnyakova P.")
@allure.story("UI: Adding interface for projects")
@allure.step("UI: Edit project")
def test_edit_project(browser_config, auth):
    with allure.step("Add new project"):
        project = Project()
        project_id = api_add_project(name="Project for edit",
                                     announcement="announcement for edit",
                                     show_announcement=True,
                                     suite_mode=2)
    with allure.step(f"Go to new project page with id {project_id}"):
        project.go_to_project_page(project_id)
    with allure.step("Click edit button"):
        project.click_edit_button()
    with allure.step("Type new name and announcement"):
        project.input_project_data()
    with allure.step("Click Save button"):
        project.click_save_button()
    with allure.step("Check message about changing"):
        project.check_success_message_editing_project()
    with allure.step("Delete project"):
        api_delete_project(project_id)


@allure.title("Check all tabs on project page")
@allure.tag("UI", "regress")
@allure.feature("Projects")
@allure.label("owner", "Vishnyakova P.")
@allure.story("UI: Adding interface for projects")
@allure.step("UI: Check all tabs in project")
def test_check_all_new_project_tabs(browser_config, auth):
    project = Project()
    with allure.step("Go to main page"):
        project.go_to_main_page()
    with allure.step("Click new project button"):
        project.click_add_project_button()
    with allure.step("Check all tabs in project form"):
        project.check_all_tabs()
