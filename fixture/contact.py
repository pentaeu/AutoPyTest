from selenium.webdriver.common.by import By
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements(By.NAME, "submit")) > 0):
            wd.find_element(By.LINK_TEXT, "add new").click()

    def update_field_data(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def fill_contact_form(self, contact):
        self.update_field_data("firstname", contact.firstname)
        self.update_field_data("middlename", contact.middlename)
        self.update_field_data("lastname", contact.lastname)
        self.update_field_data("nickname", contact.nickname)
        self.update_field_data("company", contact.company)
        self.update_field_data("address", contact.address)
        self.update_field_data("email", contact.email)

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new_contact_page()
        self.fill_contact_form(contact)
        # Submit creation
        wd.find_element(By.NAME, "submit").click()
        self.back_to_home_page()
        self.contact_cache = None

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_home_page(wd)
        self.select_first_contact(wd)
        # Delete address
        wd.find_element(By.XPATH, '//*[@id="content"]/form[2]/div[2]/input').click()
        # Accept delete
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def open_home_page(self, wd):
        wd.find_element(By.LINK_TEXT, "home").click()

    def select_first_contact(self, wd):
        wd.find_element(By.NAME, "selected[]").click()

    def edit_first_contact(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page(wd)
        self.select_first_contact(wd)
        # Go to update page
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()
        self.fill_contact_form(new_contact_data)
        # Submit update
        wd.find_element(By.NAME, "update").click()
        self.back_to_home_page()
        self.contact_cache = None

    def back_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page(wd)
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page(wd)
            self.contact_cache = []
            for element in wd.find_elements(By.NAME, "entry"):
                text = element.text
                contact_id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=text, contact_id=contact_id))
        return list(self.contact_cache)
