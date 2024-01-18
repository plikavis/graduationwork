from selene import browser, have, be, command


class Case:
    def open_cases_page(self, project_id):
        browser.open(f"/suites/overview/{project_id}")
        return self

    def click_add_case_button(self):
        browser.element('[data-testid="sidebarCasesAdd"]').click()
        return self

    def input_case_name(self):
        browser.element('[data-testid="addEditCaseTitle"]').with_(timeout=2.0).type("New test case by autotest1")
        return self

    def click_add_case_button_for_create(self,):
        browser.element('[data-testid="addTestCaseButton"]').click()
        return self

    def check_message_edit_success(self):
        browser.element('[data-testid="messageSuccessDivBox"]').should(have.text("Successfully updated the test case."))
        return self

    def click_add_next_button(self):
        browser.element("#accept_and_next").click()
        return self

    def check_message_fail(self):
        browser.element('#content-inner > div.message.message-error').should(be.visible).should(
            have.text("Field Title is a required field."))
        return self

    def click_edit_case_button(self):
        browser.element('[data-testid="testCaseEditButton"]').click()
        return self

    def click_save_button(self):
        browser.element('[data-testid="addTestCaseButton"]').click()
        return self

    def open_case_card(self):
        browser.open("/cases/view/2275")
        return self

    def check_message_create_success(self):
        browser.element('[data-testid="messageSuccessDivBox"]').should(have.text("Successfully added the new test case."))
        return self
