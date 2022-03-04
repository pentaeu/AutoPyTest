from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def fill_group_form(self, group):
        self.update_field_data("group_name", group.name)
        self.update_field_data("group_header", group.header)
        self.update_field_data("group_footer", group.footer)

    def update_field_data(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # Create group
        wd.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        # Submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group(wd)
        # Delete first group
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()

    def edit_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_group_page()
        self.select_first_group(wd)
        # Edit first group
        wd.find_element(By.NAME, "edit").click()
        self.fill_group_form(new_group_data)
        # Submit update
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()

    def select_first_group(self, wd):
        wd.find_element(By.NAME, "selected[]").click()

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()
