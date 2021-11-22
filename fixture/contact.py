from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ContactHelper:
    def __init__(self, app):
        self.app = app

    def open_contacts_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()

    def return_to_contacts_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home").click()

    def create(self, contact):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()
        self.fill_contact(contact)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[21]").click()

    def fill_contact(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        self.change_field_value("home", contact.homephone)
        self.change_field_value("mobile", contact.mobilephone)
        self.change_field_value("work", contact.workphone)
        self.change_field_value("fax", contact.fax)
        self.change_field_value("email", contact.email)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        if contact.bdate is not None:
            Select(wd.find_element(By.NAME, "bday")).select_by_visible_text(str(contact.bdate.day))
            Select(wd.find_element(By.NAME, "bmonth")).select_by_visible_text(contact.bdate.month)
            wd.find_element(By.NAME, "byear").send_keys(str(contact.bdate.year))
        if contact.adate is not None:
            Select(wd.find_element(By.NAME, "aday")).select_by_visible_text(str(contact.adate.day))
            Select(wd.find_element(By.NAME, "amonth")).select_by_visible_text(contact.adate.month)
            wd.find_element(By.NAME, "ayear").send_keys(str(contact.adate.year))
        self.change_field_value("address2", contact.address2)
        self.change_field_value("phone2", contact.phone2)
        self.change_field_value("notes", contact.notes)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).send_keys(text)

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        # select first contact
        wd.find_element(By.NAME, "selected[]").click()
        # submit deletion
        wd.find_element(By.XPATH, "//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_to_contacts_page()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        # select first group
        wd.find_element(By.NAME, "selected[]").click()
        wd.find_element(By.XPATH, "//img[@alt='Edit']").click()
        self.fill_contact(contact)
        wd.find_element(By.XPATH, "//div[@id='content']/form/input[22]").click()
        self.return_to_contacts_page()
