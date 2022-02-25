from selenium.webdriver.common.by import By


class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_group_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_group_page()
        # Create group
        wd.find_element(By.NAME, "new").click()
        # Fill group form
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(group.name)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(group.header)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(group.footer)
        # Submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        # Select first group
        wd.find_element(By.NAME, "selected[]").click()
        # Delete first group
        wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()

    def update_first_group(self):
        wd = self.app.wd
        self.open_group_page()
        # Select first group
        wd.find_element(By.NAME, "selected[]").click()
        # Update first group
        wd.find_element(By.NAME, "edit").click()
        # Fill new form
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys("awda123123123213")
        # Submit update
        wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()


    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()