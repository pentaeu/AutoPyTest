from selenium.webdriver.common.by import By
from model.contact import Contact
from selenium.webdriver.support.ui import Select
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app
        self.wd = self.app.wd

    def open_add_new_contact_page(self):
        if not (self.wd.current_url.endswith("/edit.php") and len(self.wd.find_elements(By.NAME, "submit")) > 0):
            self.wd.find_element(By.LINK_TEXT, "add new").click()

    def update_field_data(self, field_name, text):
        if text is not None:
            self.wd.find_element(By.NAME, field_name).clear()
            self.wd.find_element(By.NAME, field_name).send_keys(text)

    def get_attribute_value_by_name(self, field_name):
        return self.wd.find_element(By.NAME, field_name).get_attribute("value")

    def fill_contact_form(self, contact):
        self.update_field_data("firstname", contact.firstname)
        self.update_field_data("middlename", contact.middlename)
        self.update_field_data("lastname", contact.lastname)
        self.update_field_data("nickname", contact.nickname)
        self.update_field_data("title", contact.title)
        self.update_field_data("company", contact.company)
        self.update_field_data("address", contact.address)
        self.update_field_data("mobile", contact.mobile_phone)
        self.update_field_data("home", contact.home_phone)
        self.update_field_data("work", contact.work_phone)
        self.update_field_data("email", contact.email1)
        self.update_field_data("email2", contact.email2)
        self.update_field_data("email3", contact.email3)

    def create(self, contact):
        self.open_add_new_contact_page()
        self.fill_contact_form(contact)
        # Submit creation
        self.wd.find_element(By.NAME, "submit").click()
        self.back_to_home_page()
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # Delete address
        self.wd.find_element_by_xpath("//input[@value='Delete']").click()
        # Accept delete
        self.wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        self.app.open_home_page()
        self.select_contact_by_id(id)
        self.wd.find_element_by_xpath("//input[@value='Delete']").click()
        self.wd.switch_to.alert.accept()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def select_first_contact(self):
        self.wd.find_element(By.NAME, "selected[]").click()

    def select_contact_by_index(self, index):
        self.wd.find_elements(By.NAME, "selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def edit_contact_by_index(self, index, new_contact_data):
        self.app.open_home_page()
        self.select_contact_by_index(index)
        # Go to update page
        self.wd.find_elements(By.CSS_SELECTOR, '[title="Edit"]')[index].click()
        self.fill_contact_form(new_contact_data)
        # Submit update
        self.wd.find_element(By.NAME, "update").click()
        self.back_to_home_page()
        self.contact_cache = None

    def edit_contact_by_id(self, id, new_contact_data):
        self.app.open_home_page()
        self.select_contact_by_id(id)
        # Go to update page
        self.wd.find_element_by_xpath("//a[@href='edit.php?id=%s']/img" % id).click()
        self.fill_contact_form(new_contact_data)
        # Submit update
        self.wd.find_element_by_name("update").click()
        self.back_to_home_page()
        self.contact_cache = None

    def open_contact_to_edit_by_index(self, index):
        self.app.open_home_page()
        self.wd.find_elements(By.CSS_SELECTOR, '[title="Edit"]')[index].click()

    def open_contact_to_view_by_index(self, index):
        self.app.open_home_page()
        self.wd.find_elements(By.CSS_SELECTOR, '[title="Details"')[index].click()

    def back_to_home_page(self):
        self.wd.find_element(By.LINK_TEXT, "home page").click()

    def count(self):
        self.app.open_home_page()
        return len(self.wd.find_elements(By.NAME, "selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            self.app.open_home_page()
            self.contact_cache = []
            for element in self.wd.find_elements(By.NAME, "entry"):
                cells = element.find_elements(By.TAG_NAME, "td")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                contact_id = cells[0].find_element(By.TAG_NAME, "input").get_attribute("value")
                all_phones = cells[5].text
                all_emails = cells[4].text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=contact_id,
                                                  all_phones_from_home_page=all_phones, address=address,
                                                  all_emails_from_home_page=all_emails))
        return list(self.contact_cache)

    def get_contact_info_from_edit_page(self, index):
        self.open_contact_to_edit_by_index(index)
        firstname = self.get_attribute_value_by_name("firstname")
        lastname = self.get_attribute_value_by_name("lastname")
        contact_id = self.get_attribute_value_by_name("id")
        address = self.get_attribute_value_by_name("address")
        home_phone = self.get_attribute_value_by_name("home")
        work_phone = self.get_attribute_value_by_name("work")
        mobile_phone = self.get_attribute_value_by_name("mobile")
        email1 = self.get_attribute_value_by_name("email")
        email2 = self.get_attribute_value_by_name("email2")
        email3 = self.get_attribute_value_by_name("email3")
        return Contact(firstname=firstname, lastname=lastname, id=contact_id, home_phone=home_phone, mobile_phone=mobile_phone,
                       work_phone=work_phone, email1=email1, email2=email2, email3=email3, address=address)

    def get_contact_info_from_view_page(self, index):
        self.open_contact_to_view_by_index(index)
        text = self.wd.find_element(By.ID, "content").text
        home_phone = re.search("H: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        return Contact(home_phone=home_phone, mobile_phone=mobile_phone, work_phone=work_phone)

    def add_contact_to_group_by_id(self, contact_id, group_id):
        self.app.open_home_page()
        self.select_contact_by_id(contact_id)
        self.wd.find_element_by_name("to_group").click()
        Select(self.wd.find_element_by_name("to_group")).select_by_value(group_id)
        self.wd.find_element_by_name("add").click()
        self.contact_cache = None

    def delete_contact_from_group(self, contact_id, group_id):
        self.app.open_home_page()
        self.wd.find_element_by_name("group").click()
        Select(self.wd.find_element_by_name("group")).select_by_value(group_id)
        self.wd.find_element_by_id(contact_id).click()
        self.wd.find_element_by_name("remove").click()
        self.contact_cache = None
