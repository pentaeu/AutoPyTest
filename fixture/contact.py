from selenium.webdriver.common.by import By


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_add_new_contact_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()

    def fill_the_form(self, contact):
        wd = self.app.wd
        # Fill firstname data
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").clear()
        wd.find_element(By.NAME, "firstname").send_keys(contact.firstname)
        # Fill middlename data
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").clear()
        wd.find_element(By.NAME, "middlename").send_keys(contact.middlename)
        # Fill lastname data
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").clear()
        wd.find_element(By.NAME, "lastname").send_keys(contact.lastname)
        # Fill nickname data
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").clear()
        wd.find_element(By.NAME, "nickname").send_keys(contact.nickname)
        # Fill company data
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").clear()
        wd.find_element(By.NAME, "company").send_keys(contact.company)
        # Fill address data
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").clear()
        wd.find_element(By.NAME, "address").send_keys(contact.address)
        # Fill email data
        wd.find_element(By.NAME, "email").click()
        wd.find_element(By.NAME, "email").clear()
        wd.find_element(By.NAME, "email").send_keys(contact.email)

    def create(self, contact):
        wd = self.app.wd
        self.open_add_new_contact_page()
        self.fill_the_form(contact)
        # Submit creation
        wd.find_element(By.NAME, "submit").click()
        self.back_to_home_page()

    def delete_first_contact(self):
        wd = self.app.wd
        # Go to home page
        wd.find_element(By.LINK_TEXT, "home").click()
        # Select address
        wd.find_element(By.NAME, "selected[]").click()
        # Delete address
        wd.find_element(By.XPATH, '//*[@id="content"]/form[2]/div[2]/input').click()
        # Accept delete
        wd.switch_to.alert.accept()

    def update_first_contact(self, contact):
        wd = self.app.wd
        # Go to home page
        wd.find_element(By.LINK_TEXT, "home").click()
        # Select address
        wd.find_element(By.NAME, "selected[]").click()
        # Go to update page
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()
        self.fill_the_form(contact)
        # Submit update
        wd.find_element(By.NAME, "update").click()
        self.back_to_home_page()

    def back_to_home_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()
