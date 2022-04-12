from selenium.webdriver.common.by import By
from model.group import Group


class GroupHelper:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def open_group_page(self):
        if not (self.wd.current_url.endswith("/group.php") and len(self.wd.find_elements(By.NAME, "new")) > 0):
            self.wd.find_element(By.LINK_TEXT, "groups").click()

    def fill_group_form(self, group):
        self.update_field_data("group_name", group.name)
        self.update_field_data("group_header", group.header)
        self.update_field_data("group_footer", group.footer)

    def update_field_data(self, field_name, text):
        if text is not None:
            self.wd.find_element(By.NAME, field_name).click()
            self.wd.find_element(By.NAME, field_name).clear()
            self.wd.find_element(By.NAME, field_name).send_keys(text)

    def create(self, group):
        self.open_group_page()
        # Create group
        self.wd.find_element(By.NAME, "new").click()
        self.fill_group_form(group)
        # Submit group creation
        self.wd.find_element(By.NAME, "submit").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_index(self, index):
        self.open_group_page()
        self.select_group_by_index(index)
        # Delete first group
        self.wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def delete_group_by_id(self, id):
        self.open_group_page()
        self.select_group_by_id(id)
        # Delete first group
        self.wd.find_element(By.NAME, "delete").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_group_by_index(self, index, new_group_data):
        self.open_group_page()
        self.select_group_by_index(index)
        # Edit first group
        self.wd.find_element(By.NAME, "edit").click()
        self.fill_group_form(new_group_data)
        # Submit update
        self.wd.find_element(By.NAME, "update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def edit_group_by_id(self, id, new_group_data):
        self.open_group_page()
        self.select_group_by_id(id)
        # Edit some group
        self.wd.find_element_by_name("edit").click()
        self.fill_group_form(new_group_data)
        # Submit update
        self.wd.find_element_by_name("update").click()
        self.return_to_groups_page()
        self.group_cache = None

    def select_first_group(self):
        self.wd.find_element(By.NAME, "selected[]").click()

    def select_group_by_index(self, index):
        self.wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_group_by_id(self, id):
        self.wd.find_element(By.CSS_SELECTOR, "input[value='%s']" % id).click()

    def return_to_groups_page(self):
        self.wd.find_element(By.LINK_TEXT, "group page").click()

    def count(self):
        self.open_group_page()
        return len(self.wd.find_elements(By.NAME, "selected[]"))

    group_cache = None

    def get_group_list(self):
        if self.group_cache is None:
            self.open_group_page()
            self.group_cache = []
            for element in self.wd.find_elements(By.CSS_SELECTOR, "span.group"):
                text = element.text
                group_id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.group_cache.append(Group(name=text, group_id=group_id))
        return list(self.group_cache)
