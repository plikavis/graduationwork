from selene import browser, have, command
from selene.support.conditions import be


class Project:
    def click_add_project_button(self):
        browser.element('[data-testid="sidebarProjectsAddButton"]').should(be.visible).click()
        return self

    def input_project_data(self):
        browser.element('[data-testid="addProjectNameInput"]').type("New project by autotest 1")
        browser.element('[data-testid="addEditProjectAnnouncement"]').type("Announcement by autotest 1")
        return self

    def click_show_announcement(self):
        browser.element('[data-testid="addEditProjectShowAnnouncement"]').should(be.visible).click()
        return self

    def choose_siute_mode_base(self):
        browser.element('[data-testid="addEditProjectSuiteModeSingleBaseline"]').should(
            be.visible).click()
        return self

    def choose_enable_cases(self):
        browser.element('[data-testid="addEditProjectCaseStatusesEnabled"]').should(be.visible).click()
        return self

    def click_add_project_button_for_create(self):
        browser.element('[data-testid="addEditProjectAddButton"]').perform(command.js.scroll_into_view)
        browser.element('[data-testid="addEditProjectAddButton"]').should(be.visible).click()
        return self

    def check_message_adding_new_project(self):
        browser.element('[data-testid="messageSuccessDivBox"]').should(
            have.text("Successfully added the new project."))
        return self

    def check_error_message_adding_project(self):
        browser.element('#content-inner > div.message.message-error').should(
             have.text("Field Name is a required field."))
        return self

    def go_to_project_page(self, id):
        browser.open(f"/projects/overview/{id}")
        return self

    def click_save_button(self):
        browser.element('[data-testid="addEditProjectAddButton"]').should(be.visible).click()
        return self

    def check_success_message_editing_project(self):
        browser.element('#content-inner > div.message.message-success').with_(timeout=3.0).should(
             have.text("Successfully updated the project."))
        return self

    def click_edit_button(self):
        browser.element('[data-testid="editProjectButton"]').should(be.visible).click()
        return self

    def go_to_main_page(self):
        browser.open("/")
        return self

    def check_all_tabs(self):
        browser.element('[data-testid="addProjectNameInput"]').should(be.visible)
        browser.element("#projects-tabs-access").click()
        browser.element('[data-testid="addEditProjectAccessTabGlobal"]').should(have.text("Global Role"))
        browser.element("#projects-tabs-defects").click()
        browser.element("#defect_id_url").should(be.visible)
        browser.element("#projects-tabs-references").click()
        browser.element("#reference_id_url").should(be.visible)
        browser.element("#users-fields-fields").click()
        browser.element("#addConfig").should(have.text("Add User Variable"))
        return self


project = Project()
