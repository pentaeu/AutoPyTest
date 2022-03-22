from selenium.webdriver.common.by import By
from model.contact import Contact
import re


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
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def fill_contact_form(self, contact):
        self.update_field_data("firstname", contact.firstname)
        self.update_field_data("middlename", contact.middlename)
        self.update_field_data("lastname", contact.lastname)
        self.update_field_data("nickname", contact.nickname)
        self.update_field_data("title", contact.title)
        self.update_field_data("company", contact.company)
        self.update_field_data("address", contact.address)
        self.update_field_data("mobile", contact.mobilephone)
        self.update_field_data("home", contact.homephone)
        self.update_field_data("work", contact.workphone)
        self.update_field_data("email", contact.email1)
        self.update_field_data("email2", contact.email2)
        self.update_field_data("email3", contact.email3)

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new_contact_page()
        self.fill_contact_form(contact)
        # Submit creation
        wd.find_element(By.NAME, "submit").click()
        self.back_to_home_page()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # Delete address
        wd.find_element(By.XPATH, '//*[@id="content"]/form[2]/div[2]/input').click()
        # Accept delete
        wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements(By.NAME, "selected[]")[index].click()

    def edit_contact_by_index(self, index, new_contact_data):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # Go to update page
        wd.find_elements(By.CSS_SELECTOR, '[title="Edit"]')[index].click()
        self.fill_contact_form(new_contact_data)
        # Submit update
        wd.find_element(By.NAME, "update").click()
        self.back_to_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements(By.CSS_SELECTOR, '[title="Edit"]')[index].click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_elements(By.CSS_SELECTOR, '[title="Details"')[index].click()

    def back_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements(By.NAME, "entry"):
                cells = element.find_elements(By.TAG_NAME, "td")
                lastname = cells[1].text
                firstname = cells[2].text
                contact_id = element.find_element(By.NAME, "selected[]").get_attribute("value")
                all_phones = cells[5].text.splitlines()
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=contact_id,
                                                  homephone=all_phones[0], mobilephone=all_phones[1],
                                                  workphone=all_phones[2]))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element(By.NAME, "firstname").get_attribute("value")
        lastname = wd.find_element(By.NAME, "lastname").get_attribute("value")
        id = wd.find_element(By.NAME, "id").get_attribute("value")
        home_phone = wd.find_element(By.NAME, "home").get_attribute("value")
        work_phone = wd.find_element(By.NAME, "work").get_attribute("value")
        mobile_phone = wd.find_element(By.NAME, "mobile").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id, homephone=home_phone, mobilephone=mobile_phone,
                       workphone=work_phone)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element(By.ID, "content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        return Contact(homephone=home_phone, mobilephone=mobile_phone, workphone= work_phone)
